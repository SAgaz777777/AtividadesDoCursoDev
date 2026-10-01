altura1 = float(input("Digite a altura da primeira pessoa (m): "))
altura2 = float(input("Digite a altura da segunda pessoa (m): "))

if altura1 > altura2:
    print("A primeira pessoa é mais alta.")
elif altura2 > altura1:
    print("A segunda pessoa é mais alta.")
else:
    print("Ambas as pessoas têm a mesma altura.")