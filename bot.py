import os
import telebot
from flask import Flask, request

# استيراد توكن البوت من المتغيرات البيئية
TOKEN = os.getenv("BOT_TOKEN")  # قم بتعيينه في Render لاحقًا
bot = telebot.TeleBot(TOKEN)

# إنشاء أمر /start للترحيب بالمستخدم
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا بك في AIMX Mining Bot! 🚀")

# تشغيل البوت
if __name__ == "__main__":
    bot.polling()
