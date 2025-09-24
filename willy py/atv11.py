nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade: "))

if idade <2: 
    print (nome,"esta com",idade,"anos e pela tabela e considerado um bebe")
 
elif idade >2:
    print (nome," esta com",idade,"anos e pela tabela e considerado uma crianca ") 

elif idade >12:
    print (nome," esta com",idade,"anos e pela tabela e considerado uma jovem ") 

elif idade >22:
    print (nome," esta com",idade,"anos e pela tabela e considerado uma adulto ") 

elif idade >65:
    print (nome," esta com",idade,"anos e pela tabela e considerado uma idoso ") 

else :
    print("muito velinho")   