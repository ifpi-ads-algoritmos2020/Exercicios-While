#Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.
def main():
    limite_inferior = int(input('inferior: '))
    limite_superior = int(input('superior: '))
    for c in range(limite_inferior, limite_superior):
        if c % 2 != 0:
            print(c, end=' ')


main()
