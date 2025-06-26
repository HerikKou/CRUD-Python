cadastro =[]


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
            print("Cadastrado com sucesso")
                
        case 2:
            if not cadastro:
                 print("Nenhuma pesssoa cadastrada")
                 continue
            nome = input("digite o nome da pessoa:")
            
            for buscar in cadastro:
                    if buscar[0] == nome:
                             print(buscar)

                 
            
        case 3:
              if not cadastro:
                print("Nenhuma pesssoa cadastrada")
                continue
              
              for i in cadastro:
               print(i)
             
        case 4: 
            if not cadastro:
                 print("Nenhuma pesssoa cadastrada")
                 continue
            nome = input("digite o nome da pessoa:")
            for buscar in cadastro:
                if buscar[0] == nome:
                     cadastro.remove(buscar)
                     print(cadastro)
                     print("Pessoa Removida com Sucesso")
                else:
                     print("Erro ao remover a pessoa")     
            
        case 5:
              print("programa encerrado")
              break
        case _: 
              print("Opção inválida")     
  
   
      