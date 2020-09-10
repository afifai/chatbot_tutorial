from helpers import kasus_hari_ini
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint
from io import BytesIO

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

def save(update, context):
    chat_id = str(update.update_id)
    file_image = update.message.photo[0].get_file()
    f = BytesIO(file_image.download_as_bytearray())
    with open("images/"+chat_id+".jpg", "wb") as fi:
        fi.write(f.getbuffer())
    #update.message.reply_text("Foto Anda telah tersimpan")
    update.message.reply_photo(open("images/"+chat_id+".jpg", "rb"))

# MAIN PROGRAM
TOKEN = 'YOUR TOKEN'
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
dp.add_handler(MessageHandler(Filters.photo, save))

# run bot
updater.start_polling()
updater.idle()
