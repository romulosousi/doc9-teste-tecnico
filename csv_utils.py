import csv
import os

def salvar_csv(faturas, base_url, csv_file):
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
<<<<<<< HEAD
        writer.writerow(["ID da Fatura", "Data da Fatura", "URL da fatura"])
        for item in faturas:
            id_fatura = item["id"]
            writer.writerow([id_fatura, item["duedate"], base_url + item["invoice"]])
=======
        writer.writerow(["Número da Fatura", "Data da Fatura", "URL da fatura"])
        for item in faturas:
            numero_fatura = os.path.splitext(os.path.basename(item["invoice"]))[0]
            writer.writerow([numero_fatura, item["duedate"], base_url + item["invoice"]])
>>>>>>> 9a50d48c945aca1cc226bb0f0002c3dd3afb888a
