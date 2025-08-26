import csv
import os

def salvar_csv(faturas, base_url, csv_file):
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID da Fatura", "Data da Fatura", "URL da fatura"])
        for item in faturas:
            id_fatura = item["id"]
            writer.writerow([id_fatura, item["duedate"], base_url + item["invoice"]])