import telebot

# Naya Token update kar diya hai
TOKEN = '8997639190:AAFobB_hL5bYClQWyAvlwI4XiZLpf4sR60U'
bot = telebot.TeleBot(TOKEN)

# 1. Welcome Message
@bot.message_handler(content_types=['new_chat_members'])
def welcome_message(message):
    for user in message.new_chat_members:
        welcome_text = (
            f"🌟 Hello {user.first_name}! Welcome to our family! 🌟\n\n"
            "Rules padh lena, warna seedha BAN mil jayega. Enjoy!"
        )
        bot.reply_to(message, welcome_text)

# 2. Rules Command
@bot.message_handler(commands=['rules'])
def send_rules(message):
    rules_text = (
        "📜 WELCOME TO OUR GROUP 📜\n\n"
        "🚨 YAHAN KE KADAK RULES: 🚨\n"
        "1️⃣ Badtameezi, gaali-galoch ya lafda kiya toh seedha BAN! 🚫\n"
        "2️⃣ Bina permission ke links ya spamming mat karna. 🔗\n"
        "3️⃣ Sabhi members ki respect karein. 🤝\n"
        "4️⃣ RESPECT ADMINS SPECIALLY PRIME DEVIL 👑\n"
        "5️⃣ RESPECT ALL ✊\n"
        "6️⃣ GALI DI AUR FIR GHAMAND DIKHAYA TO TERA INFORMATION LEAK HOGA SAMJHA LOMDE 😒💀"
    )
    bot.reply_to(message, rules_text)

# 3. Link & Bad Words Filter
BAD_WORDS = ['gaali1', 'gaali2', 'chutiya', 'madarchod'] # Yahan apni gaaliyan add kar

@bot.message_handler(func=lambda message: True)
def filter_everything(message):
    # Link Check
    if 'http' in message.text.lower() or 't.me' in message.text.lower():
        bot.delete_message(message.chat.id, message.message_id)
        bot.reply_to(message, "⚠️ Link allow nahi hai!")
        return
    
    # Bad Words Check
    if any(word in message.text.lower() for word in BAD_WORDS):
        bot.delete_message(message.chat.id, message.message_id)
        bot.reply_to(message, "❌ Gaali dena mana hai, rules padh le!")

# Is part ko purane bot.polling ki jagah paste kar
print("Bot is running...")
bot.infinity_polling()

