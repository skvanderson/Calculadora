def calculadora(num1, num2, operacao):
    if operacao == 1:
        solucao = num1 + num2
    elif operacao == 2:
        solucao = num1 - num2
    elif operacao == 3:
        solucao = num1 * num2
    elif operacao == 4:
        if num2 != 0: 
            solucao = num1 / num2
        else:
            solucao = 0  
    else:
        solucao = 0  
    return solucao

opcao_1 = 25
opcao_2 = 18
operacao = 1
solucao = calculadora(opcao_1, opcao_2, operacao)
print("Solucão da Operacão é --->", solucao)
