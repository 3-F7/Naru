import requests
import os
import sys
import time
import json
import base64
from discord_webhook import DiscordWebhook
from pystyle import Colors, Colorate, Center
import random
import string
from random import randint
from itertools import cycle
import threading

webhook = None

proxies = [
    "180.183.157.159:8080",
    "46.4.96.137:1080",
    "47.91.88.100:1080",
    "82.196.11.105:1080",
    "51.254.69.243:3128",
]

proxy_pool = cycle(proxies)

black = "\033[1;30m"
titletext = " [ NARU ] Developed By Yazzo, Follow me on GitHub [@3-F7]"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
invalidurl = f"{red}[NARU]{white} Invalid url!"

os.system(f'title {titletext}')

def mL():
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_purple, r"""                                      
        888b    888        d8888 8888888b.  888     888 
        8888b   888       d88888 888   Y88b 888     888 
        88888b  888      d88P888 888    888 888     888 
        888Y88b 888     d88P 888 888   d88P 888     888 
        888 Y88b888    d88P  888 8888888P"  888     888 
        888  Y88888   d88P   888 888 T88b   888     888 
        888   Y8888  d8888888888 888  T88b  Y88b. .d88P 
        888    Y888 d88P     888 888   T88b  "Y88888P"                                                                
     Follow me on GitHub for more updates @3-F7 :3""", 1)))

def Choice():
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_purple, """
    [1] Add Webhook
    [2] Send a message through Webhook
    [3] Get webhook Info
    [4] Delete Webhook                                                
    [5] Get Server info by Server Link
    [6] Generate Discord Tokens
    [7] Exit
""", 1)))

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')


def DELETE_WEBHOOK(URL):
    print(Colorate.Horizontal(Colors.purple_to_blue, '[NARU] Trying to delete Webhook...', 1))
    try:
        delete_request = requests.delete(URL)
        delete_request.raise_for_status()
        print(Colorate.Horizontal(Colors.purple_to_blue, '[NARU] Webhook deleted Successfully', 1))
        input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] Press enter to go back to the main menu...", 1))
        clear()
        mL()
        Choice()

    except requests.exceptions.HTTPError as errh:
        print(Colorate.Horizontal(Colors.red_to_purple, "[NARU] HTTP Error: " + str(errh), 1))
        input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] Press enter to go back to the main menu...", 1))
        clear()
        mL()
        Choice()

    except requests.exceptions.ConnectionError as errc:
        print(Colorate.Horizontal(Colors.red_to_purple, "[NARU] Error Connecting: " + str(errc), 1))
        input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] Press enter to go back to the main menu...", 1))
        clear()
        mL()
        Choice()

    except requests.exceptions.Timeout as errt:
        print(Colorate.Horizontal(Colors.red_to_purple, "[NARU] Timeout Error: " + str(errt), 1))
        input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] Press enter to go back to the main menu...", 1))
        clear()
        mL()
        Choice()

    except requests.exceptions.RequestException as err:
        print(Colorate.Horizontal(Colors.red_to_purple, "[NARU] Request Exception: " + str(err), 1))
        input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] Press enter to go back to the main menu...", 1))
        clear()
        mL()
        Choice()


def ADD_WEBHOOK(WHURL):
    if WHURL.startswith("https://discord.com/api/webhooks/"):
        WHRequest = requests.get(WHURL)
        if WHRequest.status_code == 200:
            print(Colorate.Horizontal(Colors.green_to_cyan, '[NARU] Webhook Found!', 1))
            return WHURL
    print(Colorate.Horizontal(Colors.red_to_yellow, '[NARU] Invalid Webhook URL!', 1))


def extract_and_print_server_info(link):
    code = link.replace("https://discord.gg/", "")
    
    api_endpoint = f"https://discord.com/api/invites/{code}"
    
    response = requests.get(api_endpoint)
    
    if response.status_code == 200:
        data = response.json()
        
        sorted_data = dict(sorted(data.items()))
        
        print(json.dumps(sorted_data, indent=4))
        input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] Press enter to go back to the main menu...", 1))
    else:
        print("Error:", response.status_code)


def WEBHOOK_INFO():
    info_request = requests.get(webhook)
    webhook_info = info_request.json()
    if info_request.status_code == 200:
        print("     [NARU] Webhook ID:", webhook_info['id'])
        print("     [NARU] Channel ID:", webhook_info['channel_id'])
        print("     [NARU] Server ID:", webhook_info['guild_id'])
        print("     [NARU] Webhook Type:", "Incoming" if webhook_info['type'] == 1 else "Outgoing")
        print("     [NARU] Webhook URL:", webhook_info['url'])
        print("     [NARU] Webhook Token:", webhook_info['token'])
        print("     [NARU] Webhook Creator User ID:", webhook_info['user']['id'])
        print("     [NARU] Webhook Creator Username:", webhook_info['user']['username'])
        print("     [NARU] Webhook Creator Avatar URL:", webhook_info['user']['avatar'])
        print("     [NARU] Webhook Creator Discriminator:", webhook_info['user']['discriminator'])
        print("     [NARU] Webhook Creator Public Flags:", webhook_info['user']['public_flags'])
        print("     [NARU] Webhook Creator Nitro (0 = no, 1 = yes):", webhook_info['user']['premium_type'])
        print("     [NARU] Webhook Creator Flags:", webhook_info['user']['flags'])
        print("     [NARU] Webhook Creator Banner:", webhook_info['user']['banner'])
        print("     [NARU] Webhook Creator Accent Color:", webhook_info['user']['accent_color'])
        print("     [NARU] Webhook Creator Global Name:", webhook_info['user']['global_name'])
        print("     [NARU] Webhook Creator Avatar Decoration Data:", webhook_info['user']['avatar_decoration_data'])
        print("     [NARU] Webhook Creator Banner Color:", webhook_info['user']['banner_color'])
        print("     [NARU] Token Type:", "Bot Token" if 'bot' in webhook_info else "Webhook Token")
        print("     [NARU] Webhook Username:", webhook_info['name'])
        print("     [NARU] Webhook Avatar URL:", webhook_info['avatar'])

        input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] Press enter to go back to the main menu...", 1))
        clear()
        mL()
        Choice()
    else:
        print("Failed to retrieve information about the webhook. Status code:", info_request.status_code)
        input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] Press enter to go back to the main menu...", 1))
        clear()
        mL()
        Choice()

