import telebot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from telebot import apihelper
import os
import sys
import time
DRIVER = "chromedriver.exe"
driver = webdriver.Chrome (DRIVER)
driver.get("http://192.168.0.66:8080/job/uff_jenkins/lastSuccessfulBuild/allure/")
time.sleep(1)
login = driver.find_element_by_id("j_username")
login.send_keys("Anthill")
pswd = driver.find_element_by_name("j_password")
pswd.send_keys("Vehfdtq")
ent = driver.find_element_by_id ("remember_me")
ent.send_keys(Keys.ENTER)
time.sleep(3)
screenshot = driver.save_screenshot("my_screenshot.png")
driver.quit()
apihelper.proxy = { 'https':'https://anthill:a09NT21hil23l@5.253.63.139:54322'}
TOKEN = '1036759397:AAEne-CNrRv9Td82tT1zSKqrizbILOrq1Wo'
bot = telebot.TeleBot(TOKEN)
caption = "http://192.168.0.66:8080/job/uff_jenkins/lastSuccessfulBuild/allure/"
photo = open('my_screenshot.png', 'rb')
bot.send_photo(-292886159, photo,caption)
bot.polling()

