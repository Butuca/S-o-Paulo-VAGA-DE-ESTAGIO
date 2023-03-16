import json
#LEITURA E IMPRESSAO DO dados.json
with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
    for i in dados:
        print(i['dia'], 'Dia:', i['valor'], '.')

#ATRIBUI A VARIAVEL VALOR TODOS OS DIAS ONDE O FATURAMENTO FOI DIFERENTE DE ZERO
valor = [dado['valor'] for dado in dados if dado['valor'] != 0]

# CALCULA A MEDIA
media = sum(valor) / len(valor)

#CALCULA OS DIAS QUE O VALOR DE FATURAMENTO FORAM MAIORES QUE A MEDIA
diasMaiorQueAMedia= valor = [dado['dia'] for dado in dados if dado['valor'] > media]

#CALCULA O MAIOR E MENOR VALOR
menorValor = min(valor)
maiorValor = max(valor)

#EXIBE OS DADOS
print('\nMenor FATURAMENTO: ', menorValor)
print('Maior FATURAMENTO: ', maiorValor)
print('FATURAMENTO Médio: ', media)
print('Dias onde o FATURAMENTO foi maior que a media mensal: ', diasMaiorQueAMedia)


