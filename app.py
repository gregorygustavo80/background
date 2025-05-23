import schedule
import time
import requests

sites = [
    "https://groggy.onrender.com",
]

def acessar():
    print("Acessando sites...")
    for site in sites:
        try:
            print(f"Acessando {site}")
            requests.get(site)
        except Exception as e:
            print(f"Erro ao acessar {site}: {e}")

schedule.every(1).minutes.do(acessar)

while True:
    schedule.run_pending()
    time.sleep(1)
