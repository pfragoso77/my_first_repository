
#definição de função para adicionar personagens
def adicionar_personagem(lista_personagens):
    nome = input('Insira o nome da personagem: ')
    idade = int(input('Insira a idade da personagem: '))
    profissão = input('Insira a profissão da personagem: ')
    hobbies = input('Insira os hobbies da personagem, dividos por vírgula: ').split(",")
    descrição = input('Insira uma breve descrição da personagem: ')
    personagem = {'nome': nome, 'idade': idade, 'profissão': profissão, 'hobbies': hobbies, 'descrição': descrição,}
    lista_personagens.append(personagem)
#definição de função para modificar personagem
def modificar_personagem(lista_personagens):
    nome_personagem = input("Digite o nome da personagem a modificar: ")
    campo_modificar = input("Digite o campo a modificar (nome, idade, profissão, hobbies, descrição): ")
    novo_valor = input("Digite o novo valor para o campo: ")
    for personagem in lista_personagens:
        if personagem["nome"] == nome_personagem:
            personagem[campo_modificar] = novo_valor
            print("Personagem modificado com sucesso!")
            break
    else:
        print("Personagem não encontrado!")
#definição função para remover personagem    
def remover_personagem(lista_personagens):
    nome_personagem = input("Digite o nome da personagem a remover: ")
    for personagem in lista_personagens:
        if personagem["nome"] == nome_personagem:
            lista_personagens.remove(personagem)
            print("Personagem removido com sucesso!")
            break
    else:
        print("Personagem não encontrado!")
#definição função para vizualizar personagens
def visualizar_personagens(lista_personagens):
    for personagem in lista_personagens:
        print("---------------------------")
        print("Nome:", personagem["nome"])
        print("Idade:", personagem["idade"])
        print("Profissão:", personagem["profissão"])
        print("Hobbies:", (personagem["hobbies"]))
        print("Descrição:", personagem["descrição"])
lista_personagens = []
#definição função pesquisar personagens
def pesquisar_personagem(lista_personagens):
    nome_personagem = input("Digite o nome da personagem a pesquisar: ")
    for personagem in lista_personagens:
        if personagem["nome"] == nome_personagem:
           print("Informações da personagem:")
           print("Nome:", personagem["nome"])
           print("Idade:", personagem["idade"])
           print("Profissão:", personagem["profissão"])
           print("Hobbies:", personagem["hobbies"])
           print("Descrição:", personagem["descrição"])
           break
    else:
        print("Personagem não encontrado!")
#Loop que serve de menu       
while True:
    print("1. Adicionar personagem")
    print("2. Modificar personagem")
    print("3. Remover personagem")
    print("4. Visualizar personagens")
    print("5. Pesquisar personagem")
    print("6. Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        adicionar_personagem(lista_personagens)
    elif opcao == 2:
        modificar_personagem(lista_personagens)
    elif opcao == 3:
        remover_personagem(lista_personagens)
    elif opcao == 4:
        visualizar_personagens(lista_personagens)
    elif opcao == 5:
        pesquisar_personagem(lista_personagens)
    elif opcao == 6:
        print("Obrigado, até breve!")
        break
    else:
        print("Opção inválida. Tente novamente.")
