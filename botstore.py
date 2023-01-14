import sys, os, time, getpass
from sys import platform
try:
    import tkinter as tk
except Exception:
    pass

if platform == "linux" or platform == "linux2":
    #!/usr/bin/env python3
    #/usr/bin/python3
    print("Your platform is linux")
    os.system("clear")
else:
    pass

os.system('clear||cls')

# -*- coding: utf-8 -*-

if not sys.version_info.major==3 and sys.version_info.minor >= 6:
    print("you need to upgrade your python version to up > 3.6") # Attention
    if platform == "linux" or platform == "linux2":
        os.system("xdg-open https://python.org/download") # If you use python < 3.6>
    elif platform =="win32":
        os.startfile("https://python.org/download")
    else:
        sys.exit(1)
    sys.exit(1) # exit if you not use python > 3.6

__author__ = "Xnuvers007 / Indra Dwi A"
__version__ = "1.3.2"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2023, Xnuvers007"
__credits__ = ["Xnuvers007", "Botostore.com"]
__python__ = "3.11.0"

# tanya = str(input("Do you use termux ? (y/n) "))
# if tanya == "y" or tanya == "Y":
#     os.system("pip install wheel")
#     os.system("pkg install libjpeg-turbo")
#     os.system('''LDFLAGS="-L/system/lib/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install Pillow
# ''')
# elif tanya == "n" or tanya == "N":
#     pass

import requests
from bs4 import BeautifulSoup

try:
    from PIL import Image, ImageTk
    from io import BytesIO
except Exception as e:
    pass

# try:
#     from PIL import Image, ImageTk
#     from io import BytesIO
#     import requests
#     from bs4 import BeautifulSoup
#     # from tqdm import tqdm
# except Exception as e:
#     print(e)
    # if platform == "linux" or platform == "linux2":
    #     ask = str(input("Do you want to install requests, beautifulsoup4, pillow ? (y/n) "))
    #     if ask == "y" or ask == "Y":
    #         user = getpass.getuser()
    #         username = input("apakah kamu ingin menginstallnya root atau {} [1, 2]) : ".format(user))
    #         if username == "root" or username == "1":
    #             os.system("sudo pip3 install requests beautifulsoup4 pillow") # tqdm
    #         elif username == user or username == "2":
    #             os.system("pip3 install requests beautifulsoup4 pillow") # tqdm
    #         else:
    #             print("You must write root or {} ".format(user))
    #     elif ask == "n" or ask == "N":
    #         sys.exit(1)
    #     else:
    #         print("You must write y or n")

    # elif platform == "win32":
    #     ask = str(input("Do you want to install requests, beautifulsoup4, pillow ? (y/n) ")) # tqdm
    #     if ask == "y" or ask == "Y":
    #         os.system("pip install requests beautifulsoup4 pillow") # tqdm
    #     elif ask == "n" or ask == "N":
    #         sys.exit(1)
    #     else:
    #         print("You must write y or n")

    # elif platform == "darwin":
    #     ask = str(input("Do you want to install requests, beautifulsoup4, pillow ? (y/n) "))
    #     if ask == "y" or ask == "Y":
    #         os.system("pip3 install requests beautifulsoup4 pillow") # tqdm
    #     elif ask == "n" or ask == "N":
    #         sys.exit(1)
    #     else:
    #         print("You must write y or n")

    # else:
    #     print("Your platform is not supported")
    #     sys.exit(1)


# for i in tqdm(range(100), desc='Loading', total=100, bar_format='{l_bar}{bar}|', ncols=100, ascii=True):
#     time.sleep(0.1)


url = 'https://botostore.com'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safar537.36 Edg/108.0.1462.54'})

print("\033[92m Tunggu Sebentar Loading Page 5 Detik \033[0m")
time.sleep(5)
os.system('clear||cls')

soup = BeautifulSoup(r.text, 'html.parser')

