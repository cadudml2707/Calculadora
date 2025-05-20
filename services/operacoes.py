def soma(num: float, num2: float):
    return num+num2

def subtracao(num: float, num2: float):
    return num-num2

def multiplicacao(num: float, num2: float):
    return num*num2

def divisao(num: float, num2: float):
    if num == 0 or num2 == 0:
        return 'Resultado inexistente'
    else:
        return num/num2

def calculate(tipo: str, num: float, num2: float):  
    if tipo == 'soma':
        return soma(num, num2)
    elif tipo == 'divisão':
        return divisao(num, num2)
    elif tipo == 'multiplicação':
        return multiplicacao(num, num2)
    elif tipo == 'subtração':
        return subtracao(num, num2)
    else:
        return 'Dados inválidos!'