from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
import sys
from pip._vendor.colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait


FROM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))

class MainApp(QMainWindow , FROM_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Ui()
        self.Handel_Button()
        self.Handel_Button2()

        





    def Handel_Ui(self):
        self.setWindowTitle('Checker Twitter')
        self.setFixedSize(225,432)

    def Handel_Button(self):
        #self.QPushButton.clicked.connect(self.checkk)
        self.pushButton_3.clicked.connect(self.checkk)
    def Handel_Button2(self):
        self.pushButton_2.clicked.connect(self.exit)







    def checkk(self):
        

        delay = 50
        opts = Options()
        option = webdriver.ChromeOptions()
        # options.add_argument("headless")
        opts.add_argument("--incognito")
        #opts.add_argument("--headless")
        opts.add_argument('--disable-gpu')
        opts.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=opts)

        time.sleep(3)
        driver.get("https://mobile.twitter.com/i/flow/signup")
        driver.set_page_load_timeout(30)
        # driver.maximize_window()
        time.sleep(5)
        d = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-18t94o4')))
        # d = driver.find_element_by_css_selector('.css-18t94o4')
        d.click()

        with open('emails.txt', 'r') as f:

            lines = f.readlines()
            for line in lines:
                mail = line
                time.sleep(1)

                try:

                    driver.find_element_by_name('email').clear()
                except:
                    pass
                driver.find_element_by_name('email').send_keys(mail)
                time.sleep(2)
                content = driver.find_element_by_css_selector('.css-1dbjc4n')
                message = "Email has already been taken."
                message1 = "تمّ استخدام هذا البريد الإلكتروني مسبقًا."
                message2 = "Please enter a valid email."
                message22 = "يرجى إدخال بريد إلكتروني صالح."
                

                if message in content.text:
                    self.listWidget.addItem(mail) 
                    y = open('Available.txt', 'a')
                    y.write(mail)
                    y.close()
                elif message1 in content.text:
                    self.listWidget.addItem(mail)
                    y = open('Available.txt', 'a')
                    y.write(mail)
                    y.close()

                    driver.find_element_by_name('email').send_keys(Keys.CONTROL + "a")
                    driver.find_element_by_name('email').send_keys(Keys.DELETE)
                elif message2 in content.text:
                    self.listWidget.addItem(mail)
                    s = open('Not Available.txt', 'a')
                    self.listWidget.addItem(mail)
                    s.close()
                    driver.find_element_by_name('email').send_keys(Keys.CONTROL + "a")
                    driver.find_element_by_name('email').send_keys(Keys.DELETE)
                elif message22 in content.text:
                    self.listWidget.addItem(mail)
                    s = open('Not Available.txt', 'a')
                    s.write(mail)
                    s.close()

                    driver.find_element_by_name('email').send_keys(Keys.CONTROL + "a")
                    driver.find_element_by_name('email').send_keys(Keys.DELETE)

                else:
                    self.listWidget.addItem(mail)
                    s = open('Not Available.txt', 'a')
                    s.write(mail)
                    s.close()
                    driver.find_element_by_name('email').send_keys(Keys.CONTROL + "a")
                    driver.find_element_by_name('email').send_keys(Keys.DELETE)

    
    def exit(self):
        app.exec_()





def main():
    app = QApplication(sys.argv)
   # listWidget = QListWidget()
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
