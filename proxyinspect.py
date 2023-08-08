import requests
from colorama import Fore, Style
def ascii_art():
    print("""

██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ██╗███╗   ██╗███████╗██████╗ ███████╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██║████╗  ██║██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ██║██╔██╗ ██║███████╗██████╔╝█████╗  ██║        ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ██║██║╚██╗██║╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ██║██║ ╚████║███████║██║     ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                     

""")

def check_proxy(proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

def is_proxy_anonymous(proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
        if response.status_code == 200:
            client_ip = response.json().get('origin', '')
            if not client_ip.startswith(proxy.split(':')[0]):
                return True
    except requests.RequestException:
        pass
    return False

def main():
    filename = 'proxies.txt'
    with open(filename, 'r') as file:
        proxies = [line.strip() for line in file]

    total_proxies = len(proxies)
    valid_proxies = []

    print(f"Total proxies: {total_proxies}")

    for proxy in proxies:
        print(f"Testing proxy {proxy} from list {filename}...")
        if check_proxy(proxy):
            if is_proxy_anonymous(proxy):
                valid_proxies.append(proxy)
                print(f"{Fore.GREEN}Proxy Valid and Anonymous{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}Proxy Valid but Not Anonymous{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Proxy Invalid{Style.RESET_ALL}")

    print(f"\nTotal valid and anonymous proxies: {len(valid_proxies)}")
    print("Valid and anonymous proxies list:")
    for proxy in valid_proxies:
        print(proxy)

if __name__ == "__main__":
    ascii_art()
    print("DISCLAIMER:\nThe accuracy of this tool depends on the restrictions of the proxy you are testing.\nMany public proxies use IP Rotation, Rate Limiting and Server Load Limiting which sometimes prevents the successfull connection to them.")
    start = input("\nPress Enter to start checking proxies...")
    main()
