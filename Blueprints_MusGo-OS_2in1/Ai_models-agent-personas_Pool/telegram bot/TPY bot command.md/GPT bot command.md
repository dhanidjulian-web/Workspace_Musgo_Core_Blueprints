Saya sudah cek dokumentasinya. TPY (Telebot Python) di Telebot Creator mendukung command, chaining command, handleNextCommand, runCommand, runCommandAfter, penyimpanan data, API request, broadcast, dan berbagai fungsi bawaan lainnya. 

Berikut beberapa contoh command yang sering dipakai.

/start

bot.sendMessage(
"👋 Selamat datang " + message.from_user.first_name +
"\n\nGunakan /help untuk melihat menu."
)

/help

bot.sendMessage("""
📚 Daftar Perintah

/start - Mulai bot
/help - Bantuan
/id - Cek ID
/profile - Profil
/reminder - Pengingat
/color - Input warna favorit
""")

/id

bot.sendMessage(
"🆔 User ID: " + str(message.from_user.id)
)

/profile

bot.sendMessage(
"👤 Nama: " + message.from_user.first_name +
"\n🆔 ID: " + str(message.from_user.id)
)

/ping

bot.sendMessage("🏓 Pong!")

/random

import random

bot.sendMessage(
"🎲 Angka: " + str(random.randint(1,100))
)

/time

import time

bot.sendMessage(
"⏰ " + str(time.time())
)

/reminder

bot.sendMessage(
"⏳ Pengingat akan dikirim 60 detik lagi."
)

runCommandAfter(
60,
"send_reminder"
)

send_reminder

bot.sendMessage(
"🔔 Ini pengingat yang dijadwalkan."
)

/color

bot.sendMessage(
"Masukkan warna favorit kamu:"
)

handleNextCommand(
"save_color"
)

save_color

saveData(
"favorite_color_" + str(message.from_user.id),
message.text
)

bot.sendMessage(
"✅ Warna tersimpan: " + message.text
)

/mycolor

warna = getData(
"favorite_color_" + str(message.from_user.id)
)

bot.sendMessage(
"🎨 Warna favorit: " + str(warna)
)

/echo

if params:
bot.sendMessage(params)
else:
bot.sendMessage(
"Gunakan: /echo teks"
)

wildcard (*)

bot.sendMessage(
"❓ Perintah tidak dikenali."
)

at handler (@)

print(
"Pesan dari " +
str(message.from_user.id)
)Kalau yang Anda butuhkan level lanjut (HTTP API, OpenAI/GPT, scraper web, upload file, database user, sistem membership, panel admin, broadcast massal, crypto payment, URL shortener, downloader TikTok/YouTube, dll.), saya bisa buatkan 50+ command TPY siap tempel ke Telebot Creator dalam satu paket lengkap.

---
End Of Part
===========🔐™️®️©️🔐===========

---
Berikut paket command TPY yang berguna untuk berbagai kebutuhan bot Telegram di Telebot Creator.

########################################

SISTEM ADMIN

########################################

/admin

ADMIN_ID = 123456789

if message.from_user.id == ADMIN_ID:
bot.sendMessage("✅ Akses Admin")
else:
bot.sendMessage("❌ Ditolak")

########################################

BROADCAST

########################################

/bc

ADMIN_ID = 123456789

if message.from_user.id != ADMIN_ID:
bot.sendMessage("❌ Tidak diizinkan")
return

bot.sendMessage("Masukkan pesan broadcast:")
handleNextCommand("send_broadcast")

send_broadcast

pesan = message.text

users = getData("users")

for uid in users:
bot.sendMessageToUser(uid, pesan)

bot.sendMessage("✅ Broadcast selesai")

########################################

AUTO SAVE USER

########################################

@

users = getData("users")

if not users:
users = []

uid = message.from_user.id

if uid not in users:
users.append(uid)
saveData("users", users)

########################################

URL SHORTENER

########################################

/short

if not params:
bot.sendMessage("Contoh:\n/short https://google.com")
return

url = "https://tinyurl.com/api-create.php?url=" + params

result = HTTP.get(url)

bot.sendMessage(result)

########################################

QR GENERATOR

########################################

/qr

if not params:
bot.sendMessage("Contoh:\n/qr Halo Dunia")
return

link = "https://api.qrserver.com/v1/create-qr-code/?size=500x500&data=" + params

bot.sendPhoto(link)

########################################

PASSWORD GENERATOR

########################################

/password

import random
import string

pw = ''.join(
random.choice(
string.ascii_letters +
string.digits
) for i in range(16)
)

