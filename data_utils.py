from datetime import datetime

def filtrar_faturas_vencidas(data):
    hoje = datetime.today().date()
    faturas_validas = [
        item for item in data
        if datetime.strptime(item["duedate"], "%d-%m-%Y").date() <= hoje
    ]
    return faturas_validas
