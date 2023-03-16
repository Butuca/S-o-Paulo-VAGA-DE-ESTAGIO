string = 'Ola Mundo'
stringInvertida = ''

#Percorre a String de trás para frente
for i in range(len(string)-1,-1,-1):
    #atribui os caracteres para a nova String
    stringInvertida += string[i]

print(stringInvertida)
