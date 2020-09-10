from helpers import kasus_hari_ini
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint
def start(update, context):
    update.message.reply_text("Halo, Selamat Datang di Bot NgodingPython")

def info(update, context):
    update.message.reply_text("Ini adalah Bot yang dibuat pada tanggal 17 Agustus 2020")

def main(update, context):
    update.message.reply_text("Saya Memikirkan Sebuah Angka, Coba Tebak")

def kasushariini(update, context):
    m = kasus_hari_ini()
    update.message.reply_text(m)

def tebakan(update, context):
    tebakan = int(update.message.text)
    if tebakan < angka:
        update.message.reply_text("Tebakan Kamu Kekecilan")
    elif tebakan > angka:
        update.message.reply_text("Tebakan Kamu Kegedean")
    else:
        update.message.reply_text("Tebakan Kamu Benar")

# MAIN PROGRAM
TOKEN = '1385555541:AAFYQslJmw-yfROBTlY0JJJvbu-04wfGLcY'
updater = Updater(TOKEN, use_context=True)

angka = randint(1,10)

dp = updater.dispatcher

# Menambah Command
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("info", info))
dp.add_handler(CommandHandler("main", main))
dp.add_handler(CommandHandler("kasus_hari_ini", kasushariini))

# Menambah Message Handler
dp.add_handler(MessageHandler(Filters.text, tebakan))

# run bot
updater.start_polling()
updater.idle()
