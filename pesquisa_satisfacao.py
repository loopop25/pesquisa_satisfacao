TOTAL_ENTREVISTADOS = 10

qtd_excelente = 0
qtd_ruim = 0

print("--- PESQUISA DE SATISFAÇÃO TUDOWEB ---")

for i in range(TOTAL_ENTREVISTADOS):
    print(f"\nEntrevistado {i + 1}:")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opcao = int(input("Digite sua opção (1, 2 ou 3): "))
    
    if opcao == 1:
        qtd_excelente = qtd_excelente + 1
    elif opcao == 3:
        qtd_ruim = qtd_ruim + 1

print("\n--- RESULTADO FINAL ---")
print("a) Quantidade de respostas EXCELENTE:", qtd_excelente)
print("b) Quantidade de respostas RUIM:", qtd_ruim)