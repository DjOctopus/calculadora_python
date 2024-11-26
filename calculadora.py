# Definição das funções para cada operação básica
def adicionar(x, y):
    # Função para adicionar dois números
    return x + y

def subtrair(x, y):
    # Função para subtrair o segundo número do primeiro
    return x - y

def multiplicar(x, y):
    # Função para multiplicar dois números
    return x * y

def dividir(x, y):
    # Função para dividir o primeiro número pelo segundo, com verificação de divisão por zero
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"

# Função principal que gera o menu e executa as operações
def calculadora():
    # Exibe as opções de operação para o usuário
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Solicita ao usuário para escolher uma operação
    escolha = input("Digite sua escolha (1/2/3/4): ")

    # Solicita ao usuário para digitar os dois números para a operação
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Verifica qual operação foi escolhida e executa a função correspondente
    if escolha == '1':
        print("Resultado: ", adicionar(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtrair(num1, num2))
    elif escolha == '3':
        print("Resultado: ", multiplicar(num1, num2))
    elif escolha == '4':
        print("Resultado: ", dividir(num1, num2))
    else:
        # Caso o usuário digite uma opção inválida
        print("Opção inválida")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa
    calculadora()
