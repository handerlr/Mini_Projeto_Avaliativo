import csv
import re
from datetime import datetime

# ==========================================
# 1. FUNÇÕES AUXILIARES
# ==========================================

def limpar_categoria(nome):
    # Se o nome for vazio ou nulo
    if nome == "" or nome == None:
        return "sem categoria"

    # Deixa tudo minúsculo e tira os espaços em branco das pontas
    nome = nome.lower()
    nome = nome.strip()

    # Usa o Regex para trocar o que não for letra, número ou espaço por nada ('')
    nome = re.sub(r'[^a-z0-9 ]', '', nome)

    return nome

def mudar_formato_data(data_texto):
    if data_texto == "" or data_texto == None:
        return ""

    try:
        # Transforma o texto em uma data do Python
        data_python = datetime.strptime(data_texto, "%Y-%m-%d %H:%M:%S")
        # Transforma a data do Python no formato brasileiro
        data_brasil = data_python.strftime("%d/%m/%Y")
        return data_brasil
    except:
        # Se der erro, devolve como estava
        return data_texto

# ==========================================
# 2. FUNÇÃO PRINCIPAL
# ==========================================

def executar_limpeza():
    # Variáveis para contar os resultados no final
    total_produtos = 0
    categorias_arrumadas = 0
    produtos_jogados_fora = 0

    total_pedidos = 0
    pedidos_cancelados = 0
    datas_vazias = 0
    cancelados_e_vazios = 0

    print("Começando a ler os arquivos...\n")

    # --- LENDO OS PRODUTOS ---
    with open('olist_products_dataset.csv', mode='r', encoding='utf-8') as arquivo_prod:
        leitor_produtos = csv.DictReader(arquivo_prod)

        for linha in leitor_produtos:
            total_produtos = total_produtos + 1

            # Arrumar categoria vazia
            categoria_atual = linha['product_category_name']
            if categoria_atual == "":
                linha['product_category_name'] = "Sem Categoria"
                categorias_arrumadas = categorias_arrumadas + 1

            # Limpar o texto da categoria usando a função
            linha['product_category_name'] = limpar_categoria(linha['product_category_name'])

            # Tratar nulos nas dimensões (Regra escolhida: descartar a linha)
            # Justificativa: Escolhi jogar a linha fora porque se eu colocar um peso
            # ou tamanho inventado (como a média), o valor do frete vai sair errado.
            peso = linha['product_weight_g']
            comprimento = linha['product_length_cm']
            altura = linha['product_height_cm']
            largura = linha['product_width_cm']

            if peso == "" or comprimento == "" or altura == "" or largura == "":
                produtos_jogados_fora = produtos_jogados_fora + 1
                continue # Pula para a próxima linha sem salvar essa


    # --- LENDO OS PEDIDOS ---
    with open('olist_orders_dataset.csv', mode='r', encoding='utf-8') as arquivo_ped:
        leitor_pedidos = csv.DictReader(arquivo_ped)

        for linha in leitor_pedidos:
            total_pedidos = total_pedidos + 1

            status = linha['order_status']
            data_entrega = linha['order_delivered_customer_date']
            data_aprovacao = linha['order_approved_at']

            # Contar cancelados
            if status == 'canceled':
                pedidos_cancelados = pedidos_cancelados + 1

            # Verificar a hipótese da diretoria
            if data_entrega == "":
                datas_vazias = datas_vazias + 1
                if status == 'canceled':
                    cancelados_e_vazios = cancelados_e_vazios + 1

            # Arrumar a data de aprovação
            linha['order_approved_at'] = mudar_formato_data(data_aprovacao)

    # --- RELATÓRIO NA TELA ---
    print("--- RELATÓRIO FINAL ---")
    print("\n[PRODUTOS]")
    print(f"Total lido: {total_produtos}")
    print(f"Categorias vazias que foram preenchidas: {categorias_arrumadas}")
    print(f"Produtos descartados por falta de medida: {produtos_jogados_fora}")

    print("\n[PEDIDOS]")
    print(f"Total lido: {total_pedidos}")
    print(f"Total de pedidos cancelados: {pedidos_cancelados}")

    print("\n[VALIDAÇÃO DA IDEIA DA DIRETORIA]")
    print("A diretoria achava que toda data de entrega vazia era de pedido cancelado.")
    print(f"Total de datas de entrega vazias: {datas_vazias}")
    print(f"Desses, quantos estavam cancelados: {cancelados_e_vazios}")

    if datas_vazias == cancelados_e_vazios:
        print("Resposta: A diretoria está certa!")
    else:
        print("Resposta: A diretoria está errada. Tem pedido sem data de entrega que não foi cancelado.")

# Rodar o código
if __name__ == "__main__":
    executar_limpeza()