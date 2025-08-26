import os
import requests
from concurrent.futures import ThreadPoolExecutor

def baixar_fatura(item, base_url, save_dir):
    invoice_url = base_url + item["invoice"]
    numero_fatura = os.path.splitext(os.path.basename(item["invoice"]))[0]
    filename = os.path.join(save_dir, f"{numero_fatura}.jpg")

    r = requests.get(invoice_url, stream=True)
<<<<<<< HEAD
=======
    r.raise_for_status()  # lança erro se a requisição falhar
>>>>>>> 9a50d48c945aca1cc226bb0f0002c3dd3afb888a

    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

<<<<<<< HEAD
    print(f"Fatura baixada: {item["id"]}, Link: {invoice_url}")
=======
    print(f"Baixado: {filename}")
>>>>>>> 9a50d48c945aca1cc226bb0f0002c3dd3afb888a

def baixar_faturas_paralelo(faturas, base_url, save_dir):
    with ThreadPoolExecutor(max_workers=12) as executor:
        executor.map(lambda item: baixar_fatura(item, base_url, save_dir), faturas)