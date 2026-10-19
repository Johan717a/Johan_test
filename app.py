from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock


COUNT_FILE = Path("data/count.txt")
COUNT_FILE.parent.mkdir(parents=True, exist_ok=True)
COUNT_LOCK = Lock()
# 用来保存访问次数的文件
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 浏览器请求图标时，不增加访问次数
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        # 这个示例只提供首页
        if self.path != "/":
            self.send_error(404)
            return

        # 读取之前的访问次数
        if COUNT_FILE.exists():
            count = int(COUNT_FILE.read_text(encoding="utf-8"))
        else:
            count = 0

        # 次数加一，并保存
        count += 1
        COUNT_FILE.write_text(str(count) + "\n", encoding="utf-8")

        # 生成页面内容
        html = f"""
        <!doctype html>
        <html lang="zh-CN">
        <meta charset="utf-8">
        <title>我的 Python 项目</title>
        <h1>你好，Python！</h1>
        <p>这是我的第一个 Docker + Python 项目。</p>
        <p>累计访问次数：{count}</p>
        <a href="/">再访问一次</a>
        </html>
        """

        # 把网页发送给浏览器
        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8000), Handler)
    print("Python 服务已启动，监听 8000 端口", flush=True)
    server.serve_forever()
