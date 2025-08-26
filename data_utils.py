from datetime import datetime

def filtrar_faturas_vencidas(data):
    hoje = datetime.today().date()
    faturas_validas = [
        item for item in data
        if datetime.strptime(item["duedate"], "%d-%m-%Y").date() <= hoje
    ]

    for item in faturas_validas:
        data_fatura = datetime.strptime(item["duedate"], "%d-%m-%Y").strftime("%d/%m/%Y")
        print(f"Fatura vencida: {item['id']}, Data da Fatura: {data_fatura}")

    return faturas_validas
