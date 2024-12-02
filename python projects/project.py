import xlrd
import os
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from pynput import *
from pynput import mouse,keyboard
import time
# import materials


username = os.getlogin()# get username
def log(x):
    fn = 'C:/Users/' + str(username) + '/Contacts/file.log'# log file path
    f = open(fn , 'at+')# open log file
    f.write(str(x))# write logs in log file
    f.close()# save the logs    

m = mouse.Controller()
def click_(x, y):
    m.position=(x, y)# mouse position
    m.click(mouse.Button.left,1)# left click with mouse

key = keyboard.Controller()
def press_(k):
    key.press(str(k))# press key
    key.release(str(k))# release key

def sl(t):
    time.sleep(t)

cp = 'C:/Users/' + str(username) + '/onedrive/desktop/cache/'# cache path

loc = ('ilia.xls')# excel file path

wb = xlrd.open_workbook(loc)# open excel

sheet = wb.sheet_by_index(0)# sheet 1

x = 'C:/Users/' + str(username) + '/OneDrive/Desktop/cache/'

msg = input('plz enter your message: ')

print('--------------------------------------------------------------------------')

while True:

    num = input('press [1] for add a new number\npress [2] to chose phone number\npress [3] to run\npress [4] to retype msg\npress [5] to exit\nplz inter: ')# menu

    if num == '1':
        print('--------------------------------------------------------------------------')      
        nn = input('your new number name: ')# number name
        os.system('cd ' + str(x))
    
        if str(nn) not in os.listdir(x):
            os.system('mkdir ' + str(nn))

        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=' + str(x) + str(nn))
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get('https://web.whatsapp.com')
        sl(10)
        driver.close()

    if num == '2':
        print('--------------------------------------------------------------------------')
        dl = os.listdir(x)# dirs in path
    
        for i in dl:
            print(i)
        print('--------------------------------------------------------------------------')
        cn = input('plz copy your number and pate it here: ')

        print('--------------------------------------------------------------------------')

        cp = 'C:/Users/' + str(username) + '/onedrive/desktop/cache/' + str(cn)

    if num == '3':
        print('--------------------------------------------------------------------------')
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=' + str(cp))
        driver = webdriver.Chrome(options=options)# open chrome
        driver.maximize_window()# maximize window
    
        for i in range(2,6):
            enc = sheet.cell_value(i ,2)# encription number
            code = sheet.cell_value(i ,1)# formula value
            dec = int(enc) / int(code)# create decription number
            driver.get('https://web.whatsapp.com/send?phone=' + str(int(dec)) + '&text=' + str(msg) + '&app_absent=0') # url to send message
            if i == 2:
                sl(8)
            sl(7)
            # driver.get('wa.me' + str(int(dec)) + '?text=this is a test message')
            # driver.find_element_by_xpath('//*[@id="action-button"]').click()
            # driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div').click()# attach image
            sl(0.1)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button').click()# attach image
            sl(1.4)
            # if i == 2:
            #    click_(100, 150)# go to desktop
            # else:
            #   click_(100,200)# go to desktop
            # sl(0.75)
            click_(300,55)
            path = os.getcwd()
        
            for i in str(path):
                press_(i)# image path
            sl(0.4)
        
            click_(400,55)

            click_(300,420)# search box
            sl(0.4)
        
            for i in 'IMG':
                press_(i)# image name
            sl(0.15)
        
            click_(450,450)# open
            sl(1.2)
            driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div').click()# send
            sl(5)
            log(str(i) + ' sended; number is: ' + str(enc))

    if num == '4':
        msg = input('plz retype your message: ')
    
    if num == '5':
        break