print("\n")
print("=====================================")
print("\033[1mTitle: Bot Store Telegram\n\033[0m")
print("\033[1m",soup.title.text.title(),"\033[0m")


for meta in soup.find_all('meta'):
    if meta.get('name') == 'description':
        print("Description: " + meta.get('content').title())
print("=====================================")

# get total bot added checked and online
total_bot = soup.find('div', class_='text-center').find('a').text
print("Total bot added: " + total_bot)
print("Do you Want to search bots ? or see all bots ?")
print("1. Search")
print("2. See all")
print("3. Donation")
print("4. Update")
print("5. Contact Me")
print("6. Exit")
print("=====================================")

# Do again if user write incorrect option
while True:
    try:
        daftar = int(input("Choose: "))
        break
    except (ValueError, TypeError, NameError, KeyboardInterrupt):
        print("You must write a number!")
    
if daftar == 1:
    print("=====================================")
    print("you choose search")
    print("=====================================")
    search = input("Search: ")
    combine = "https://botostore.com/search/?q=" + search
    r = requests.get(combine, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safar537.36 Edg/108.0.1462.54'})
    soup = BeautifulSoup(r.text, 'html.parser')
    for lists in soup.find_all('div', class_='tpl-block-list tpl-component-netcat-module-search-result tpl-template-new-api-search'):
        print("\033[1mSearch Result : "+ lists.find('strong').text,"\033[0m\n")
        for content in lists.find_all('div', class_='row justify-content-center pt-5 mb-3 no-gutters'):
            for link in content.find('div', class_='col-sm-12 col-md-8 col-lg-6').find_all('a', class_='d-block pb-3 mb-3 text-body element search-element'):
                print("Bot Name: " + link.find('h4', class_="e-title").text)
                print("Bot Description: " + link.find('div', class_='e-description').text)
                element = link.find('span', title='Bot is active and replies instantly')
                if element:
                    print("Bot Status: " + element.text)
                else:
                    print("Bot Status: Offline")
                    
                botlink2 = "https://botostore.com" + link.get('href')
                print("Bot Link: " + botlink2 + "?do=open_card")
                print("=====================================")
                    
                # print(link.get('href'))
    print("\n")
    asking = str(input("do you want to open bot link ? (y/n) "))
    if asking == "y" or asking == "Y":
        inputlink = input("Write bot link: ")
        if platform == "linux" or platform == "linux2":
            os.system('clear||cls')
            os.system("xdg-open " + inputlink)
        elif platform == "win32":
            os.system('clear||cls')
            os.startfile(inputlink)
        elif platform == "darwin":
            os.system('clear||cls')
            os.system("open " + inputlink)
        else:
            print("Your platform is not supported")
            time.sleep(3)
            os.system('clear||cls')
            sys.exit(1)

    elif asking == "n":
        os.system('clear||cls')
        sys.exit(1)
                
    else:
        os.system('clear||cls')
        time.sleep(3)
        print("You must write y or n")
        sys.exit(1)

    print("=====================================")
    # reverse count from 5 to 1
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    os.system('clear||cls')
    sys.exit(1)
    
    
elif daftar == 2:
    print("You choose see all")
    print("=====================================")
    print("Here is the list of bots: ")
    print("\n")
    for lists in soup.find_all('div', class_='row justify-content-center no-gutters'):
        for content in lists.find_all('div', class_='col-sm-6 col-lg-3'):
            print(content.find('h4').text)
            for divstyle in content.find_all('div', style='height:120px;margin:1.5rem 1.5rem 1rem;overflow:hidden'):
                print(divstyle.find('div', class_="e-description").text)
            print(content.find('div', title='Bot is active and replies instantly').text, "Bot Status is ", content.find('div', title='Bot is active and replies instantly').find('span', class_="text-primary").text)
            botlink = content.find('a', class_="mb-3 btn btn-sm btn-outline-primary").get('href')
            gabung = url + botlink
            print("Bot link: " + gabung)

    print("\n")
    asking = str(input("do you want to open bot link ? (y/n) "))
    if asking == "y" or asking == "Y":
        inputlink = input("Write bot link: ")
        if platform == "linux" or platform == "linux2":
            os.system('clear||cls')
            os.system("xdg-open " + inputlink)
        elif platform == "win32":
            os.system('clear||cls')
            os.startfile(inputlink)
        elif platform == "darwin":
            os.system('clear||cls')
            os.system("open " + inputlink)
        else:
            print("Your platform is not supported")
            time.sleep(3)
            os.system('clear||cls')
            sys.exit(1)

    elif asking == "n":
        os.system('clear||cls')
        sys.exit(1)
                
    else:
        print("You must write y or n")
        time.sleep(3)
        os.system('clear||cls')
        sys.exit(1)

    print("=====================================")
    # reverse count from 5 to 1
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    os.system('clear||cls')
    sys.exit(1)

elif daftar == 3:
    print("You choose donation")
    print("=====================================")
    print("Thanks for your donation")
    print("=====================================")
    # for i in range(0, 3):
    #     i += 1
    #     print(i)
    #     time.sleep(1)
    print('''
    1. Dana (Not Supported termux) https://t.me/xnuvers07
    2. Saweria
    3. Seabank
    ''')
    pilih = int(input("Choose your payment method: "))
    if pilih == 1:
        root = tk.Tk()
        root.title("Donation")
        image_url = "https://ndraeee25.000webhostapp.com/dana/DanaXnuvers007.jpeg"
        response = requests.get(image_url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        panel = tk.Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
        root.mainloop()
    elif pilih == 2:
        if platform == "linux" or platform == "linux2":
            os.system('clear||cls')
            os.system("xdg-open https://saweria.co/xnuvers007")
        elif platform == "win32":
            os.system('clear||cls')
            os.startfile("https://saweria.co/xnuvers007")
        elif platform == "darwin":
            os.system('clear||cls')
            os.system("open https://saweria.co/xnuvers007")
        else:
            print("Your platform is not supported")
            time.sleep(3)
            os.system('clear||cls')
            sys.exit(1)
    elif pilih == 3:
        print("=====================================")
        print("Account Number: 901276459950")
        print("Account Name: Indra Dwi A")
        print("=====================================")
    else:
        sys.exit(1)

elif daftar == 4:
    print("You choose update")
    print("=====================================")
    os.system('clear||cls')
    print("=====================================")
    print("Checking for update")
    os.system("git pull")
    print("=====================================")
    print("Update complete")
    print("=====================================")
    # reverse count from 5 to 1
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    os.system('clear||cls')
    sys.exit(1)

elif daftar == 5:
    print("You choose contact me")
    print("=====================================")
    print("Contact me on: ")
    print("=====================================")
    print("Channel = https://t.me/xnuvers07")
    print("do you want to open it ? (y/n)")
    op = str(input("y/n: "))
    if op == "y" or op == "Y":
        if platform == "linux" or platform == "linux2":
            os.system('clear||cls')
            os.system("xdg-open https://t.me/xnuvers07")
        elif platform == "win32":
            os.system('clear||cls')
            os.startfile("https://t.me/xnuvers07")
        elif platform == "darwin":
            os.system('clear||cls')
            os.system("open https://t.me/xnuvers07")
        else:
            print("Your platform is not supported")
            time.sleep(3)
            os.system('clear||cls')
            sys.exit(1)
    elif op == "n" or op == "N":
        os.system('clear||cls')
        sys.exit(1)
    else:
        os.system('clear||cls')
        sys.exit(1)

elif daftar == 6:
    print("You choose exit")
    print("=====================================")
    print("Thanks for using this program")
    print("=====================================")
    # reverse count from 5 to 1
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    os.system('clear||cls')
    sys.exit(1)

else:
    print("=====================================")
    print("You must write a number 1 or 2")
    print("=====================================")
    # reverse count from 5 to 1
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    os.system('clear||cls')
    sys.exit(1)

