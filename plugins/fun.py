from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import random, re



RUN_STRINGS = (
  "Oh.. insolence... same as before....there is no change....it's not the spit that doesn't hold the course....!!!",
  "Allah... each of the children's... passion...",
  "Sir, I don't know how to write... I don't know how to read....",
  "Don't be silent today... After today's fort.....",
  "Thinking that it is ash, it will burn if you don't build a coal that doesn't stand to burn.",
  "Understand that there is only one life, there is no heaven and no hell, 'one life', where and how he wants it.",
  "What a bombastic explosion! Such a terrific disclosure!!",
  "Go Away Stupid In The House Of My Wife And Daughter You Won't See My Minute Of Today... Don't Get Down..",
  "I Can Do That Do Can I That",
  "Just because cream biscuits have cream, tiger biscuits don't necessarily have tiger. Work will be done, man...",
  "It's like when you get scared and go to the ballpark, you are told to go to the ballpark.",
  "My Lord.... You will not allow me to be good.",
  "Car engine out completely......",
  "Don't get tired of it!!",
  "Porotta and chicken that your father made at midnight....",
  "Oh, and when you fall in love, it's love.... When we fall in love, it's wire....",
  "God save me only....",
  "Waste of toddy and wet rain drunk for her....",
  "Where have you been all this time?....!",
  "English is not very good....",
  "All the Dreams Like Twinkle Stars...",
  "My Prantan Muthappa give him a way",
  "Ali, will you give me the dowry amount?",
  "You are very tired",
  "He was waiting with tears in his eyes.",
  "Chellakandu said, don't go. Ya .\
   SHUT UO YOUR MOUTH BLOODY gramavasis.",
  "Go shit .\
   To die with you patto.",
  "Because of you, the locals and those who left Gunollya, why are Gunollya living like this? .", 
)


IKKA_STRINGS = (
    "CAACAgUAAxkBAAIDUmIN8bqiD5DYQLjQzUwH7-1AsH0eAAJGBAAClj7wVxJlL3v8QuaoHgQ",
    "CAACAgUAAxkBAAIDVmIN8cCiVJZl05m0wiggUJaOvYarAAL5BAACo7lRVClze9Et3bCJHgQ",
    "CAACAgUAAxkBAAIDV2IN8cSKz20_0T-f7BlHVQfQYPu_AAKfAwACA4rwV01BOgyNllX1HgQ",
    "CAACAgUAAxkBAAIDWGIN8coT1jTnXpetiFOKVGZVCX78AAJLBAACrXgAAVTcB_E8ndEu0h4E",
    "CAACAgUAAxkBAAIDWWIN8c-GSo6HX8bmIvJOwDXG1pJ-AAJkBAACbYZIVIF7psBskaRiHgQ",
    "CAACAgUAAxkBAAIDWmIN8dfwrILfwAABBczAR4DoYxpkvAACvwUAAlNOSFRraTuQ8L5Qzx4E",
    "CAACAgUAAxkBAAIDXGIN8eN4RRZPSvKW5OcDhBGnF_qIAAJtBQACwq0JVAnAmIgTMZr6HgQ",
    "CAACAgUAAxkBAAIDeGIN8ke0Qm7S8rWAp5XRHtG21RP1AAJzBQACg5tAVL8bVAS2wafYHgQ",
    "CAACAgUAAxkBAAIDfGIN8lvvH0C9VGSLMV7fvxJ9L_r9AAIlBgACf4hJVA_SXDgpTipeHgQ",
    "CAACAgUAAxkBAAIDf2IN8nL54y-xsW_PGMX5T96e_ErnAAJiAwACjh3YV6f4T7ZwQqExHgQ",
    "CAACAgUAAxkBAAIDgmIN8oZFf70SfKUOl9nnk0Q0uIGPAAJjAwAC3-lRVqPrbp8AAeUBch4E",
    "CAACAgUAAxkBAAIDj2IN86K_5xEpxc00sVRoFLgNgvh_AALeAgACh49oVh2VB0KUEX3zHgQ",
    "CAACAgUAAxkBAAIDkmIN87LWn-56jo9wHTdifHsdBCAiAAJPAwACK4yZVlCyU1tXbk2YHgQ",
) 


@Client.on_message(filters.command("dice"))
async def roll_dice(bot, message):
    await bot.send_dice(message.chat.id, "🎲")

@Client.on_message(filters.command("arrow"))                                      
async def roll_arrow(bot, message):
    await bot.send_dice(message.chat.id, "🎯")

@Client.on_message(filters.command("goal"))
async def roll_goal(bot, message):
    await bot.send_dice(message.chat.id, "⚽️")

@Client.on_message(filters.command("luck"))
async def roll_luck(bot, message):
    await bot.send_dice(message.chat.id, "🎰")

@Client.on_message(filters.command("throw"))
async def roll_throw(bot, message):
    await bot.send_dice(message.chat.id, "🏀")

@Client.on_message(filters.command(["bowling", "tenpins"]))
async def roll_bowling(bot, message):
    await bot.send_dice(message.chat.id, "🎳")

@Client.on_message(filters.command("runs"))
async def runs(bot, message):
    fun_txt = random.choice(RUN_STRINGS)
    await message.reply_text(fun_txt)

@Client.on_message(filters.command("ikka"))
async def ikka(bot, message):
    pic = random.choice(IKKA_STRINGS)
    await message.reply_sticker(pic)

@Client.on_message(filters.command("brain", ".") & filters.me)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("brain")
    animation_chars = [          
              "Your Brain ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
              "Your Brain ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
              "Your Brain ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
              "Your Brain ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
              "Your Brain ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
              "Your Brain ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
              "Your Brain ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
              "Your Brain ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
              "Your Brain ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
              "Your Brain ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
              "Your Brain ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
              "Your Brain ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
              "Your Brain ➡️ 🧠\n\n           (> ^_^)>🗑",
              "Your Brain ➡️ 🧠\n\n           <(^_^ <)🗑",
          ]
    for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i %14 ])
		
