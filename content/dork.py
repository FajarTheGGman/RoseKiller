import urllib3 as url
from bs4 import BeautifulSoup

class Dork:
    def main():
        req = url.PoolManager()
        user = str(input("[Dork] >_ "))
        for ulang in range(10):
            send = req.request("GET", "http://www1.search-results.com/web?q=" + user + "&page=" + str(ulang))
            parsing = BeautifulSoup(send, features="lxml")
            print("[+] Here's The Results")
            for data in parsing.find_all("cite"):
                print(data.string)