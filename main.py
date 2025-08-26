import os
import time
import requests
from downloader import baixar_faturas_paralelo
from csv_utils import salvar_csv
from data_utils import filtrar_faturas_vencidas
import config

# Início da contagem
start_time = time.time()

<<<<<<< HEAD
os.makedirs(config.SAVE_DIR, exist_ok=True)

# Post para buscar dados
res = requests.post(config.SEED_URL)
data = res.json()["data"]


# Filtrar faturas vencidas ou de hoje
faturas_validas = filtrar_faturas_vencidas(data)
print(f"\nTotal de faturas vencidas ou de hoje: {len(faturas_validas)}\n")
=======
# Criar pasta de destino
os.makedirs(config.SAVE_DIR, exist_ok=True)

# Obter dados da tabela
res = requests.post(config.SEED_URL)
res.raise_for_status()
data = res.json()["data"]

# Filtrar faturas vencidas ou de hoje
faturas_validas = filtrar_faturas_vencidas(data)
>>>>>>> 9a50d48c945aca1cc226bb0f0002c3dd3afb888a

# Baixar faturas em paralelo
baixar_faturas_paralelo(faturas_validas, config.BASE_URL, config.SAVE_DIR)

# Criar CSV
salvar_csv(faturas_validas, config.BASE_URL, config.CSV_FILE)

# Fim da contagem
end_time = time.time()
tempo_execucao = end_time - start_time
print(f"\nCSV criado: {config.CSV_FILE}")
print(f"Processo concluído! Tempo total de execução: {tempo_execucao:.1f} segundos")
