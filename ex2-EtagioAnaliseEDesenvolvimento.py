# Recebe o número informado pelo usuário
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa as variáveis para calcular a sequência de Fibonacci
anterior = 0
atual = 1
sequencia = [0, 1]

# Loop para calcular a sequência de Fibonacci até encontrar um número maior ou igual ao número informado
while atual < numero:
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    sequencia.append(atual)

# Imprime a sequência de Fibonacci encontrada
print("Sequência de Fibonacci encontrada:")
print(sequencia)

# Verifica se o número informado pertence à sequência de Fibonacci
if atual == numero:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

