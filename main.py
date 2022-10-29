import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("2026567765:AAGiABbTY1r80L-L_zox67akSCP7r9by9P4")

def getMeaning(word):
    url = f"https://www.myordbok.com/definition?q={word}"
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content,"html.parser")
    formatted = """"""
    try:
        meaningList = soup.find("div",class_="meaning")
        pos = meaningList.find_all("div",class_="pos")
        for i in pos:
            letter_type = i.find_all("h2")[0].getText()
            formatted += f"\n {letter_type} \n\n"
            text = i.find_all("p")
            for elem in text:
                myanmar_meaning = elem.getText()
                formatted += f"{myanmar_meaning}"       
    except:
        formatted = "Can't Find your words" 

    return formatted

@bot.message_handler(commands=["start","codejapoe"])
def start(message):
    text = "Welcome to Eng-Mm Dictionary Bot.\nHere are the commands\n/search word\n/about"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['search'])
def search(message):
    text = message.text
    text = text.replace("/search ","")
    meaning = getMeaning(text)
    user_data = "{} {} searched '{}'".format(message.from_user.first_name, message.from_user.last_name, text)
    bot.send_message(-588064518, user_data)
    bot.send_message(message.chat.id, meaning)

@bot.message_handler(content_types=["sticker", "video", "photo", "audio", "voice", "location", "contact", "document"])
def forward(message):
    data = "From {} {}".format(message.from_user.first_name, message.from_user.last_name)
    bot.forward_message(-588064518, message.chat.id, message.message_id)
    bot.send_message(-588064518, data)

@bot.message_handler(commands=['about'])
def about(message):
    us = "Created on 18 Sep and modified on 19 Sep.\nCreators: Code Ja Poe, Coding with KKO"
    bot.send_message(message.chat.id, us)

@bot.message_handler(content_types=["text"])
def browse(message):
    text = message.text
    meaning = getMeaning(text)
    user_data = "{} {} searched '{}'".format(message.from_user.first_name, message.from_user.last_name, text)
    bot.send_message(-588064518, user_data)
    bot.send_message(message.chat.id, meaning)

bot.polling()
