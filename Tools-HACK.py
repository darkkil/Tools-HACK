import os
os.system("clear")
def menu():

    print(""" 
    
               __.......__
            .-:::::::::::::-.
          .:::''':::::::''':::.
        .:::'     `:::'     `:::.
   .'\  ::'   ^^^  `:'  ^^^   '::  /`.
  :   \ ::   _.__       __._   :: /   ;
 :     \`: .' ___\     /___ `. :'/     ;
:       /\   (_|_)\   /(_|_)   /\       ;
:      / .\   __.' ) ( `.__   /. \      ;
:      \ (        {   }        ) /      ;
 :      `-(     .  ^"^  .     )-'      ;
  `.       \  .'<`-._.-'>'.  /       .'
    `.      \    \;`.';/    /      .'
      `._    `-._       _.-'    _.'
       .'`-.__ .'`-._.-'`. __.-'`.
     .'       `.         .'       `.
   .'           `-.   .-'           `.
       _           ___   _  _    __
      | |__ _  _  / __| | \| |  /  \
      | '_ \ || | \__ \ | .` | | () |
      |_.__/\_, | |___/ |_|\_|  \__/
            |__/
===============================================
      This script ONLY FOR Termux users!
===============================================
 1. Install Nmap 
 2. Install Hydra
 3. Install SQLMap
 4. Install Metasploit
 5. Install ngrok
 6. Install Kali Nethunter
 7. Install angryFuzzer
 8. Install Red_Hawk
 9. Install Weeman
10. Install IPGeoLocation
11. Install Cupp
12. Instagram Bruteforcer (instahack)
13. Twitter Bruteforcer   (TwitterSniper)
14. Install Ubuntu
15. Install Fedora
16. Install viSQL
17. Install Hash-Buster
18. Install D-TECT
19. Install Routersploit
20. Install Tmux-Bunch ( Bind payload in apps )
21. Install Vncserver
22. Install Wireshark
23. Install ArchLinux                     [working]
24. Install social engineering Tool kit
25. Install HTTrack                       [working]
26. Install Beef-xss
27. Coming soon
==============================================
99. Exit
===============================================
""")

loop = True

while loop:
    menu()
    what = input("##: ")
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap installed successfully :)")
        print("[+] Type 'nmap' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra installed successfully :)")
        print("[+] Type 'hydra' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap installed successfully :)")
        print("[+] Go to sqlmap folder and type 'python2 sqlmap.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit installed successfully :)")
        print("[+] Type 'msfconsole' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        os.system("cp /data/data/com.termux/files/home/ngrok /date/date/com.termux/files/usr/bin")
        os.system("cd /data/data/com.termux/files/usr/bin && chmod +x ngrok")
        print("====================================")
        print("[+] ngrok installed successfully :)")
        print("[+] Type 'ngrok http 80' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter installed successfully :)")
        print("[+] Go to Nethunter-In-Termux folder and type './kalinethunter' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] angryFuzzer installed successfully :)")
        print("[+] Go to angryFuzzer folder and type 'python2 angryFuzzer.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK installed successfully :)")
        print("[+] Go to RED_HAWK folder and type 'php rhawk.php' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman installed successfully :)")
        print("[+] Go to weeman folder and type 'python2 weeman.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation installed successfully :)")
        print("[+] Go to IPGeoLocation folder and type 'python ipgeolocation.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp installed successfully :)")
        print("[+] Go to cupp folder and type 'python cupp3.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack installed successfully :)")
        print("[+] Go to instahack folder and type 'python hackinsta.py' to start.")
        print("====================================") 
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper installed successfully :)")
        print("[+] Go to TwitterSniper folder and type 'python TwitterSniper.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu installed successfully :)")
        print("[+] Go to termux-ubuntu folder and type './start.sh' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora installed successfully :)")
        print("[+] Type 'sh termux-fedora.sh f26_arm64' or 'sh termux-fedora.sh f26_arm' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL installed successfully :)")
        print("[+] Go to viSQL folder and type 'python2 viSQL.py --help' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "19":
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit installed successfully :)")
            print("[+] Go to routersploit folder and type 'python2 rsf.py' to start.")
            print("====================================")
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "20":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone  https://github.com/Hax4us/Tmux-Bunch")
        os.system("cd /data/data/com.termux/files/home && cd Tmux-Bunch")
        os.system("cd /data/data/com.termux/files/home && cd Tmux-Bunch && chmod +x auto-update setup tmuxbunch")
        os.system("cd /data/data/com.termux/files/home && cd Tmux-Bunch && ./tmuxbunch")
        os.system("cd /data/data/com.termux/files/home && cd Tmux-Bunch && ./setup")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Tmux-Bunch installed successfully :)")
        print("[+] type 'tmuxbunch' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "21":
        os.system("pkg update -y")
        os.system("pkg install -y curl")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && curl -LO https://raw.githubusercontent.com/Hax4us/guitmux/master/guitmux")
        os.system("cd /data/data/com.termux/files/home && chmod +x guitmux")
        os.system("cd /data/data/com.termux/files/home && ./guitmux")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] vncserver installed successfully :)")
        print("[+] Type 'vncserver' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "22":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y curl")
        os.system("cd /data/data/com.termux/files/home && curl -LO  https://raw.githubusercontent.com/Hax4us/Hax4us.github.io/master/termux-x-tools")
        os.system("cd /data/data/com.termux/files/home && chmod +x termux-x-tools")
        os.system("cd /data/data/com.termux/files/home && ./termux-x-tools")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Wireshark installed successfully :)")
        print("[+] Type 'wireshark-gtk' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "23":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y curl")
        os.system("cd /data/data/com.termux/files/home && curl -LO  https://raw.githubusercontent.com/sdrausty/TermuxArch/master/setupTermuxArch.sh")
        os.system("cd /data/data/com.termux/files/home && chmod +x setupTermuxArch.sh ")
        os.system("cd /data/data/com.termux/files/home && sh setupTermuxArch.sh")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ArchLinux installed successfully :)")
        print("[+] Go to ArchLinux folder.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "24":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y curl")
        os.system("cd /data/data/com.termux/files/home && curl -LO  https://raw.githubusercontent.com/Hax4us/setoolkit/master/setoolkit.sh")
        os.system("cd /data/data/com.termux/files/home && chmod +x setoolkit.sh")
        os.system("cd /data/data/com.termux/files/home && sh setoolkit.sh")
        os.system("cd /data/data/com.termux/files/home && cd setoolkit && chmod +x setup.py")
        os.system("cd /data/data/com.termux/files/home && cd setoolkit && ./setup.py install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Setoolkit installed successfully :)")
        print("[+] Type 'setoolkit' to start")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "25":
        os.system("pkg update -y")
        os.system("apt install -y termux-exec")
        os.system("pkg install -y curl")
        os.system("cd /data/data/com.termux/files/home && curl -LO  https://raw.githubusercontent.com/Hax4us/httrack_In_termux/master/httrack")
        os.system("cd /data/data/com.termux/files/home && chmod +x httrack")
        os.system("cd /data/data/com.termux/files/home && sh httrack")
        os.system("cd /data/data/com.termux/files/home")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] HTTrack installed successfully :)")
        print("[+] Now you can Exit and Start again Termux then Type httrack")
        print("====================================")
        rmenu = input("[?] Do you want to Exit (y/n): ")
        if rmenu == "n":
            menu()
        else:
            break
    elif what == "26":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y beef-xss")
        print("====================================")
        print("[+] BeEF installed successfully :)")
        print("[+] Type beef-xss to start")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "99":
        print("Bye.")
        break
