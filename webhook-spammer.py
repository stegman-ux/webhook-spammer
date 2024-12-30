import requests
import colorama
from colorama import Fore
import clear
import time
webhook = input(Fore.YELLOW+"[<]entrée l'url du webhook : ")
message = input(Fore.YELLOW+"[<]entrée le message a envoyer : ")
message_to_send = {
    "content":f"{message}"
}
webhook_url = f"{webhook}"

while True:
 requests.post(webhook_url,json=message_to_send)
 time.sleep(0.3)
 print(f"sended message '{message}'")
clear.clear()
input(Fore.YELLOW+f"[<]le message '{message}' à bien etais envoyer au webhook...")

# script nuL  mais j'mets quand meme des crédits 
# créator : intrable
# serveur discord : .gg/freeforreal
