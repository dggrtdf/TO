import requests
import os
import threading
import time
import sys
from threading import Thread as HSO

try:
    from instagramtolle import GMAIL, instagram
except ImportError:
    os.system("pip install instagramtolle==0.3")

G = '\033[1;32m'
R = '\033[1;31m'
W = '\033[1;37m'
B = '\033[2;36m'
Bl = '\033[1;34m'

def jalan(text):
    for char in text + "\n":
        print(char, end='', flush=True)
        time.sleep(0.03)


jalan('\033[3;41m﴾ TL  : @AAj0A   |𝐉𝐀𝟑𝐅𝐑 |IN : @u.b2b')
jalan('\033[0;32m──────────────────────────────      ')
print('''\033[1;32m  
     
░░░░░██╗░█████╗░██████╗░███████╗██████╗░
░░░░░██║██╔══██╗╚════██╗██╔════╝██╔══██╗
░░░░░██║███████║░█████╔╝█████╗░░██████╔╝
██╗░░██║██╔══██║░╚═══██╗██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║██████╔╝██║░░░░░██║░░██║
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝ 



   ''')

jalan('\033[1;32m──────────────────────────────      ')
print("\033[92m﴾ \033[95m 𝗗𝗘𝗩  : \033[91m TL  : @AAj0A   ﴿ \033[94m | \033[93m ﴾ 𝐉𝐀𝟑𝐅𝐑 ﴿ \033[92m | \033[96m ﴾IN | @u.b2b  ﴿ ")
jalan('\033[1;32m──────────────────────────────      ')

tok = input(f' {B}Enter Token : {W}')
id = input(f' {B}Enter ID : {W}')

ge, be, gi, bi = 0, 0, 0, 0
def info(email):
    global id, tok
    try:
        user = email.split("@")[0]
        response = instagram.GetUserInfo(user)

        if response.status_code == 200:
            data = response.json()['result'][0]['user']
            fols = data.get('follower_count', '0')
            folg = data.get('following_count', '0')
            user_id = data.get('id', '0')
            full_name = data.get('full_name', '0')
            res = GMAIL.CheckEmail(email).get("data").get("status")

            result_text = f'''
𝓝𝓮𝔀 𝓘𝓷𝓼𝓽𝓪𝓰𝓻𝓪𝓶 𝓗𝓲𝓽 
✦•━━━━━━━━━━━━━•✦
𝓤𝓼𝓮𝓻𝓷𝓪𝓶𝓮 : {user}
𝓔𝓶𝓪𝓲𝓵 : {email}
𝓡𝓔𝓢𝓣 : {res}
𝓕𝓸𝓵𝓵𝓸𝔀𝓮𝓻𝓼: {fols}
𝓕𝓸𝓵𝓵𝓸𝔀𝓲𝓷𝓰 : {folg}
𝓝𝓪𝓶𝓮 : {full_name}
𝓤𝓡𝓛 ==> https://www.instagram.com/{user}
𝐁𝐘 - @AAj0A
</>
✦•━━━━━━━━━━━━━•✦
  ♡   ‌ ‌      ❍ㅤ         ⎙ㅤ    ‌     ⌲ 
 ˡᶦᵏᵉ ‌   ᶜᵒᵐᵐᵉⁿᵗ       ˢᵃᵛᵉ         ˢʰᵃʳ
            '''
            requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={result_text}")
            with open('hits.txt', 'a') as file:
                file.write(f'{result_text}\n')

        else:
            raise Exception("Failed to fetch user info")

    except Exception as e:
        error_text = f'''
✦•━━━━━━━━━━━━━•✦
𝓤𝓼𝓮𝓻𝓷𝓪𝓶𝓮  : {user}
𝓔𝓶𝓪𝓲𝓵 : {email}
𝓤𝓡𝓛 ==> https://www.instagram.com/{user}
𝐁𝐘 - @AAj0A
</>
✦•━━━━━━━━━━━━━•✦
  ♡   ‌ ‌      ❍ㅤ         ⎙ㅤ    ‌     ⌲ 
 ˡᶦᵏᵉ ‌   ᶜᵒᵐᵐᵉⁿᵗ       ˢᵃᵛᵉ         ˢʰᵃʳ
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={error_text}")
        with open('hits.txt', 'a') as file:
            file.write(f'{error_text}\n')

def ch(email):
    global ge, be, gi, bi
    try:
        check_status = instagram.CheckEmail(email).get("data").get("status")
        if check_status:
            gi += 1
            gmail_status = GMAIL.CheckEmail(email).get("data").get("status")
            if gmail_status:
                ge += 1
                info(email)
            else:
                be += 1
        else:
            bi += 1


        sys.stdout.write(
            f'\r{G}Hits : {W}{ge} {R}| Bad : {W}{bi} {B}| Bad Email : {W}{be} {Bl}| Good Email : {W}{gi}'
        ), sys.stdout.flush()

    except:
        print("ON VPN...")

def h():
    while True:
        try:
            generated_user = instagram.generateUsername2013()
            user = generated_user["data"]["username"]
            if user and "None" not in user:
                email = f"{user}@gmail.com"
                ch(email)
        except:
            pass

for i in range(50):
    HSO(target=h).start()