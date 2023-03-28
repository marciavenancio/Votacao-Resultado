print ("Votação para o dia das Lives")
segunda_feira = int(input("Insira a quantidade de votos as Lives de Segunda-feira obtiveram: "))
terca_feira = int(input("Insira a quantidade de votos as Lives de Terça-feira obtiveram: "))
quarta_feira = int(input("Insira a quantidade de votos as Lives de Quarta-feira obtiveram: "))
quinta_feira =  int(input("Insira a quantidade de votos as Lives de Quinta-feira obtiveram: "))
sexta_feira = int(input("Insira a quantidade de votos as Lives de Sexta-feira obtiveram: "))

if segunda_feira > terca_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira:
    print ("\nO dia escolhido para as Lives foi Segunda-feira!")
elif terca_feira > segunda_feira and terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > sexta_feira:
        print("\nO dia escolhido para as Lives foi Terça-feira!")
elif quarta_feira > segunda_feira and quarta_feira > terca_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira:
    print("\nO dia escolhido para as Lives foi Quarta-feira!")
elif quinta_feira > segunda_feira and quinta_feira > terca_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira:
    print("\nO dia escolhido para as Lives foi Quinta-feira!")
elif sexta_feira > segunda_feira and sexta_feira > terca_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira:
    print("\nO dia escolhido para as Lives foi Sexta-feira!")

else:
    print("\n Houve empate. Em breve faremos uma nova votação para decidir entre as datas mais votadas! ")