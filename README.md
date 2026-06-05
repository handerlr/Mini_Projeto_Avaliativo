# Mini_Projeto_Avaliativo
Machine Learning e Visão Computacional [T2]  Mini-Projeto Avaliativo - Módulo 1 - Semana 07 realizado conforme proposta do curso SCTEC 

# Projeto de Limpeza de Dados - Olist

## Sobre o Projeto
Este é o meu mini-projeto de Engenharia de Dados. A ideia é pegar arquivos de produtos e pedidos da loja Olist que estão bagunçados e com informações faltando, e fazer uma limpeza geral neles (isso é chamado de ETL). 

Eu fiz tudo usando apenas o Python puro, sem usar bibliotecas prontas como o Pandas. O código arruma textos, preenche coisas vazias, muda o formato das datas para o jeito brasileiro e ainda verifica uma dúvida que a diretoria da empresa tinha sobre os pedidos cancelados.

## Como rodar no seu computador
1. Você precisa ter o Python instalado.
2. Baixe os dois arquivos de dados: `olist_products_dataset.csv` e `olist_orders_dataset.csv`.
3. Coloque esses dois arquivos na mesma pasta onde está o meu arquivo `main.py`.
4. Abra o terminal (ou prompt de comando), vá até a pasta e digite:
   `python main.py`
5. O programa vai rodar e mostrar um relatório com os resultados na sua tela.

## Por que limpar os dados ajuda a Inteligência Artificial? (Reflexão)
No mundo da Inteligência Artificial, existe uma regra famosa: "Lixo entra, lixo sai". Isso significa que se a gente tentar ensinar uma IA usando dados errados ou sujos, ela vai aprender errado. Por exemplo, se a gente deixar a categoria "Moveis" e "móveis!!" como duas coisas diferentes porque não limpamos o texto, a IA vai ficar confusa. 

Além disso, temos que cuidar com os dados nulos. No meu código, decidi apagar produtos que não tinham peso ou tamanho. Se eu inventasse um valor para colocar no lugar (como a média), a Inteligência Artificial ia achar que muitos pacotes têm aquele tamanho exato. Isso deixaria ela "viciada" nesse valor falso, gerando um problema chamado de *Overfitting*, e ela ia errar feio na hora de calcular o frete de um produto real no futuro.
