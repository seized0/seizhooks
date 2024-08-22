import requests
import colorama
from colorama import *
import json

red = Fore.RED
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
lmangenta = Fore.LIGHTMAGENTA_EX
blue = Fore.BLUE
green = Fore.GREEN
cyan = Fore.CYAN

###################################################

            # Made with ❤️

            # By uhq.s

            # Seizcord v1

            # https://discord.gg/wyUuYr9DEN

###################################################

class Hook():
    def __init__(self, webhook=""):
        self.webhook = webhook


    # def Delete(self):
    #     url = 'https://discord.com/api/v9/channels/1269018586635047089/webhooks'

    #     data = {                                                                              
    #         "url":self.webhook                                                                       WHY I DID THIS ?????????????????????????????????????
    #         }
    #                                                                                                     WHY I DID THIS ?????????????????????????????????????
    #     req = requests.delete(url=self.webhook,headers=data)

    #     if req.status_code == 200 or 204:
    #         print(green +  'WEBHOOK DELETED SUCCESFULY')

    #     else:
    #         print(red + f'ERROR : {req.status_code}')

    def Delete(self):

        req = requests.delete(self.webhook)

        if req.status_code == 200 or 204:
            print(green + 'WEBHOOK DELETED SUCCESSFULY')
        
        else:
            print(red + f'ERROR {req.status_code} : {req.text}')

    
    def SendMessage(self,message,name,avatar):

        headers = {'Content-Type': 'application/json'}

        data = {
            'content':message,
            'username':name,
            'avatar_url': avatar
        }
        req = requests.post(url=self.webhook, json=data,headers=headers)       


        if req.status_code ==  200 or 204:
            print(green + f'SUCCESSFULY SENT MESSAGE : {message}')

        else:
            print(red + f'ERROR {req.status_code} : {req.text}')





    
###################################################

            # Made with ❤️

            # By uhq.s

            # Seizcord v1

            # https://discord.gg/wyUuYr9DEN

###################################################