#Calculo de Média 

'''n1 = float(input("Qual sua nota do 1 bimestre? "))
n2 = float(input("Qual sua nota do 2 bimestre? "))
n3 = float(input("Qual sua nota do 3 bimestre? "))

media = (n1+n2+n3) / 3
print("A média da sua nota é:",media)
if media >= 7:
    print("Você foi aprovado!")
elif media <= 6.9:
    print("Você ficou de recuperação!")
else:
    print("Você foi reprovado!")'''

'''n1 = float(input("Qual sua nota do 1 bimestre? "))
n2 = float(input("Qual sua nota do 2 bimestre? "))
n3 = float(input("Qual sua nota do 3 bimestre? "))

media = (n1+n2+n3) / 3
if media >= 7:
    print(f"Você foi aprovado! Tirou: {media}")
elif media <= 6.9:
    print(f"Você ficou de recuperação! Tirou: {media}")
else:
    print(f"Você foi reprovado! Tirou: {media}")'''

n1 = float(input("Qual sua nota do 1 bimestre? "))
n2 = float(input("Qual sua nota do 2 bimestre? "))
n3 = float(input("Qual sua nota do 3 bimestre? "))
n4 = float(input("Qual sua nota do 4 bimestre? "))

media = (n1+n2+n3+n4) / 4
if media >= 7:
    print(f"Você foi aprovado! Você tirou: {media:.2f}")
elif 5<= media <= 6.9:
    print(f"Você ficou de recuperação! Você tirou: {media:.2f}")
else:
    print(f"Você foi reprovado! Você tirou: {media:.2f}")
