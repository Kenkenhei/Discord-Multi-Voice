import os
import threading
from flask import Flask

# 1. Tạo Web Server ảo để "qua mặt" Render lấy gói Free $0
app = Flask(__name__)


@app.route("/")
def home():
    return "Self-bot đang treo thành công 24/7!", 200


def run_self_bot():
    # 2. Gọi file self-bot gốc của bạn lên chạy ngầm độc lập
    os.system("python self-bot.py")


if __name__ == "__main__":
    # Chạy self-bot trong một luồng riêng để không làm kẹt Web Server
    threading.Thread(target=run_self_bot, daemon=True).start()

    # Mở port 10000 theo yêu cầu bắt buộc của Render gói Free
    app.run(host="0.0.0.0", port=10000)
