# 使用已经安装好 Python 的基础镜像
FROM python:3.13-slim

# Python 日志立即输出
ENV PYTHONUNBUFFERED=1

# 设置容器内部的工作目录
WORKDIR /app

# 把电脑上的程序复制进镜像
COPY app.py /app/app.py

# 说明程序使用的端口
EXPOSE 8000

# 容器启动时执行的命令
CMD ["python", "app.py"]
