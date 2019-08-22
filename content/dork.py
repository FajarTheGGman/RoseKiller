import urllib3 as url
from bs4 import BeautifulSoup

class Dork:
    def main():
        req = url.PoolManager()
        user = str(input("[Dork] >_ "))
        print("[+] Here's The Results")
        send = req.request("GET", "http://www1.search-results.com/web?q=" + user)
        parsing = BeautifulSoup(send.data, features="html.parser")
        for data in parsing.find_all("cite"):
            print(data.string)
