import os
from bs4 import BeautifulSoup as bs
import urllib3 as url
from content.xss import *
from content.dork import *
from content.sc import *

class Main:
    def banner():
        print("               ';.")
        print("    .---.,       \  [!] Report Error To My Social Media :)")
        print("   []-.__,>=======;==================")
        print("    `----'      ,/   [Rose Killer]")
        print("              .;'        [By]")
        print("                    [Fajar Firdaus]")
    def Run():
        def help():
            print("[Help Commands]")
            print("- help (See all commands)")
            print("- xss (exploit websites using xss method)")
            print("- dork (dork website)")
            print("- script (take script deface in website)")
        
        user = str(input("\n\n[RoseKiller] >_ "))
        if user == "xss":
            xss = Xss.main()
        elif user == "dork":
            dork = Dork.main()
        elif user == "script":
            sc = Sc.main()
        elif user == "help":
            help()
        else:
            print("[!] Wrong Commands")
            help()

banner = Main.banner()
r = Main.Run()
