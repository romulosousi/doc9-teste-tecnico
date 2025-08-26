# doc9-teste-tecnico
Teste Técnico Doc9: Automação em Python para extrair dados de uma tabela web, fazer o download de PDFs e gerar um CSV.

##Descrição
Esse script baixa automaticamente todas as faturas de um site, filtra apenas as faturas vencidas ou que vencem hoje, e gera umCSV com informações de cada fatura.

## Estrutura do projeto
- `main.py`: Código principal que faz o download e cria o CSV
- `downloader.py`: Funções para download de faturas
- `csv_utils.py`: Função que cria o CSV
- `data_utils.py`: Função que filtra as faturas vencidas
- `config.py`: Arquivo que contém parâmetros de configurações
- `invoices/`: Pasta onde as faturas serão salvas

## Requisitos
- Python 3.13.5

## Decisões Técnicas e Otimizações de Performance
- **Escolha da biblioteca:** A ideia iniceral era usar Selenium, mas como um dos critérios de avaliação era executar o código em menos de 2 segundos, o Selenium teria desclassificado o projeto. Por isso utilizei `requests`para capturar via POST o JSON contendo todas as faturas.

- **Download paralelo:** Cada fatura precisa ser baixada. Como são 12 faturas, baixar uma a uma levaria mais de 12 segundos. Para otimizar, foi usado `ThreadPoolExecutor` com `max_workers=12`, permitindo baixar todas em paralelo, reduzindo o tempo total para cerca de 1 segundo.

- **Bibliotecas padrão do Python:** Nenhuma biblioteca externa é necessária; todas usadas são padrão do Python (`os`, `csv`, `datetime`, `concurrent.futures`, `requests`).

- **Observação sobre tempo de execução:** No computador local (Nordeste do Brasil), o tempo médio foi de 2 segundos. No Google Colab, devido à proximidade do servidor, o tempo caiu para cerca de 0,20 segundos.