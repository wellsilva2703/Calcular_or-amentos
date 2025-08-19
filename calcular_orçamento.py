print('-> Bem vindo ao programa para calcular orçamento!')
#\\Para usar é simples, abaixo tem uma lista de opções e basta escolher a que quer acessar, por exemplo: 2 - Calcular orçamento -> Gradil e assim em diante..
import json


def calcular_pintura():
    nome_cliente = input('Qual o nome do cliente ou empresa?\n')
    valor_metragem_pintura = float(input('Qual o valor da metragem da pintura?\n->R$'))
    metragem_total_pintura = float(input('Qual a metragem total da aréa para pintura?\n->'))
    total_pintura = valor_metragem_pintura * metragem_total_pintura

    try:
        with open('Orçamentos_pinturas.json', 'r', encoding='utf-8') as arquivo_pintura:
            lista_geral_pinturas = json.load(arquivo_pintura)
            print(lista_geral_pinturas) 

    except FileNotFoundError:
        lista_geral_pinturas = []
        
    lista_geral_pinturas.append({
        'Nome do cliente/empresa': nome_cliente,
        'Valor da metragem': valor_metragem_pintura,
        'Metragem total': metragem_total_pintura,
        'Valor final do orçamento': total_pintura
    })

    with open('Orçamentos_pinturas.json', 'w', encoding='utf-8') as arquivo_pintura:
        json.dump(lista_geral_pinturas, arquivo_pintura, ensure_ascii=False, indent=6)

    return f'Nome do cliente: {nome_cliente}\nValor p\Metro(pintura) = R${valor_metragem_pintura:.2f}\nMetragem total da aréa para pintura = {metragem_total_pintura}M\nValor total da area para a pintura = R${total_pintura:.2f}'

def calcular_gradil():
    nome_do_cliente = input('Qual o nome do cliente ou empresa?\n')
    valor_metragem_gradil = float(input('Qual o valor da metragem dos gradils?\n->R$'))
    metragem_total_gradio = float(input('Qual a metragem total da aréa dos gradils?\n->'))
    total_gradil = valor_metragem_gradil * metragem_total_gradio

    try:
        with open('Orçamento_gradils.json', 'r', encoding='utf-8') as arquivo_gradils:
            lista_geral_gradils = json.load(arquivo_gradils)
            print(lista_geral_gradils)

    except FileNotFoundError:
        lista_geral_gradils = []
 
    lista_geral_gradils.append({
        'Nome do cliente/empresa': nome_do_cliente,
        'Valor da metragem': valor_metragem_gradil,
        'Metragem total': metragem_total_gradio,
        'Valor final do orçamento': total_gradil
    })

    with open('Orçamentos_gradils.json', 'w', encoding='utf-8') as arquivo_gradils:
        json.dump(lista_geral_gradils, arquivo_gradils, ensure_ascii=False, indent=6)

    return f'Nome do cliente: {nome_do_cliente}\nValor per metragem: R${valor_metragem_gradil:.2f}\nMetragem total: {metragem_total_gradio}M\nValor total = R${total_gradil:.2f}'

def calcular_alvenaria():
    nome_do_cliente = input('Qual o nome do cliente ou empresa?\n')
    valor_metragem_alvenaria = float(input('Qual o valor da metragem da alvenaria?\n->R$'))
    metragem_total_alvenaria = float(input('Qual a metragem total da aréa da alvenaria?\n->'))
    total_alvenaria = valor_metragem_alvenaria * metragem_total_alvenaria

    try:
        with open('Orçamentos_alvenaria.json', 'r', encoding='utf-8') as arquivo_alvenaria:
            lista_geral_alvenaria = json.load(arquivo_alvenaria)
            print(lista_geral_alvenaria)
    
    except FileNotFoundError:
        lista_geral_alvenaria = []
        

    lista_geral_alvenaria.append({
        'Nome do cliente/empresa': nome_do_cliente,
        'Valor da metragem': valor_metragem_alvenaria,
        'Metragem total': metragem_total_alvenaria,
        'Valor final do orçamento': total_alvenaria,
    })

    with open('Orçamentos_alvenaria.json', 'w', encoding='utf-8') as arquivo_alvenaria:
        json.dump(lista_geral_alvenaria, arquivo_alvenaria, ensure_ascii=False, indent=6)

    return f'Nome do cliente: {nome_do_cliente}\nValor per metragem: R${valor_metragem_alvenaria:.2f}\nMetragem total: {metragem_total_alvenaria}M\nValor total = R${total_alvenaria:.2f}'

def calcular_estrutura_metalica():
    nome_do_cliente = input('Qual o nome do cliente ou empresa?\n')
    valor_metragem_estrutura_metalica = float(input('Qual o valor da metragem para a estrutura metalica?\n->R$'))
    metragem_total_estrutura_metalica = float(input('Qual a metragem total da aréa para a estrutura metalica?\n->'))
    total_metalica = valor_metragem_estrutura_metalica * metragem_total_estrutura_metalica

    try:
        with open('Orçamento_estrutura_metalica.json', 'r', encoding='utf-8') as arquivo_estrutura_metalica:
            lista_geral_estrutura_metalica = json.load*arquivo_estrutura_metalica
            print(lista_geral_estrutura_metalica)

    except FileNotFoundError:
        lista_geral_estrutura_metalica = []

    lista_geral_estrutura_metalica.append({
        'Nome do cliente/empresa': nome_do_cliente,
        'Valor da metragem': valor_metragem_estrutura_metalica,
        'Metragem total': metragem_total_estrutura_metalica,
        'Valor final do orçamento': total_metalica,
    })

    with open('Orçamentos_estruturas_metalica.json', 'w', encoding='utf-8') as arquivo_estrutura:
        json.dump(lista_geral_estrutura_metalica, arquivo_estrutura, ensure_ascii=False, indent=6)

    return f'Nome do cliente: {nome_do_cliente}\nValor per metragem: R${valor_metragem_estrutura_metalica:.2f}\nMetragem total: {metragem_total_estrutura_metalica}M\nValor total = R${total_metalica:.2f}'

def visualizar_orçamentos_recentes():
    selecionando_orçamento = int(input('Qual categoria deseja visualizar?\n->1 - Pintura\n->2 - Gradils\n->3 - Alvenaria\n->4 - Estrutura metalica\n-'))

    if selecionando_orçamento == 1:
        print('Categoria de: pinturas selecionado!!')

        with open('Orçamentos_pinturas.json', 'r', encoding='utf-8') as arquivo_pinturas:
            lista_geral = json.load(arquivo_pinturas)
            return lista_geral


while True: 
    print('1 - Calcular orçamento -> Pintura.\n2 - Calcular orçamento -> Gradil.\n3 - Calcular orçamento -> alvenaria.\n4 - Calcular orçamento -> estrutura metalica.\n5 - Visualizar orçamentos recentes\n6 - Sair do menu de interação.')
    menu_de_interação = int(input('Qual opção do menu deseja acessar?\n'))
    
    if menu_de_interação == 1:
        pintura = calcular_pintura()
        print(pintura)

    elif menu_de_interação == 2:
        gradil = calcular_gradil()
        print(gradil)

    elif menu_de_interação == 3:
        alvenaria = calcular_alvenaria()
        print(alvenaria)

    elif menu_de_interação == 4:
        estrutura_metalica = calcular_estrutura_metalica()
        print(estrutura_metalica)

    elif menu_de_interação == 5:
        visualizar_orçamentos_recentes()

    elif menu_de_interação == 6:
        print('Saindo do menu de interação imediatamente....')
        break