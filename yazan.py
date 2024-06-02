from hydrogram import Client, filters
import random, sys, time
from colorama import init, Fore
from hydrogram.enums import *
init(autoreset=True)
auto_reply = True
session = "BAFxEJUAdbTNpOuOz0Qrc1lOgccx5BNWOnCn8Qa6S6PSR5Cgnxpv9wLkanGZusAuXQsfQRTzph2izlhNGag6K7EHNI0_SFYeam3M6bo5Ln6YXvp6QWfudPR7aEAwxHu_QPoz6xjGdRoTtisFptKk4ppoG1mM-evbYHG3bK733Wu1SvbYpfl-KqhEVXMr-2Imes892rlfnMYQIOZBVDlBK6FzryGwPguX-PdJQPynj5kzF1cuzdPywjztlID8NzdwG78NZSlvpqPk1c8_M_6Ok_kArAB3qepeyK87loY3f-qyTIVTYk3dPNJwKMGHDMy10iqkLXyTZW5cXsGZhKyXBa1Z4A4ckQAAAAGVUMaNAA"
alfabe = "abcçdefgğıijklmnoöprsştuvyz"
bot = Client("ilk_yazan", api_id=24588661, api_hash="332058c74190c9a3739f43676f3a21e0", session_string=session)
toplanan = 0
yapilanlar = []
@bot.on_message(filters.text)
def boton(client, message):
  global auto_reply
  global toplanan
  global yapilanlar
  #print(Fore.RED + f"\n\n=============================\n\n" + Fore.GREEN + message.text + Fore.RED + "\n\n=============================")
  if message.chat.username == "sohbet_muhabbet_goygoy" and message.text.startswith("Yeni Bir İtiraf Var!"):
    return message.reply("ilk")
  if yapilanlar is not None:
    if message.chat.id in yapilanlar:
      uye = bot.get_chat_member(message.chat.id, message.from_user.id)
      if uye.status in [ChatMemberStatus.ADMINISTRATOR]:
        if message.reply_to_message.from_user.id == bot.get_me().id:
          time.sleep(2.5)
          bot.send_message(message.from_user.id, random.choice([".", ",", "Sa"]))
          yapilanlar.remove(message.chat.id)
  if message.text.startswith(".cevapla"): 
    if str(message.from_user.id) != "7087656547" and message.from_user.id != bot.get_me().id:
      return
    textsp = message.text.split()
    if len(textsp) == 2:
        if textsp[1].lower() == "on":
          bot.delete_messages(message.chat.id, message.id)
          m = message.reply("Aktif ediliyor... ")
          time.sleep(2.5)
          auto_reply = True
          m.edit("**𝗂𝗅𝗄 𝗒𝖺𝗓𝖺𝗇 𝗍𝗈𝗉𝗅𝖺𝗆𝖺 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂.**")
        elif textsp[1].lower() == "off":
          bot.delete_messages(message.chat.id, message.id)
          m = message.reply("Bot kapatılıyor...")
          time.sleep(2.5)
          auto_reply = False
          m.edit("**𝗂𝗅𝗄 𝗒𝖺𝗓𝖺𝗇 𝗍𝗈𝗉𝗅𝖺𝗆𝖺 𝗄𝖺𝗉𝖺𝗍ı𝗅𝖽ı.**")
  elif message.text == ".alive" and message.from_user.id == bot.get_me().id:
    me = bot.get_me();
    bot.delete_messages(message.chat.id, message.id)
    m = message.reply("**𝗂𝗅𝗄 𝗒𝖺𝗓𝖺𝗇 𝗌𝖺𝗒𝗂𝗌𝗂 𝖺𝗅𝗂𝗇𝗂𝗒𝗈𝗋 𝖻𝗎 𝗂𝗌𝗅𝖾𝗆 𝖻𝗂𝗋𝖺𝗓 𝗌𝗎𝗋𝖾𝖻𝗂𝗅𝗂𝗋.**")
    time.sleep(2.5)
    m.edit(f'''
@{me.username}

**𝖧𝖾𝗌𝖺𝖻𝗂𝗇𝖽𝖺 𝗍𝗈𝗉𝗅𝖺𝗆 𝖽𝖺 {toplanan} 𝗍𝖺𝗇𝖾 𝗂𝗅𝗄 𝗒𝖺𝗓𝖺𝗇 𝗍𝗈𝗉𝗅𝖺𝖽𝗂𝗆.**''')
  if auto_reply == False:
    return

  if ChatType.CHANNEL or ChatType.PRIVATE:
    return
  if message.text.replace("İ", "i").lower().startswith("ilk") or "ilk" in message.text.replace("İ", "i").lower():
    if message.forward_from_chat and "-100" in  str(message.forward_from_chat.id):
      
      text = message.text.replace("İ", "i")
      words = text.split()
      try:
        index_start = words.index("ilk")
        index_end = words.index("yazana")
        keywords = words[index_start + 1:index_end]    
        message.reply(" ".join(keywords))
        yapilanlar.append(message.chat.id)
        toplanan += 1
        bot.send_photo(chat_id="vpnteam32", photo="https://telegra.ph/file/27352362b962056c53aa3.jpg", caption="**𝖸𝖤𝖭𝖨 𝖨𝖫𝖪 𝖸𝖠𝖹𝖠𝖭:**\n\n**𝖦𝗋𝗎𝗉 𝗂𝖽𝗂:** `{}`\n\n**𝖦𝗋𝗎𝗉 𝖺𝖽𝗂:** {}".format(message.chat.id, message.chat.title))
      except:
        if "ilk yazan" in message.text.replace("İ", "i").lower() and message.forward_from_chat:
          if "-100" in str(message.forward_from_chat.id):
            message.reply("".join(random.sample(alfabe, k=1)))
            yapilanlar.append(message.chat.id)           
            toplanan += 1
            bot.send_photo(chat_id="vpnteam32", photo="https://telegra.ph/file/27352362b962056c53aa3.jpg", caption="**𝖸𝖤𝖭𝖨 𝖨𝖫𝖪 𝖸𝖠𝖹𝖠𝖭:**\n\n**𝖦𝗋𝗎𝗉 𝗂𝖽𝗂:** `{}`\n\n**𝖦𝗋𝗎𝗉 𝖺𝖽𝗂:** {}".format(message.chat.id, message.chat.title))    
           
bot.run();