x = input("Digite um número: ")
y = input("Digite um segundo número: ")
z = input("Digite um terceiro número: ")

if x > y and y > z:
   print("Maior deles é: " + x + " E menor deles é: " + z)
elif y > z and z > x:
    print("Maior deles é: " + y + " E o menor deles é: " + x) 

elif z > x and x > y:
    print("Maior deles é: " + z + " E o menor deles é: " + y)

elif x < y and y > z:
    print("O maior deles é: " + y + " E o menor deles é " + z)

