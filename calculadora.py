def calculadora(opcao_1, opcao_2, operacao):
    if operacao == 1:
        solucao = opcao_1 + opcao_2
    elif operacao == 2:
        solucao = opcao_1 - opcao_2
    elif operacao == 3:
        solucao = opcao_1 * opcao_2
    elif operacao == 4:
        if opcao_2 != 0: 
            solucao = opcao_1 / opcao_2
        else:
            solucao = "divisão por zero não permitida!"
    else:
        solucao = "Operação Invalida"
    return solucao

opcao_1 = 18
opcao_2 = 0
operacao = 4 
solucao = calculadora(opcao_1, opcao_2, operacao)
print("Solução da Operação é --->", solucao)
