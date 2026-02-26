import telebot

TOKEN = "8579345468:AAF863QHv_DM7Kq_O57aFJz6acZbI2phPnU"
CHANNEL_ID = -1003614805156 # Keyin to‘ldiramiz

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Taksi bot ishga tushdi 🚕")

@bot.message_handler(func=lambda message: True)
def group_filter(message):
    text = message.text.lower()

    if "menga taksi kerak" in text or "menga mashina kerak" in text or "odam bor" in text:

        username = message.from_user.username
        if username:user_text = f"@{username}"
        else:user_text = message.from_user.first_name

        info = f"""
<b>🚕 YANGI BUYURTMA</b>

👥 Guruh: {message.chat.title}
📝 Matn: {message.text}
👤 User: {user_text}
🆔 ID: {message.message_id}
"""

        bot.send_message(CHANNEL_ID, info, parse_mode="HTML")

bot.polling()