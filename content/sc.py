import requests as r

class Sc:
    def Main():
        user = str(input("[Input Link] >_ "))
        req = r.get(user)
        if req.status_code == 200:
            g = open("Result.html", "w+")
            g.write(req.text)
            g.close()
        else:
            print("[!] Check Your Connection")