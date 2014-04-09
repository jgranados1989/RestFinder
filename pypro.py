from pyswip import *

p=Prolog()
p.consult("saludos.pl") #El consult lo que hace es carga el archivo .pl con todas las reglas
def imprimir():
	p.consult("saludos.pl")
	for i in p.query("saludo(X)"): #hago una consulta e imprimo todos los que cumplen la consulta
		print i["X"]

def agregar(saludo): #Agrega un nuevo saludo al archivo saludos.pl, carga el archivo, pero no se carga en la base de conocimientos
	arch = file("saludos.pl","a")
	functor="\nsaludo("
	functor=functor+saludo+")."
	arch.write(functor)
