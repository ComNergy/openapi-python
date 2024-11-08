from suanleme_sdk import SuanlemeAPI

api = SuanlemeAPI(
    token="<your-token>",
)

docker_compose_content = """services:
  # CPU 版 FFmpeg API 服务定义
  ffmpeg-api-cpu:
    image: harbor.suanleme.cn/library/ffmpeg-api:cpu  # 使用的 Docker 镜像，当前镜像是在公共仓库中
    restart: always
    network_mode: bridge # 使用桥接网络模式
    # 自定义标签用于服务标识
    labels:
      - suanleme_0.http.port=8000  # CPU API 的 HTTP 端口
      - suanleme_0.http.prefix=cpuapi  # CPU API 的 URL 前缀

  # GPU 版 FFmpeg API 服务定义
  ffmpeg-api-gpu:
    image: harbor.suanleme.cn/library/ffmpeg-api:gpu # 使用的 Docker 镜像，当前镜像是在公共仓库中
    restart: always
    network_mode: bridge # 使用桥接网络模式
    # 自定义标签用于服务标识
    labels:
      - suanleme_0.http.port=8000  # GPU API 的 HTTP 端口
      - suanleme_0.http.prefix=gpuapi  # GPU API 的 URL 前缀
    # 部署配置，分配 GPU 资源
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia  # 使用 NVIDIA GPU 驱动
              count: 1  # 预留的 GPU 数量
              capabilities: [ gpu ]  # 指定 GPU 功能
"""


print(api.create_task(
    name="te1st",
    desc="test",
    points=1,
    domain_prefix="test",
    docker_compose_content=docker_compose_content,
    cuda_version_required=["12.0", "12.1", "12.2", "12.3", "12.4", "12.5", "12.6", "12.7"],
    gpu_required=[16, 7],
))

print(api.get_task_list_page())