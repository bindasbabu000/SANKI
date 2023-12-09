import requests
import logging
from time import sleep
API_VERSION = 'v15.0'

HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

# ANSI escape codes for console colors
RED_COLOR = "\033[91m"
YELLOW_COLOR = "\033[93m"
GREEN_COLOR = "\033[92m"
BLACK_COLOR = "\033[30m"
BLUE_COLOR = "\033[34m"
PINK_COLOR = "\033[95m"
GOLDEN_COLOR = "\033[38;5;220m"  # Added golden color
MAROON_COLOR = "\033[38;5;88m"  # Added maroon color
SILVER_COLOR = "\033[38;5;7m"   # Added silver color
BOLD_TEXT = "\033[1m"  # Added bold text escape code
RESET_COLOR = "\033[0m"

logo = """
 .d888888  888888ba   .d888888  888888ba  888888ba     8888ba.88ba   88888888b dP     dP   888888ba   .d888888     
d8'    88  88    `8b d8'    88  88    `8b 88    `8b    88  `8b  `8b  88        88     88   88    `8b d8'    88     
88aaaaa88a 88     88 88aaaaa88a 88     88 88     88    88   88   88 a88aaaa    88aaaaa88a a88aaaa8P' 88aaaaa88a    
88     88  88     88 88     88  88     88 88    .8P    88   88   88  88        88     88   88   `8b. 88     88     
88     88  88     88 88     88  88     88 88    .8P    88   88   88  88        88     88   88   `8b. 88     88     
88     88  88     88 88     88  88     88 88    .8P    88   88   88  88        88     88   88   `8b. 88     88     
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
"""

def print_red(text):
    print(RED_COLOR + text + RESET_COLOR)

def print_yellow(text):
    print(YELLOW_COLOR + text + RESET_COLOR)

def print_green(text):
    print(GREEN_COLOR + text + RESET_COLOR)

def print_black(text):
    print(BLACK_COLOR + text + RESET_COLOR)

def print_blue(text):
    print(BLUE_COLOR + text + RESET_COLOR)

def print_pink(text):
    print(PINK_COLOR + text + RESET_COLOR)

def print_golden(text):  # Added golden color
    print(GOLDEN_COLOR + text + RESET_COLOR)

def print_maroon(text):  # Added maroon color
    print(MAROON_COLOR + text + RESET_COLOR)

def print_silver(text):  # Added silver color
    print(SILVER_COLOR + text + RESET_COLOR)

def print_bold(text):  # Added bold text
    print(BOLD_TEXT + text + RESET_COLOR)

def print_info():
    info_text = f"""
    {BOLD_TEXT}
    {RED_COLOR}
    ...[✓] AUTHOR: ANAND MEHRA                 
    ...[✓] TOOL      : IB CONVO
    ...[✓] STATUS :  FREE                                      
    ...[✓] FACEBOOK: ANAND MEHRA 
    ...[✓] WHAT'S APP : +917643890954
     ()⁠☞CONTACT FOR PRIVATE 
      SERVER AND TOOL <3
    """
    print(info_text)

def ask_for_approval():
    user_approval_key = input(f"{RED_COLOR}Enter the approval key: {RESET_COLOR}")
    return user_approval_key == '3dfdb294f71b3c974bc4d2557c792a4f23943076eafb58ecdb3d59b0abfd3d57'  # Replace with your actual secret key

def generate_whatsapp_link(phone_number):
    return f"https://wa.me/{phone_number}"

def initialize_tokens():
    num_tokens = int(input(f"{YELLOW_COLOR}Enter the number of access tokens: {RESET_COLOR}"))
    return [input(f"{BLUE_COLOR}Enter access token {i + 1}: {RESET_COLOR}") for i in range(num_tokens)]

def send_message(api_url, access_token, thread_id, message):
    response = requests.post(api_url, data={'access_token': access_token, 'message': message}, headers=HEADERS)
    return response

def get_user_name(access_token):
    response = requests.get(f'https://graph.facebook.com/{API_VERSION}/me', params={'access_token': access_token})
    user_data = response.json()
    return user_data.get('name', 'Unknown User')

def main():
    try:
        logging.basicConfig(level=logging.INFO)

        print_info()

        while True:
            if not ask_for_approval():
                print_red("Wrong approval key. Redirecting to WhatsApp of the script owner.")
                owner_whatsapp_number = '+917643890954'  # Replace with the owner's WhatsApp phone number
                whatsapp_link = generate_whatsapp_link(owner_whatsapp_number)
                print_red(f"Contact the script owner on WhatsApp: {whatsapp_link}")
                continue

            break

        owner_whatsapp_number = '+917643890954'  # Replace with the owner's WhatsApp phone number
        whatsapp_link = generate_whatsapp_link(owner_whatsapp_number)
        print_red(f"Please contact the script owner on WhatsApp: {whatsapp_link}")

        access_tokens = initialize_tokens()
        num_threads = int(input(f"{GREEN_COLOR}Enter the number of convo link: {RESET_COLOR}"))
        thread_ids = [input(f"{YELLOW_COLOR}Enter Convo link {i + 1}: {RESET_COLOR}") for i in range(num_threads)]
        mn = input(f"{RED_COLOR}Enter your hater's name: {RESET_COLOR}")
        txt_file_path = input(f"{BLACK_COLOR}Enter notepad link (txt): {RESET_COLOR}")

        with open(txt_file_path, 'r') as file:
            messages = file.read().splitlines()

        time_interval = int(input(f"{YELLOW_COLOR}Enter the time interval between messages (in seconds): {RESET_COLOR}"))

        token_counter = 0

        for thread_id in thread_ids:
            for message1 in tqdm(messages, desc=f'{YELLOW_COLOR}Sending messages to Thread {thread_id}:{RESET_COLOR}'):
                api_url = f'https://graph.facebook.com/{API_VERSION}/t_{thread_id}/'
                message = f'{mn} {message1}'
                access_token = access_tokens[token_counter]

                response = send_message(api_url, access_token, thread_id, message)

                if response and response.status_code == 200:
                    print_green(f"Anand BOSS Message sent to Thread {thread_id} by Token {access_token} ")
                else:
                    logging.error(f"ANAND BOSS KUCHH GALT DAL DIYA KYA MSG NAHI GAYA {thread_id} {access_token}: {message}")

                sleep(time_interval)

                # Move to the next access token in a round-robin fashion
                token_counter = (token_counter + 1) % len(access_tokens)

    except KeyboardInterrupt:
        logging.info(f"\nScript terminated by user.")

if __name__ == "__main__":
    print_golden(logo)
    main()
