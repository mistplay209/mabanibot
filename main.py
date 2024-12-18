from flask import Flask, request
import requests

app = Flask(__name__)

# توکن ربات را اینجا قرار بده
TOKEN = "8140337198:AAG66xEAxQhrmegDURVugQKwSdePOvOu_YY"

# مسیر اصلی برای دریافت پیام‌ها
@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
        if text == "/start":
            send_message(chat_id, "به ربات ساده خوش آمدید!")
        else:
            send_message(chat_id, f"شما گفتید: {text}")
    return "OK"

# تابع برای ارسال پیام
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot8140337198:AAG66xEAxQhrmegDURVugQKwSdePOvOu_YY/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    requests.post(url, json=payload)

# مسیر برای تنظیم وب‌هوک
@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    webhook_url = f"https://YOUR_REPLIT_URL/8140337198:AAG66xEAxQhrmegDURVugQKwSdePOvOu_YY"
    url = f"https://api.telegram.org/bot8140337198:AAG66xEAxQhrmegDURVugQKwSdePOvOu_YY/setWebhook"
    response = requests.post(url, data={"url": webhook_url})
    return response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

