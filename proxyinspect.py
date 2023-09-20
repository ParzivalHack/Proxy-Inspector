import requests
from colorama import Fore, Style

def check_proxy(proxy: str) -> list[bool, bool]:
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
        if response.status_code == 200:
            client_ip = response.json().get('origin', '')
            if client_ip.startswith(proxy.split(':')[0]):
                return True, True
            return True, False
        return False, False
    except requests.RequestException:
        return False, False

def main():
    try:
        with open('proxies.txt', 'r') as file:
            proxies = [line.strip() for line in file]
    except FileNotFoundError:
        print("File proxies.txt not found")
        input("Press Enter to exit..."); exit()

    total_proxies = len(proxies)
    valid_proxies = []

    print(f"Total proxies: {total_proxies}")

    for proxy in proxies:
        print(f"Testing proxy {proxy} from list proxies.txt...")
        """
        if check_proxy(proxy):
            if is_proxy_anonymous(proxy):
                valid_proxies.append(proxy)
                print(f"{Fore.GREEN}Proxy Valid and Anonymous{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}Proxy Valid but Not Anonymous{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Proxy Invalid{Style.RESET_ALL}")
        """
        valid, anonymous = check_proxy(proxy)
        if valid:
            if anonymous:
                valid_proxies.append(proxy)
                print(f"{Fore.GREEN}Proxy Valid and Anonymous{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}Proxy Valid but Not Anonymous{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Proxy Invalid{Style.RESET_ALL}")
    print(f"\nTotal valid and anonymous proxies: {len(valid_proxies)}")
    with open('valid_proxies.txt', 'w') as file:
        file.write('\n'.join(valid_proxies))
    print("Valid proxies saved in valid_proxies.txt")
    input("Press Enter to exit...")
    exit()

if __name__ == "__main__":
    print("""

██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ██╗███╗   ██╗███████╗██████╗ ███████╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██║████╗  ██║██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ██║██╔██╗ ██║███████╗██████╔╝█████╗  ██║        ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ██║██║╚██╗██║╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ██║██║ ╚████║███████║██║     ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                     

""")
    print("DISCLAIMER:\nThe accuracy of this tool depends on the restrictions of the proxy you are testing.\nMany public proxies use IP Rotation, Rate Limiting and Server Load Limiting which sometimes prevents the successfull connection to them.")
    input("\nPress Enter to start checking proxies...")
    main()
