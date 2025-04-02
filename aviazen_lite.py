from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import urllib.parse

# Aviasales affiliate link bazasi
AFFILIATE_LINK_BASE = "https://tp.media/r?marker=619458&trs=404323&p=4114&u=https%3A%2F%2Faviasales.com%2Fsearch%2F{from_city}{date}{to_city}1&campaign_id=100"

# Foydalanuvchini boshlash komandasi
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "✈️ Salom! Men Aviazen Lite botman.\n"
        "Qayerdan qayerga uchmoqchisiz?\n\n"
        "Masalan: Tashkent Istanbul"
    )

# Foydalanuvchi yozgan yo‘nalishni ishlovchi funksiyasi
def search_ticket(update: Update, context: CallbackContext):
    text = update.message.text
    try:
        from_city, to_city = text.strip().split()

        from_code = city_to_iata(from_city)
        to_code = city_to_iata(to_city)
        date = "01"  # oddiy sinov sanasi

        link = AFFILIATE_LINK_BASE.format(from_city=from_code, to_city=to_code, date=date)

        # CHIROYLI LINK
        update.message.reply_text(
            f"✈️ Siz uchun arzon chipta: <a href='{link}'>Aviasales orqali qidirish</a>",
            parse_mode='HTML'
        )

    except:
        update.message.reply_text("❗Iltimos, shunday yozing: Tashkent Istanbul")
# IATA kodlarni oddiy dictionary orqali aniqlash (asosiy sinov uchun)
def city_to_iata(city):
    city = city.lower()
    mapping = {
        "tashkent": "TAS",
        "istanbul": "IST",
        "moscow": "MOW",
        "dubai": "DXB",
        "newyork": "NYC",
        "london": "LON",
        "paris": "PAR",
        "seoul": "SEL",
        "tokyo": "TYO"
    }
    return mapping.get(city, "TAS")  # Agar topilmasa default TAS

# Botni ishga tushirish
def main():
    updater = Updater("8128482653:AAHPBfPpinWcif2IBiSfn_3VILBcJ3nBkdw", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_ticket))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
