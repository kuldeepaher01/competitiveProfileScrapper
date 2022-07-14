import requests
from bs4 import BeautifulSoup
import re
import json
import csv

def codechef(user):
    if(user == "None"):
        return "None"
    else:
        URL = f'https://www.codechef.com/users/{user}'
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        soln = soup.find('h5', attrs={'class': None}).text
        soln = re.sub('[^0-9]', '', soln)
        return soln

def codeforces(user):
    if (user == "None"):
        return "None"
    else:
        URL = f'https://codeforces.com/profile/{user}'
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        soln = soup.find('div', attrs={'class': '_UserActivityFrame_counterValue'}).text
        soln = re.sub('[^0-9]', '', soln)
        return (soln)


def leetcode(user):
    if (user == "None"):
        return "None"
    else:
        URL = f'https://leetcode-stats-api.herokuapp.com/{user}/'
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'html5lib')
        soup = json.loads(soup.text)
        return soup['totalSolved']



usr = [0,0,0,0,0,0,0]
usrs = []
with open('12.csv') as file:
    content = file.readlines()
with open('users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Codeforces","Ques_Solved", "Leetcode","Ques_Solved", "Codechef","Ques_Solved"])
rows = content[1:]
header = content[:1]

n=0
for i in rows:
    users= (i.split(','))
    for user in users:
        if(user ==users[3]):
            usr[5] = users[3]
            usr[6] = (codechef(user))
        elif (user==users[2]):
            usr[3] = users[2]
            usr[4] = leetcode(user)
        elif (user==users[1]):
            usr[1] = users[1]
            usr[2] = codeforces(user)
        usr[0] = users[0]
    # for us in usr:
    #     print(us)
    usrs.append(usr)
    usr = [0, 0, 0,0,0,0,0]
    n+=1
with open('users.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    print("Writing...", end="")
    writer.writerows(usrs)
    print("...")

