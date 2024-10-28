# Suanleme API SDK

共绩云算力平台的Python SDK，提供简单易用的API调用接口，内置加密签名实现。


- [API 加签文档 | 共绩算力](https://gongjiyun.com/docs/openapi/)
- [API 接口文档 | 共绩算力](https://gongjiyun.com/docs/openapi/api.html)

## 功能特性

- 完整的API签名和加密实现
- 任务全生命周期管理
- 简洁的接口设计
- 完善的错误处理

## 环境要求

- Python 3.7+

## 安装

```bash
pip install -r requirements.txt
```

## 快速开始

1. 获取接入凭证
   - 登录[共绩云管理后台](https://dockerweb.gongjiyun.com)
   - 导航至：账号管理 > API 管理 > 申请 Token
   - 生成RSA密钥对

2. 代码示例

```python
from suanleme_sdk import SuanlemeAPI

# 初始化客户端
api = SuanlemeAPI(
    token="your-token",
    pub_key="public.pem",  # RSA公钥路径
    pri_key="private.pem"  # RSA私钥路径
)

# 获取任务列表
tasks = api.get_all_tasks()

# 获取任务详情
task_info = api.get_task_info(task_id=123)
```

## API 文档

### 任务管理

| 方法 | 描述 |
|------|------|
| `get_all_tasks()` | 获取任务列表 |
| `get_task_info(task_id)` | 获取任务详情 |
| `get_task_nodes(task_id)` | 获取任务节点信息 |
| `cancel_task(task_id)` | 取消指定任务 |
| `create_task(params)` | 创建新任务 |

### 安全机制

#### API 签名流程

1. 构造签名字符串:

```
{path}\n{version}\n{timestamp}\n{token}\n{data}
```

2. RSA私钥签名（RSA-SHA256）
3. Base64编码签名结果

#### 数据加密

敏感接口的请求体处理流程：

1. JSON序列化
2. RSA公钥加密
3. Base64编码

## 配置说明

- 生产环境: `https://openapi.suanleme.cn/api`
- API版本: `1.0.0`

## 错误处理

SDK使用异常机制处理错误，建议使用 try-except 进行异常捕获：

```python
try:
    result = api.get_task_info(task_id=123)
except SuanlemeAPIError as e:
    print(f"API错误: {e}")
```