bot.sendMessage(
"🔑 " + pw
)

########################################

UUID GENERATOR

########################################

/uuid

import uuid

bot.sendMessage(
str(uuid.uuid4())
)

########################################

HASH MD5

########################################

/md5

import hashlib

if not params:
bot.sendMessage("/md5 text")
return

hashx = hashlib.md5(
params.encode()
).hexdigest()

bot.sendMessage(hashx)

########################################

BASE64 ENCODE

########################################

/b64e

import base64

if not params:
return

hasil = base64.b64encode(
params.encode()
).decode()

bot.sendMessage(hasil)

########################################

BASE64 DECODE

########################################

/b64d

import base64

if not params:
return

hasil = base64.b64decode(
params.encode()
).decode()

bot.sendMessage(hasil)

########################################

KALKULATOR

########################################

/calc

if not params:
bot.sendMessage(
"/calc 10+20"
)
return

try:
hasil = eval(params)
bot.sendMessage(
str(hasil)
)
except:
bot.sendMessage(
"Error"
)

########################################

CEK IP

########################################

/ip

if not params:
return

hasil = HTTP.get(
"http://ip-api.com/json/" +
params
)

bot.sendMessage(hasil)

########################################

RANDOM QUOTE

########################################

/quote

quote = HTTP.get(
"https://api.quotable.io/random"
)

bot.sendMessage(quote)

########################################

FAKTA ACAK

########################################

/fact

data = HTTP.get(
"https://uselessfacts.jsph.pl/api/v2/facts/random"
)

bot.sendMessage(data)

########################################

REMINDER

########################################

/remind

bot.sendMessage(
"Tulis pengingat:"
)

handleNextCommand(
"save_reminder"
)

save_reminder

saveData(
"reminder_" +
str(message.from_user.id),
message.text
)

runCommandAfter(
3600,
"send_reminder"
)

bot.sendMessage(
"✅ Reminder disimpan"
)

send_reminder

txt = getData(
"reminder_" +
str(message.from_user.id)
)

bot.sendMessage(
"🔔 Reminder:\n" +
str(txt)
)

########################################

AFK SYSTEM

########################################

/afk

saveData(
"afk_" +
str(message.from_user.id),
params
)

bot.sendMessage(
"AFK aktif"
)

@

afk = getData(
"afk_" +
str(message.from_user.id)
)

if afk:
deleteData(
"afk_" +
str(message.from_user.id)
)
bot.sendMessage(
"AFK dinonaktifkan"
)

########################################

LEVEL SYSTEM

########################################

@

xp = getData(
"xp_" +
str(message.from_user.id)
)

if not xp:
xp = 0

xp += 1

saveData(
"xp_" +
str(message.from_user.id),
xp
)

/rank

xp = getData(
"xp_" +
str(message.from_user.id)
)

bot.sendMessage(
"XP: " +
str(xp)
)

########################################

OPENAI CHAT API

########################################

/ai

prompt = params

payload = {
"model":"gpt-4o-mini",
"messages":[
{
"role":"user",
"content":prompt
}
]
}

headers = {
"Authorization":
"Bearer OPENAI_API_KEY"
}

result = HTTP.post(
"https://api.openai.com/v1/chat/completions",
payload,
headers
)

bot.sendMessage(result)

########################################

WEB SCRAPER SEDERHANA

########################################

/get

if not params:
return

html = HTTP.get(params)

bot.sendMessage(
html[:4000]
)

########################################

JSON VIEWER

########################################

/json

if not params:
return

hasil = HTTP.get(params)

bot.sendMessage(hasil)

########################################

UPTIME MONITOR

########################################

/monitor

saveData(
"target_" +
str(message.from_user.id),
params
)

runCommandAfter(
300,
"check_site"
)

check_site

url = getData(
"target_" +
str(message.from_user.id)
)

hasil = HTTP.get(url)

if hasil:
bot.sendMessage(
"✅ ONLINE"
)
else:
bot.sendMessage(
"❌ OFFLINE"
)Paket di atas mencakup:

Admin panel

Broadcast user

Database user

Reminder

AFK

Level/XP

URL Shortener

QR Generator

Password Generator

UUID

MD5/Base64

Calculator

IP Lookup

Quote & Fact API

HTTP Request

JSON Viewer

Web Scraper dasar

Monitoring website

Integrasi OpenAI


Untuk bot produksi, hindari penggunaan eval() pada command kalkulator karena berisiko jika menerima input tak tepercaya.