def calcular_media (numeros):
    if not numeros:
        return 0
    soma = sum(numeros)
    media = soma / len (numeros)
    return media
    
# Teste da função
numeros = [10, 20, 30, 40, 50]
print(f"A média é: {calcular_media (numeros)}")

