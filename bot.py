import telebot
import os
import google.generativeai as genai

# Setup
BOT_TOKEN = '8997639190:AAFobB_hL5bYClQWyAvlwI4XiZLpf4sR60U'
# Model ka naam change kar diya hai
model = genai.GenerativeModel('gemini-1.5-flash') 

bot = telebot.TeleBot(BOT_TOKEN)
BAD_WORDS = ['gaali1', 'gaali2', 'chutiya', 'madarchod']

# 1. Rules Command
@bot.message_handler(commands=['rules'])
def send_rules(message):
    rules = (
        "📜 WELCOME TO OUR GROUP 📜\n\n"
        "🚨 YAHAN KE KADAK RULES: 🚨\n"
        "1️⃣ Badtameezi, gaali-galoch ya lafda kiya toh seedha BAN! 🚫\n"
        "2️⃣ Bina permission ke links ya spamming mat karna. 🔗\n"
        "3️⃣ Sabhi members ki respect karein. 🤝\n"
        "4️⃣ RESPECT ADMINS SPECIALLY PRIME DEVIL 👑\n"
        "5️⃣ RESPECT ALL ✊\n"
        "6️⃣ GALI DI AUR FIR GHAMAND DIKHAYA TO TERA INFORMATION LEAK HOGA SAMJHA LOMDE 😒💀"
    )
    bot.reply_to(message, rules)

# 2. Welcome Message
@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    for user in message.new_chat_members:
        bot.reply_to(message, f"🌟 Welcome {user.first_name}! Rules padh lena, warna seedha BAN mil jayega!")

# 3. Filter & AI Chat
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    # Link & Bad words check
    if message.text:
        text = message.text.lower()
        if 'http' in text or 't.me' in text:
            bot.delete_message(message.chat.id, message.message_id)
            return
        
        if any(word in text for word in BAD_WORDS):
            bot.delete_message(message.chat.id, message.message_id)
            return

    # AI Chat: Sirf agar @RULE_STROM_BOT mention ho YA bot ke message ka reply diya ho
    bot_username = "RULE_STROM_BOT"
    is_mentioned = (message.text and f"@{bot_username}" in message.text)
    is_reply = (message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id)

    if is_mentioned or is_reply:
        try:
            response = model.generate_content(message.text)
            bot.reply_to(message, response.text)
        except Exception as e:
            print(f"AI Error: {e}")

print("Bot is running...")
bot.infinity_polling()
