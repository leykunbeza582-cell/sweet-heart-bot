import os
import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(level=logging.INFO)

LOVE_MESSAGES = [
    "❤️ ፍቅር በቃላት ብቻ ሳይሆን በተግባር ይገለጣል።",
    "🌹 ፈገግታሽ የቀኔ ብርሃን ነው።",
    "💕 ከልብ የሚወድ ሰው ሁሌም ለአንተ ጊዜ ያገኛል።",
    "🥰 አንተ ለአንድ ሰው የዓለም ሁሉ ደስታ ልትሆን ትችላለህ።"
]

POEMS = [
    "🌹 ዓይኖችሽ ኮከቦች፣\nፈገግታሽ ጨረቃ፣\nበልቤ ውስጥ አንቺ፣\nየማትጠፊ ብርሃን ነሽ። ❤️",
    "💕 በየቀኑ ስታስቂ፣\nልቤ ደስ ይለዋል፣\nፍቅርሽ በውስጤ፣\nእንደ አበባ ያብባል። 🌹"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "❤️ እንኳን ወደ Sweet Heart Bot በደህና መጡ! ❤️\n\n"
        "💕 የፍቅር መልዕክቶች\n"
        "🌹 የፍቅር ግጥሞች\n"
        "💌 የፍቅር ጥቅሶች\n\n"
        "ከሚከተሉት ቃላት አንዱን ይላኩ፦\n"
        "love — የፍቅር መልዕክት\n"
        "poem — የፍቅር ግጥም\n"
        "quote — የፍቅር ጥቅስ\n"
        "help — እገዛ"
    )
    await update.message.reply_text(text)

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower().strip()

    if message in ["love", "ፍቅር", "መልዕክት"]:
        reply = random.choice(LOVE_MESSAGES)
    elif message in ["poem", "ግጥም"]:
        reply = random.choice(POEMS)
    elif message in ["quote", "ጥቅስ"]:
        reply = "❤️ እውነተኛ ፍቅር ማለት አንዱ ሌላውን በክብር፣ በታማኝነት እና በመረዳት መውደድ ነው።"
    elif message in ["help", "እገዛ"]:
        reply = "❤️ love ለመልዕክት፣ poem ለግጥም፣ quote ለጥቅስ ይላኩ።"
    else:
        reply = "❤️ ሰላም! የፍቅር መልዕክት ለማግኘት love፣ ግጥም ለማግኘት poem ወይም ጥቅስ ለማግኘት quote ይላኩ።"

    await update.message.reply_text(reply)

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN environment variable is missing")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))
    app.run_polling()

if __name__ == "__main__":
    main()
