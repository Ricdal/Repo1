import random

caracteres = '!#"$%&/()=?¡'
caracter1 = random.choice(caracteres)
caracter2 = random.choice(caracteres)
caracter3 = random.choice(caracteres)
caracter4 = random.choice(caracteres)
i = 0
frase = input("Introduce una frase secreta para tu contraseña\n")

convert_fras_min = frase.casefold()
convert_may_prim_letra = convert_fras_min.title()

num_mayus = len([c for c in convert_may_prim_letra if c.isupper()])
frase_sin_espacios = frase.replace(" ", "")

while(i==0):
  if(len(frase_sin_espacios)<6 or len(frase_sin_espacios)>50):
    frase = input("\nDebe contener entre 6 y 50 carcateres. Intenta otra.\n")
  elif(num_mayus<4 or num_mayus>10):
    frase = input("\nLa frase debe contener entre 4 y 10 palabras\n")
    convert_fras_min = frase.casefold()
    convert_may_prim_letra = convert_fras_min.title()
    num_mayus = len([c for c in convert_may_prim_letra if c.isupper()])
  else:
    i+=1
    
frase_cambiada = frase.replace("A", "4" )
frase_cambiada = frase_cambiada.replace("a", "4" )
frase_cambiada = frase_cambiada.replace("E", "3" )
frase_cambiada = frase_cambiada.replace("e", "3" )
frase_cambiada = frase_cambiada.replace("I", "1" )
frase_cambiada = frase_cambiada.replace("i", "1" )
frase_cambiada = frase_cambiada.replace("O", "0" )
frase_cambiada = frase_cambiada.replace("o", "0" )
frase_cambiada = frase_cambiada.replace("t", "7" )
frase_cambiada = frase_cambiada.replace("T", "7" )
frase_cambiada = frase_cambiada.replace("B", "8" )
frase_cambiada = frase_cambiada.replace("b", "8" )
frase_cambiada = frase_cambiada.replace(" ", "")
frase_cambiada = (caracter1 + caracter2 + frase_cambiada + caracter3 + caracter4)
print("Tu contraseña es: " + frase_cambiada)
