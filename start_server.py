from pynput.keyboard import Controller
import subprocess
from time import sleep
from keyboard import press

keyboard = Controller()

def peppy():
    subprocess.Popen([r"C:\Program Files\ConEmu\ConEmu64.exe"])

    sleep(3)

    for characters in "B:":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press("enter")

    for characters in "cd B:/redstar/pep.py":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    for characters in "python pep.py":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

def lets():
    subprocess.Popen([r"C:\Program Files\ConEmu\ConEmu64.exe"])

    sleep(3)

    for characters in "B:":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press("enter")

    for characters in "cd B:/redstar/lets":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    for characters in "python lets.py":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

def avatar_server():
    subprocess.Popen([r"C:\Program Files\ConEmu\ConEmu64.exe"])

    sleep(3)

    for characters in "B:":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press("enter")

    for characters in "cd B:/redstar/avatar-server":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    for characters in "python avatarserver.py":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

def redis():
    subprocess.Popen([r"C:\Program Files\ConEmu\ConEmu64.exe"])
    
    sleep(3)

    for characters in "B:":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press("enter")

    for characters in "cd B:/redstar/Redis":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    for characters in "redis.bat":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

def nginx():
    subprocess.Popen([r"C:\Program Files\ConEmu\ConEmu64.exe"])
    
    sleep(3)

    for characters in "B:":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press("enter")

    for characters in "cd B:/redstar/nginx-1.23.3":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    for characters in "nginx.exe":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

def frontend():
    #subprocess.Popen([r"C:\Windows\System32\bash.exe"])
    subprocess.Popen([r"C:\Program Files\ConEmu\ConEmu64.exe"])
    
    sleep(3)

    for characters in "B:":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press("enter")

    for characters in "cd B:/redstar/Frontend":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    for characters in "bash":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    sleep(1)

    """ for characters in "cd /mnt/b/redstar/Frontend":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.1)
    press('enter') """

    for characters in "./frontend":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

def api():
    #subprocess.Popen([r"C:\Windows\System32\bash.exe"])
    subprocess.Popen([r"C:\Program Files\ConEmu\ConEmu64.exe"])
    
    sleep(3)

    for characters in "B:":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press("enter")

    for characters in "cd B:/redstar/api":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    for characters in "bash":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    sleep(1)

    """ for characters in "cd /mnt/b/redstar/api":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.1)
    press('enter') """

    for characters in "./API":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

def realistik_panel():
    subprocess.Popen([r"C:\Program Files\ConEmu\ConEmu64.exe"])
    
    sleep(3)

    for characters in "B:":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press("enter")

    for characters in "cd B:/redstar/RealistikPanel":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    for characters in "python main.py":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

def discord_redstar_moe():
    subprocess.Popen([r"C:\Program Files\ConEmu\ConEmu64.exe"])
    
    sleep(3)

    for characters in "B:":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press("enter")

    for characters in "cd B:/redstar/discord.redstar.moe":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

    for characters in "node index.js":
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.01)
    press('enter')

def main():
    discord_redstar_moe()
    realistik_panel()
    nginx()
    redis()
    lets()
    peppy()
    avatar_server()
    api()
    frontend()
    

if __name__ == '__main__':
    main()
