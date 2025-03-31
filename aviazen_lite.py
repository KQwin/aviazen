from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Sizning affiliate havolangiz (marker=619458)
AFFILIATE_LINK = "https://tp.media/r?marker=619458&search_url=https://avia.travelpayouts.com/?params=from:{from_city};to:{to_city}&locale=uz"

# /start komandasi uchun funksiyamiz
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "✈️ Salom! Men Aviazen Lite botman.\n"
        "Qayerdan qayerga uchmoqchisiz?\n\n"
        "Misol uchun: Tashkent Istanbul"
    )

# Foydalanuvchi yozgan matndan yo‘nalish chiqarish
def search_ticket(update: Update, context: CallbackContext):
    text = update.message.text
    try:
        from_city, to_city = text.strip().split()
        link = AFFILIATE_LINK.format(from_city=from_city, to_city=to_city)
        update.message.reply_text(f"🔗 Siz uchun chipta qidiruvi: {link}")
    except:
        update.message.reply_text("❗Iltimos, shunday yozing: Tashkent Istanbul")

# Botni ishga tushirish funksiyasi
def main():
    updater = Updater("8128482653:AAHPBfPpinWcif2IBiSfn_3VILBcJ3nBkdw", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_ticket))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
