import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# توکن ربات تلگرام خود را اینجا وارد کن
TOKEN = '8140337198:AAG66xEAxQhrmegDURVugQKwSdePOvOu_YY'

# راه‌اندازی logging برای خطایابی
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور start که وقتی کاربر وارد ربات می‌شود، اجرا می‌شود
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! من ربات شما هستم.')

# دستور help که کمک‌های ساده‌ای ارائه می‌دهد
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('برای شروع از دستور /start استفاده کن.')

def main():
    """شروع ربات و تنظیمات webhook"""
    updater = Updater8140337198:AAG66xEAxQhrmegDURVugQKwSdePOvOu_YY

    # دریافت دیسپاچر برای ثبت هندلرها
    dispatcher = updater.dispatcher

    # ثبت هندلرها برای دستورات مختلف
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
