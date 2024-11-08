import time
import json
import base64
from typing import List, Dict, Any, Optional
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_v1_5
import requests

# 当前 Python 示例仅基于 RSA BASE64 方式
class SuanlemeAPIBase:
    """
    基类，实现请求的签名和加密
    """

    # production
    BASE_URL = "https://openapi.suanleme.cn/api"

    PUBLIC_KEY = ""
    PRIVATE_KEY = ""

    def __init__(self, token: str, pub_key:str="pub.pem", pri_key:str="pri.pem"):
        """
        token: dockerweb 界面左侧账号管理通过api管理上传公钥生成
        pub_key: 生成token时上传的公钥文件路径
        pri_key: 公钥所对应的私钥文件路径
        """
        self.token = token
        self.PUBLIC_KEY = self.load_key(pub_key)
        self.PRIVATE_KEY = self.load_key(pri_key)

    @staticmethod
    def load_key(file_path: str) -> str:
        with open(file_path, "r") as file:
            content = file.read().strip()
            if len(content.splitlines()) == 1:
                content = f"-----BEGIN RSA PRIVATE KEY-----\n{content}\n-----END RSA PRIVATE KEY-----"
            return content

    def rsa_encrypt(self, message: str) -> str:
        key = RSA.import_key(self.PUBLIC_KEY)
        cipher = PKCS1_v1_5.new(key)
        ciphertext = cipher.encrypt(message.encode())
        return base64.b64encode(ciphertext).decode()

    def sign_request(self, headers: Dict[str, str], body: str, url: str) -> str:
        key = RSA.import_key(self.PRIVATE_KEY)
        signer = pkcs1_15.new(key)
        message = f"/api{url}\n{headers['version']}\n{headers['timestamp']}\n{headers['token']}\n{body}"
        hash_obj = SHA256.new(message.encode())
        signature = signer.sign(hash_obj)
        return base64.b64encode(signature).decode()

    """
    准备请求头和body, 对post请求的body进行加密
    """

    def prepare_headers(
        self, url: str, method: str, data: Optional[Dict[str, Any]] = None
    ) -> tuple:
        headers = {
            "version": "0.0.1",
            "timestamp": str(int(time.time() * 1000)),
            "Content-Type": "application/json",
            "token": self.token,
        }

        body = ""
        if method.lower() == "post" and data:
            body = json.dumps(data)
            if url in [
                "/login",
                "/user/login_and_register_sms",
                "/user/login_and_register",
                "/user/register/sms_verify",
            ]:
                body = self.rsa_encrypt(body)
                del headers["Content-Type"]

        headers["sign_str"] = self.sign_request(headers, body, url)
        return headers, body  # Return body instead of data

    """
    发送请求
    """

    def make_request(
        self, url: str, method: str = "GET", data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        try:
            full_url = f"{self.BASE_URL}{url}"
            headers, body = self.prepare_headers(url, method, data)

            if method.lower() == "get":
                response = requests.get(full_url, headers=headers, params=data)
            elif method.lower() == "post":
                response = requests.post(full_url, headers=headers, data=body)
            else:
                raise ValueError("不支持的HTTP方法")

            response.raise_for_status()  # 这会抛出 HTTPError 如果状态码不是 200
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"请求发生错误: {e}")
            # 可以选择重新抛出异常或返回一个默认值
            raise
        except ValueError as e:
            print(f"值错误: {e}")
            raise
        except Exception as e:
            print(f"发生未预期的错误: {e}")
            raise


class SuanlemeAPI(SuanlemeAPIBase):

    # 通过task id 获取任务信息
    def get_task_info(self, task_id: int) -> Dict[str, Any]:
        return self.make_request("/tasks/info", method="GET", data={"task_id": task_id})

    # 通过task id 获取任务节点信息
    def get_task_node_info(
        self, task_id: int, page: int = 1, status: str = "", machine: str = ""
    ) -> Dict[str, Any]:
        return self.make_request(
            "/tasks/point/download_list",
            method="GET",
            data={
                "task_id": task_id,
                "page": page,
                "status": status,
                "machine": machine,
            },
        )

    """
    获取当前页的任务列表
    """

    def get_task_list_page(self, page: int = 1, page_size: int = 10, search_value="") -> Dict[str, Any]:
        response = self.make_request(
            "/tasks/self_task",
            method="GET",
            data={"id": 1, "page": page, "page_size": page_size, "search_value": search_value},
        )

        if response.get("code") != "0000":
            raise ValueError(f"API Error: {response.get('message', 'Unknown error')}")

        # print("response in get_task_list:", response)
        tasks = response.get("data", {}).get("results", [])
        return {
            "tasks": {task["name"]: task["id"] for task in tasks},
            "total": response.get("data", {}).get("total", 0),
            "page": page,
            "page_size": page_size,
        }

    """
    获取提供页面内的所有任务
    """

    def get_all_tasks(self, max_pages: int = 3) -> Dict[str, int]:
        all_tasks = {}
        page = 1
        while True:
            task_data = self.get_task_list_page(page)
            all_tasks.update(task_data["tasks"])
            print(f"{task_data} for {page}")
            if len(task_data["tasks"]) < task_data["page_size"] or page >= max_pages:
                break
            page += 1
        return all_tasks

    """
    根据任务id取消任务
    """

    def cancel_task(self, task_id: int) -> Dict[str, Any]:
        print(f"Cancelling task {task_id}")
        result = self.make_request(
            "/tasks/cancel", method="POST", data={"task_id": task_id}
        )
        print(f"Cancel result for task {task_id}: {result}")
        return result

    # 创建任务，该接口暂未经过测试
    # GPU ID 查询：https://fizuclq6u3i.feishu.cn/wiki/FCQ3w0ZLei8Y7NkGOpxcCoEsnBc
    def create_task(
        self,
        name: str,
        desc: str,
        points: int,
        domain_prefix: str,
        docker_compose_content: str,
        cuda_version_required: List[str] | None = None,
        gpu_required: List[int] | None = None,
    ) -> Dict[str, Any]:
        """
        创建新任务
        
        Args:
            name: 任务名称
            desc: 任务描述
            points: 节点数量
            domain_prefix: 域名前缀
            docker_compose_content: docker-compose 配置内容
            
        Returns:
            Dict[str, Any]: API 响应结果
        """
        data = {
            "name": name,
            "desc": desc,
            "points": points,
            "domain_prefix": domain_prefix,
            "docker_compose_content": docker_compose_content,
            "cuda_version_required": cuda_version_required,
            "gpu_required": gpu_required,
        }
        
        return self.make_request("/tasks/publish", method="POST", data=data)

