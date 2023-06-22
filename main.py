import requests
import xml.etree.ElementTree as ET
import keyboard
import wolframId

counter = 1
pi = ""


def getAnswer():
    global counter, pi
    question = f"get the digit {counter} of pi"
    answer = askToWolfram(question)

    if pi == "":
        pi += answer + "."
    else:
        pi += answer.strip()

    print(pi)
    counter += 1


def askToWolfram(q):
    try:
        api = "http://api.wolframalpha.com/v2/query?podindex=2&format=plaintext&appid=" + \
            wolframId.WOLFRAM_APP_ID + "&input=" + q
        response = requests.get(api)

        # Parse the XML response
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            if root.get("success") == "true":
                pod = root.find(".//pod")
                subpod = pod.find(".//subpod")
                return subpod.find("plaintext").text
    except Exception as e:
        pass
    return False


def printTitle():
    print(" _____                     ___  ___                     ______  ")
    print("|  ___|                    |  \/  |                     | ___ (_)")
    print("| |____   _____ _ __ ______| .  . | ___  _ __ ___ ______| |_/ /_ ")
    print("|  __\ \ / / _ \ '_ \______| |\/| |/ _ \| '__/ _ \______|  __/| |")
    print("| |___\ V /  __/ | | |     | |  | | (_) | | |  __/      | |   | |")
    print("\____/ \_/ \___|_| |_|     \_|  |_/\___/|_|  \___|      \_|   |_|")


printTitle()
print("")
print("Press ENTER to add a digit to pi, press ESC to block the program")
print("")
while True:
    if keyboard.is_pressed('enter'):
        getAnswer()
    if keyboard.is_pressed('esc'):
        print("Program Blocked")
        break
