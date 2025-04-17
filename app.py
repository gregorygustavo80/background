import schedule
import time
import requests

sites = [
    "https://abaixo-assinado-1.onrender.com/",
    "https://bioinsightstools.streamlit.app/",
]

def acessar():
    print("Acessando sites...")
    for site in sites:
        try:
            print(f"Acessando {site}")
            requests.get(site)
        except Exception as e:
            print(f"Erro ao acessar {site}: {e}")

schedule.every(10).minutes.do(acessar)

while True:
    schedule.run_pending()
    time.sleep(1)
