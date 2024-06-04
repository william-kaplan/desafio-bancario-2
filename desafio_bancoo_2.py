def menu():
    menu = """
---------- MENU ----------
    
[d]  - Depositar
[s]  - Sacar
[e]  - Extrato
[nc] - Nova Conta
[lc] - Listar Contas
[nu] - Novo Usuário
[q]  - Sair
    
=>"""

    return input(menu)

def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("\nValor inválido, por favor selecione novamente a operação desejada.")
    else:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}"
        print("\nDepósito realizado com sucesso!\n")
    print("-" * 30)
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saques = numero_saques >= limite_saques
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
          
    if excedeu_saques:
        print(f"\nLimite de saques diários atingido!\n")
    elif excedeu_limite:
        print(f"\nValor de saque acima do limite permitido!\n")
    elif excedeu_saldo:
        print("\nSaldo indiponível!\n")
    elif valor > 0: 
        saldo -= valor 
        numero_saques += 1
        extrato += f"\nSaque: - R$ {valor:.2f}"
        print("\nSaque realizado com sucesso!\n")
    else:
        print("\nValor inválido, por favor selecione novamente a operação desejada.\n")
    print("-" * 27)
    
    return saldo, extrato
        
def exibir_extrato(saldo, /, *, extrato):
    print("---------- Extrato ----------")
    print(extrato)
    print(f"Saldo: R$ {saldo}\n")
    print("-" * 29)
    
def criar_usuario(usuarios):
    print("---------- Criar usuáios ----------")
    cpf = input("\nInforme seu CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nJá existe um usuário cadastrato com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aa): ")
    endereco = input("Informe seu endereço completo (rua, número, bairro, cidade, estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\nUsuário cadastrado com sucesso!\n")
    print("-" * 35)
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    print("---------- Criar conta ----------")
    cpf = input("\nInforme o CPF do usuário: \n")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!\n")
        print("-" * 31)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado!\n")
    print("-" * 31)
    
def listar_contas(contas):
    print("---------- Lista de Contas ----------")
    for conta in contas:
        
        linha = f"""      
Agência: {conta["agencia"]}
Conta: {conta["numero_conta"]}
Títular: {conta["usuario"]["nome"]}         
        """
        
        print(linha)
    print("-" * 37)
        
def main():

    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == "d":
            print("---------- Depósito ----------")
            valor = float(input("\nInforme o valor do depósito: R$ "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
                
        elif opcao == "s":
            print("---------- Sacar ----------")
            valor = float(input("\nInforme o valor do saque: R$ "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE
            )
                
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
                    
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()