def token_generator_tool(num_threads):
    N = input(Colorate.Horizontal(Colors.cyan_to_blue,"[NARU] How many tokens : ", 1))
    tokens = generate_tokens(N)
    send_requests(tokens, num_threads)

def generate_tokens(N):
    time.sleep(0.3)
    count = 0
    tokens = []
    while(int(count) < int(N)):
        base64_string = "=="
        while(base64_string.find("==") != -1):
            sample_string = str(randint(000000000000000000, 999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string + "." + random.choice(string.ascii_letters).upper() + ''.join(
                random.choice(string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
                random.choice(string.ascii_letters + string.digits) for _ in range(27))
            count += 1
            tokens.append(token)
    return tokens

def send_requests(tokens, num_threads):
    N = len(tokens)
    current_path = os.path.dirname(os.path.realpath(__file__))
    url = "https://discordapp.com/api/v6/users/@me/library"
    
    def token_check_thread(tokens, start_idx, end_idx):
        for idx in range(start_idx, end_idx):
            token = tokens[idx]
            proxy = next(proxy_pool)
            header = {
                "Content-Type": "application/json",
                "authorization": token
            }
            try:
                r = requests.get(url, headers=header)
                print(r.text)
                print(token)
                if r.status_code == 200:
                    print(u"\u001b[32;1m[NARU] Token Works!\u001b[0m")
                    with open(current_path + "/" + "workingtokens.txt", "a") as f:
                        f.write(token + "\n")
                elif "rate limited." in r.text:
                    print("[NARU] You are being rate limited.")
                else:
                    print(u"\u001b[31m[NARU] Invalid Token.\u001b[0m")
            except Exception as e:
                print("An error occurred:", e)
    
    chunk_size = N // num_threads

    threads = []
    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < num_threads - 1 else N
        thread = threading.Thread(target=token_check_thread, args=(tokens, start_idx, end_idx))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] Press enter to go back to the main menu...", 1))

def main():
    os.system(f'title {titletext}')
    while True:
        clear()
        mL()
        Choice()
        numchoice = (input(Colorate.Horizontal(Colors.purple_to_blue, "[NARU] What option do you want to use?: ", 1)))

        if numchoice == "1":
            clear()   
            WHURL = input(Colorate.Horizontal(Colors.purple_to_blue, '[NARU] Enter Webhook URL: ', 1))
            global webhook
            webhook = ADD_WEBHOOK(WHURL)
            print(Colorate.Horizontal(Colors.white_to_blue, '[NARU] Going back to the main menu...'))
            time.sleep(2.25)
            Choice()

        elif numchoice == "2":
            if webhook:
                while True:
                    wh = DiscordWebhook(url=webhook)
                    msg = input(Colorate.Horizontal(Colors.red_to_purple, '[NARU] Enter your message: '))
                    if not msg:
                        msg = input(Colorate.Horizontal(Colors.red_to_purple, '[NARU] Enter your message: '))
                    wh.content = msg

                    spam_or_not = input(Colorate.Horizontal(Colors.red_to_purple, '[NARU] Do you want to Spam? (y/n): '))
                    if spam_or_not == 'y'.lower():
                        ammount_of_spam = input(Colorate.Horizontal(Colors.red_to_purple, '[NARU] How many times do you wanna spam?: '))
                        if "2" <= ammount_of_spam <= "50":
                            for _ in range(ammount_of_spam):
                                spam_response = wh.execute()
                        else:
                            print(Colorate.Horizontal(Colors.red_to_purple, '[NARU] Invalid number of spam messages. Please enter a number between 2 and 50.'))
                    else:
                        response1 = wh.execute()
        
        elif numchoice == "3":
            if webhook:
                WEBHOOK_INFO()    

        elif numchoice == "4":
            if webhook:
                DELETE_WEBHOOK(webhook)

        if numchoice == "5":
            discord_link = input(Colorate.Horizontal(Colors.red_to_purple, '[NARU] Enter Discord Server Link: '))
            extract_and_print_server_info(discord_link)

        elif numchoice == "6":
            num_threads = int(input(Colorate.Horizontal(Colors.red_to_purple, '[NARU] How many threads do you want to use for token generation?: ')))
            token_generator_tool(num_threads)

        elif numchoice == "7":
            sys.exit()
        else:
            clear()
            mL()
            Choice()

if __name__ == '__main__':
    main()
