import ftplib
import re
from ftplib import FTP
import telebot
from dateutil import parser
from datetime import datetime
from telebot import apihelper

apihelper.proxy = { 'https':'https://anthill:a09NT21hil23l@5.253.63.139:54322'}
TOKEN = '603890438:AAE5T7edt2I3JCZ_SfoXC_YnERgSZrkExE0'
bot = telebot.TeleBot(TOKEN)

'''Подключаемся к FTP'''
ftp: FTP = ftplib.FTP('217.25.239.57', 'backup_office_1c', 'J#ei8V')
'''Переходим в дерикторию'''
lines = []
ftp.dir("/Office_ANTHILL", lines.append)

for line in lines:
    tokens = line.split(maxsplit = 9)
    name = tokens[8]
    time_str = tokens[5] + " " + tokens[6] + " " + tokens[7]
    time = parser.parse(time_str)
    txt = open('txt.txt', 'w')
    txt.write(name + ' - ' + str(time))
    txt.close()
    print(name + ' - ' + str(time))

'''Текущая дата'''
teckdata = datetime.today().strftime('%Y-%m-%d')
print(teckdata)

dataBackUP = open('txt.txt', 'r')
line = dataBackUP.readlines()
match = re.search('\d{4}-\d{2}-\d{2}', str(line))
'''Дата последнего бэкапа'''
databack = datetime.strptime(match.group(), '%Y-%m-%d').date()
print(databack)
txt.close()

'''txt1 = open('txt.txt', 'w')
txt1.write(str(teckdata)+'\n'+str(databack))
txt1.close()'''
'''Проверка текущей даты и даты последенего бэкапа'''
a=str(teckdata)
b=str(databack)
'''Отправка информации об ошибке в чат Telegram'''
if a==b:
    bot.send_message(-378792840,"Дата последенего бэкапа---{D}".format(D=databack))
    print("Верно")
else:
    bot.send_message(-378792840,"ОШИБКА:Дата последнего бэкапа не совпадает с текущей датой:{D}".format(D=databack))
    #print("Бэкап не делался")
bot.polling()
