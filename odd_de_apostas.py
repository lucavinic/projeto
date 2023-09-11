print('\t ---Aposta Esportiva---') 
#precisa saber o valor da odd
odd = float(input("Qual a odd do time que você quer apostar? "))

#quanto já gastou em outra aposta
gasto = float(input("Qual valor já foi gasto em outra aposta? "))

#conta para saber qual valor investir para não sair perdendo
investimento = (2 * gasto) / odd

#conta de lucro
lucro = (investimento * odd) - gasto

print("O valor ideal para apostar e lucrar, tendo em vista que já fez uma outra aposta de", gasto, "é de", f"{investimento:.2f}.","Onde terá um lucro de", lucro)