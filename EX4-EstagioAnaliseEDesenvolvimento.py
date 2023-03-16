sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
out = 19849.53
#CALCULA O VALOR TOTAL SOMADO POR TODOS OS ESTADOS
total = sp + rj + mg + es + out

#ATRIBUI A PORCENTAGEM FAZENDO UMA CONTA SIMPLES: O VALOR DE CADA ESTADO DIVIDIDO PELO TOTAL
porcentagem_sp = (sp / total) * 100
porcentagem_rj = (rj / total) * 100
porcentagem_mg = (mg / total) * 100
porcentagem_es = (es / total) * 100
porcentagem_ou = (out / total) * 100

#EXIBE OS VALORES
print("Porcentagem de SP: ", round(porcentagem_sp), '%')
print("Porcentagem de RJ: ", round(porcentagem_rj), '%')
print("Porcentagem de ES: ", round(porcentagem_mg), '%')
print("Porcentagem de MG: ", round(porcentagem_es), '%')
print("Porcentagem de Outros: ", round(porcentagem_ou), '%')