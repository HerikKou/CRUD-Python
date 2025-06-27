import json;
def CarregarDados():
   try:
        with open("CRUD.json","r") as arquivo:
             return json.load(arquivo)
   except FileNotFoundError:
        return []

def salvar_dados(lista):
    with open("cadastros.json", "w") as arquivo:
        json.dump(lista, arquivo, indent=4)       
cadastro =CarregarDados()


while True:
    print("""
        -----Menu----

        1-Cadastrar
        2-Buscar por nome
        3-listarTudo
        4-excluir 
        5-sair

""")
    op = int (input("Escolha sua opção:"))
    match op:

        case 1:
            nome = input("digite seu nome:")
            idade = int(input("digite sua idade:"))
            email = input("digite seu email:")
            
            if  "@gmail.com" not in email:
                print("Email inválido")
                continue
              
            

            cadastro.append((nome,idade,email))
            salvar_dados(cadastro)
            print("Cadastrado com sucesso")
                
        case 2:
            if not cadastro:
                 print("Nenhuma pesssoa cadastrada")
                 continue
            nome = input("digite o nome da pessoa:")
            
            for buscar in cadastro:
                    if buscar[0] == nome:
                             print(buscar)
                           
                             salvar_dados(buscar)   
                 
            
        case 3:
              if not cadastro:
                print("Nenhuma pesssoa cadastrada")
                continue
              
              for i in cadastro:
               print(i)
             
               salvar_dados(i)
             
        case 4: 
            if not cadastro:
                 print("Nenhuma pesssoa cadastrada")
                 continue
            nome = input("digite o nome da pessoa:")
            for buscar in cadastro:
                if buscar[0] == nome:
                     cadastro.remove(buscar)
                     print(cadastro)
                    
                     salvar_dados(buscar)
                     print("Pessoa Removida com Sucesso")

                else:
                     print("Erro ao remover a pessoa")     
            
        case 5:
              print("programa encerrado")
              break
        case _: 
              print("Opção inválida")     
  
   
      