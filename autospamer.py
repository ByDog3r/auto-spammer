import os
from pyautogui import typewrite
from time import sleep

RED, GREEN, NONE, wards = "\033[0;31m", "\033[1;32m", "\033[0m", []

def script():

    def logo():
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print(f"""{RED}
        ▄▄▄· ▄• ▄▌▄▄▄▄▄      ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ·▄▄▄▄  
        ▐█ ▀█ █▪██▌•██  ▪     ██· █▌▐█▐█ ▀█ ▀▄ █·██▪ ██ 
        ▄█▀▀█ █▌▐█▌ ▐█.▪ ▄█▀▄ ██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐█· ▐█▌
        ▐█ ▪▐▌▐█▄█▌ ▐█▌·▐█▌.▐▌▐█▌██▐█▌▐█ ▪▐▌▐█•█▌██. ██ 
        ▀  ▀  ▀▀▀  ▀▀▀  ▀█▄▀▪ ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀▀▀▀▀▀• 
        {GREEN}            Made for @ByDog3r\n
        """+NONE)

    def main():
        try:
            logo()

            word = input("Enter the text you want to repeat > ")

            again = int(input("Enter the number of comments or messages > ")); logo()

            print(f"{GREEN}[{NONE}*{GREEN}]{NONE} Select comment or DM"); sleep(5)

            [wards.append(word) for comment in range(again)]
            for comment in range(again):
                typewrite(wards[comment%7])
                typewrite("\n")
                sleep(2)
            
            logo()
            print(f"{GREEN}[{RED}~{GREEN}]{NONE} The attack has been completed successfully..")
        except:

            logo()
            print(f"{RED}Follow directions... " + NONE)

    main()

script()