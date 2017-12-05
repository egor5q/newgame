# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
import random
import threading
from telebot import types
token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)

currentchat=[]

@bot.message_handler(commands=['start'])
def startmessage(message):
  m=message.from_user.id
  bot.send_message(m, 'Приветствую тебя в игре "MagicWars! Здесь тебе предстоит научиться создавать свои мистические войска и сражаться с друзьями'+
                  ', а так же изучать особенности каждого своего воина! Жми /help, чтобы узнать всё в подробностях') 
                  
                   




@bot.message_handler(commands=['help'])
def helpmessage(message):
  bot.send_message(message.from_user.id, 'Чтобы сыграть в игру, добавьте меня в чат и напишите /begin для начала набора игроков.'+"\n"+
                   'Пока что доступен только режим игры 1 на 1, но в будущих обновлениях будут добавлены командные бои!'+"\n"+"\n"+
                   'В этой игре вы играете за одного из магов, который обороняет свою крепость, или нападает на чужую! '+
                   'Чтобы атаковать врага, вы призываете специальный алтарь, на котором каждый новый ход появляется одно из ваших выбранных '+
                   'существ (для каждого существа свой алтарь), которое вступает в бой с существами врагов, и разделавшись с ними, идет в атаку на крепость.'+
                   ' Все существа полностью самостоятельны, вам лишь нужно грамотно выбрать алтари для их появления.'+"\n"+'Цель игры: уничтожить крепость соперника')




@bot.message_handler(commands=['begin'])
def beginmessage(message):
  if message.chat.id not in currentchat:
    currentchat.append(message.chat.id)
  
  
  
  
  
  
  
  
  
  
  


if __name__ == '__main__':
  bot.polling(none_stop=True)



