import bottle
import requests
import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import string

TOKEN = os.environ.get('TOKEN')

def soupify(url):
    my_url=url
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup=soup(page_html,"html.parser")
    return page_soup
def sendMessage(chat_id, text):
    r = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",data={"chat_id": chat_id, "text": text})
    return r.status_code == 200
def make_reply(msg):
    reply = None
    if(msg=="musicn"):
        page_soup=soupify("https://www.npr.org/sections/new-music/")
        ok=page_soup.findAll("h2",class_="title")
        li=[]
        li.append("MUSIC NEWS FROM https://www.npr.org/sections/new-music/")
        for i in ok:
            li.append(i.getText().strip())
        reply=str(li)[1:-1]
    if(msg=="ttrends"):
        my_url="https://trends24.in/india/"
        page_soup=soupify(my_url)
        ok=page_soup.findAll("div",class_="trend-card")
        reply=[]
        for i in range(0,1):
            reply.append(ok[i].text.strip())
        reply= str(reply)[1:-1]
        for char in reply:
            if char in "#":
                reply= reply.replace(char,'\n')
    if(msg=="!starwars"):
        my_url="https://www.starwars.com/news/"
        page_soup=soupify(my_url)
        ok=page_soup.find_all("h2",{"class":"cb-title"})
        reply=[]
        reply.append("LATEST STAR WARS NEWS from https://www.starwars.com/news/")
        for i in range(1,8):
            reply.append(ok[i].text.strip())
        reply=str(reply)[1:-1]
        for char in reply:
            if char in ",":
                reply= reply.replace(char,'\n')
    if(msg=="!talk-dirty"):
        reply="WELL I JUST CAUGHT U DIDN'T I?"
    if(msg=="heybot"):
        reply= "sup type in any !anime-news,!porn,!starwars..i can even !talk-dirty...MORE ON THE WAY"
    if(msg=="!anime-news"):
        my_url="https://www.animenewsnetwork.com/news/"
        page_soup=soupify(my_url)
        ok=page_soup.find_all("h3")
        reply=[]
        reply.append("...LATEST ANIME NEWS from https://www.animenewsnetwork.com/news ..")
        for i in range(1,8):
            reply.append(ok[i].text.strip())
        reply= str(reply)[1:-1]
        for char in reply:
            if char in ",":
                reply= reply.replace(char,'\n')
    return reply

def handle_update():

    update = bottle.request.json
    message   = update['message']
    chat_id = message['chat']['id']
    text    = message['text']
    print(update)

    sendMessage(chat_id, make_reply(text))

    return ""


if __name__ == "__main__":
    app = bottle.Bottle()
    app.route("/update", "POST", handle_update)
    app.run(host="0.0.0.0",  port = int(os.environ.get("PORT", 5000)), debug=True)