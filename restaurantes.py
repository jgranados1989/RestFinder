from pyswip import *
from ctypes import *
from pyswip.prolog import Prolog

p=Prolog()
p.consult("rest.pl") #El consult lo que hace es carga el archivo .pl con todas las reglas
p.consult("plati.pl")

'''
Lista de restaurantes
'''
def imprimirRest():
	p=Prolog()
	p.consult('rest.pl')
	resultados=[]
	for result in p.query("restaurante(A,_,_,_,_)"):
		r=result["A"]
		resultados.append(str(r))
	log = file("log.txt","a")
	log.write(str(resultados)+"\n")
	log.close()
	return resultados

'''
Lista de platillos
'''
def imprimirPlato():
	p=Prolog()
	p.consult("plati.pl")
	resultados=[]
	for plato in p.query("platillo(_,A,_,_,_)"):
		r=plato["A"]
		resultados.append(str(r))
	log = file("log.txt","a")
	log.write(str(resultados)+"\n")
	log.close()
	return resultados

'''
Lista de restaurantes filtrados por tipo de comida
Entradas: tipo de comida a buscar (comidaRapida,comidaGourmet,pizzeria,etc)
'''
def restaurantesXtipo(tipocomida):
	p=Prolog()
	p.consult("rest.pl")
	resultados=[]
	for restaurante in p.query("restaurantesXtipo(A,"+tipocomida+")"):
		r=restaurante["A"]
		resultados.append(str(r))
	log = file("log.txt","a")
	log.write(str(resultados)+"\n")
	log.close()
	return resultados

'''
Busqueda de restaurantes por nombre	
Entradas: nombre del restaurante
'''
def buscaRestaurantesXNombre(nombre):
	p=Prolog()
	p.consult("rest.pl")
	resultados=[]
	for restaurante in p.query("buscaRest("+nombre+",A,B,C,D)"):
		temporal=[]
		tipo=restaurante["A"]
		ubicacion=restaurante["B"]
		telefono=str(restaurante["C"])
		jornada=restaurante["D"]
		temporal.append(str(tipo))
		temporal.append(str(ubicacion))
		temporal.append(str(telefono))
		temporal.append(str(jornada))
		temporal.append("Fin de restaurante")
		resultados.append(temporal)
		temporal=[]
	log = file("log.txt","a")
	log.write(str(resultados)+"\n")
	log.close()
	return resultados

'''
Lista de restaurantes que tienen platillos de algun pais especifico
Entradas: pais a buscar
'''
def buscaRestaurantesXPais(pais):
	p=Prolog()
	p.consult("plati.pl")
	resultados=[]
	for restaurante in p.query("buscaRestXPais(Nombre,"+pais+")"):
		r=restaurante["Nombre"]
		resultados.append(str(r))
	log = file("log.txt","a")
	log.write(str(resultados)+"\n")
	log.close()
	return resultados

'''
Lista de platillos de un restaurante especifico	
Entradas: nombre del restaurante a buscar
'''
def buscaPlatillosRest(restaurante):
	p=Prolog()
	p.consult("plati.pl")
	resultados=[]
	for restaurante in p.query("platillosXrest("+restaurante+",Nombre,Sabor,Pais,Ingredientes)"):
		temporal=[]
		temporal.append("Nombre: "+str(restaurante["Nombre"]))
		temporal.append("Sabor: "+str(restaurante["Sabor"]))
		temporal.append("Pais de origen: " +restaurante["Pais"])
		t=""
		for i in list(restaurante["Ingredientes"]):
			t+=str(i)+" - "
		temporal.append(str("Ingredientes: "+t))
		t=""
		resultados.append(temporal)
		temporal=[]
	log = file("log.txt","a")
	log.write(str(resultados)+"\n")
	log.close()
	return resultados

'''
Lista de platillos de un restaurante especifico que tengan un ingrediente en particular
Entradas: nombre del restaurante y el ingrediente que se desea buscar
'''
def platillosXrestIngrediente(restaurante,ingrediente):
	p=Prolog()
	p.consult("plati.pl")
	resultados=[]
	resultados.append("Lista de platillos de "+restaurante+" que incluyen "+ingrediente+":")
	for restaurante in p.query("platillosXrestIngrediente("+restaurante+",Nombre,Sabor,Pais,"+ingrediente+")"):
		resultados.append(restaurante["Nombre"])
	log = file("log.txt","a")
	log.write(str(resultados)+"\n")
	log.close()
	return resultados

'''
Agrega un restaurante a la base de conocimientos
'''
def agregarRest(nombre,tipoComida,ubicacion,telefono,horario):
	arch = file("rest.pl","a")
	arch.write('\n')
	functor="restaurante("
	functor=functor+nombre+","+tipoComida+","+ubicacion+","+telefono+","+horario+")."
	arch.write(functor)
	p.assertz("'"+functor+"'") #con esto carga las varas a la base de conocimientos

'''
Agrega un platillo a la base de conocimientos
'''
def agregarPlatillo(rest,nombrePlat,sabor,PaisOrg,Ingredientes): #sabor puede ser picante, salado, dulce, agridulce, amargo
	arch = file("plati.pl","a")
	arch.write('\n')
	functor="platillo("
	functor=functor+rest+","+nombrePlat+","+sabor+","+PaisOrg+","+Ingredientes+")." #Ingredientes por ahora lo agrego como si fuera una lista de python, creo que en prolog el manejo es algo similar
	arch.write(functor)
	p.assertz("'"+functor+"'") #con esto carga las varas a la base de conocimientos

'''
Funcion de ejecucion de pruebas
'''

#imprimirRest()
#imprimirPlato()
#restaurantesXtipo("comidaRapida")
#buscaRestaurantesXNombre("mcDonalds")
#buscaRestaurantesXPais("alemania")
#buscaPlatillosRest("bk")
