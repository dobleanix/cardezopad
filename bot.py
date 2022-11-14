from datetime import *
from locale import currency
import requests
from telethon import *
import logging
import time
from random import *

logging.basicConfig(level=logging.INFO)

try:
    API_ID = ("24395180")
    API_HASH = ("34d74dd2a9fe59f8bd07676f1cb3d14a")
    TOKEN = ("5303936229:AAEIobvVIgClj0BZC5cO_yYXZEUGIF4josQ")
except ValueError:
    print("You forgot to fullfill vars")
    print("Bot is quitting....")
    exit()
except Exception as e:
    print(f"Error - {str(e)}")
    print("Bot is quitting.....")
    exit()

bot = TelegramClient('bin', API_ID, API_HASH)
bin = bot.start(bot_token=TOKEN)

#Responde al comando /start
@bin.on(events.NewMessage(pattern="^[.$!?/]start$"))
async def handler(event):
    welcome = await event.reply(f'**Bienvenido {event.sender.first_name} a @SakuraChkBot **')
    time.sleep(2)
    felici = await welcome.edit("**Cualquier duda que tengas no dudes en contactarme**")
    time.sleep(2)
    textWelcome = f"""
<b>Hola</b> @{event.sender.username}
<b>Para conocer nuestros comandos escribe /cmds</b>
<b>Tu UserID es:</b> {event.sender_id}
<b>Owner:</b> @camilafuentes
"""
    await felici.edit(textWelcome, parse_mode="HTML")

###############################

#responde al comando /gen
@bin.on(events.NewMessage(pattern="^[.$!?/]gen$"))
async def generador(event):
    textGen = f"""
<b>Hola</b> @{event.sender.username}
<b>Este comando estará disponible proximamente...</b>
<b>Tu UserID es:</b> {event.sender_id}
<b>🤖Bot by:</b> @camilafuentes
"""
    await event.reply(textGen, parse_mode="HTML")

################################

#Responde al comando /cmds
@bin.on(events.NewMessage(pattern="^[.$!?/]cmds$"))
async def comandos(event):
    textcmds = f"""
<b>Hey</b> @{event.sender.username}
<b>🔓 Estos son los comandos disponibles</b>
<b>/start - Iniciar bot</b>
<b>/bin - Información de la serie proporcionada</b>
<b>/ip - Checar nivel de riesgo de una IP (API dead, solo se puede ver info de la IP</b>
<b>/gen - Generador de tarjetas aleatorias</b>
<b>🤖Bot by:</b> @camilafuentes
"""
    await event.reply(textcmds, parse_mode="HTML")
###############################

#Responde al comando /ip
@bin.on(events.NewMessage(pattern="^[.$!?/]ip"))
async def ip_fruad(event):
    IPxx = await event.reply("📍🔜💻 Verificando en mi base de datos...")
    try:
      inputip = event.text.split(" ", maxsplit=1)[1]

      resu = requests.get(f'https://api.geoiplookup.net/?query='+inputip+'&json=true')
      result = resu.json()
      country = result['countryname']
      city = result['city']
      isp = result['isp']
      msgip = f'''
🔰IP: {inputip}
🌎País: {country}
🔵Ciudad: {city}
🔹ISP: {isp}
<b>🙍Checked By: @{event.sender.username}</b>
<b>🤖Bot by: @camilafuentes</b>
'''
      await IPxx.edit(msgip, parse_mode="HTML")
    except Exception as e:
      err = '❌ Por favor proporcione una IP validá [❌ Comando OFF]'
      await IPxx.edit(err)

###############################

#Responde al comando /bin
@bin.on(events.NewMessage(pattern="^[.$!?/]bin"))
async def binc(event):
    xx = await event.reply("💳🔜💻 Verificando en mi base de datos...")
    try:
        input = event.text.split(" ", maxsplit=1)[1]

        url = requests.get(f"https://bin-check-dr4g.herokuapp.com/api/{input}")
        res = url.json()
        brand = res['data']['vendor']
        bin = res['data']['bin']
        type = res['data']['type']
        level = res['data']['level']
        bank = res['data']['bank']
        country = res['data']['countryInfo']['name']
        emoji = res['data']['countryInfo']['emoji']
        currency = res['data']['countryInfo']['code']

        valid = f"""
<b>✅Bin Valid</b>
<b>⚜Bin: </b> <code>{bin}</code>
<b>💳Info: </b> <code>{brand} -</code><code> {type} -</code><code> {level}</code>
<b>🏛Bank: </b> <code>{bank}</code>
<b>🌎Country: </b> <code>{country} </code><code>{emoji}</code>
<b>💲Currency: </b> <code>{currency}</code>
<b>🙍Checked By: @{event.sender.username}</b>
<b>🤖Bot by: @camilafuentes</b>
"""
        await xx.edit(valid, parse_mode="HTML")
    except IndexError:
       await xx.edit("Porfavor proporcione 6 números para verificar\n__`/bin xxxxxx`__")
    except KeyError:
        await xx.edit(f"**⚜Bin -** `{input}`\n**❌Status -** `Invalid Bin`\n\n**🙍Checked By: ** @{event.sender.username}\n**Bot by: @camilafuentes**")
###############################

print ("Iniciando el bot")
bin.run_until_disconnected()
