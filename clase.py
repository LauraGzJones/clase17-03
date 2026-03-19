#Declaración de variables
nom = ""
ed = 0
correo = ""
# frase = """Esto es un párrafo
# **❌ ERROR GRAVE QUE DEBES EVITAR ABSOLUTAMENTE:**
# **✅ CÓMO HACERLO CORRECTAMENTE EN EL MISMO CASO:**
# puedo escribir todo lo que quiera:"""
# print(frase)


#Entrada
nom = ""; nom = input("Ingrese nombre: ")
ed = input("Su edad: ")
correo = input("Correo electrónico: ")

#Salida
print("Hola", nom, "tienes", ed, "años, tu correo es :", correo)

 #f-string llama a la variable  de igual forma 
 
print (f"Hola {nom} tienes {ed} años, tu correo es : {correo},")

# sep  ARGUMENTO /PARAMETRO
# sirve para definir cómo se separan los valores que imprime print
print(nom, ed, correo, sep="; ",end=";") 

#end sirve  para definir el final del print 
print(f"Hola {nom}\ntienes {ed} años\ntu correo es : {correo}")
#/n caracter de escape q retorna y hace  linea nueva 



