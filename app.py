import schedule
import time
import requests

def acessar():
    print("Acessando site...")
    requests.get("https://google.com")

schedule.every(1).minutes.do(acessar)

while True:
    schedule.run_pending()
    time.sleep(1)
