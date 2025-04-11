import schedule
import time
import requests

def acessar():
    print("Acessando site...")
    requests.get("https://abaixo-assinado-1.onrender.com/")

schedule.every(1).minutes.do(acessar)

while True:
    schedule.run_pending()
    time.sleep(1)
