from pyswip import *

p=Prolog()
p.consult("rest.pl") #El consult lo que hace es carga el archivo .pl con todas las reglas
#p.consult("plati.pl")


def generator_to_list(function):
    def wrapper(*args, **kwargs):
        return list(function(*args, **kwargs))
    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper

'''
Lista de restaurantes
'''
def imprimirRest():
	resultados=[]
	i=p.query("restaurante(A,_,_,_,_)")
	#for i in p.query("restaurante(A,_,_,_,_)"): #hago una consulta e imprimo todos los que cumplen la consulta
	#	resultados.append(str(i["A"]))
	#print resultados
	return i

'''
Lista de platillos
'''
def imprimirPlato():
	p.consult("plati.pl")
	resultados=[]
	for plato in p.query("platillo(_,A,_,_,_)"):
		resultados.append(str(plato["A"]))
		#print plato["A"]
	print resultados
	print "========== Fin de platillos =========="
	return resultados

'''
Lista de restaurantes filtrados por tipo de comida
Entradas: tipo de comida a buscar (comidaRapida,comidaGourmet,pizzeria,etc)
'''
def restaurantesXtipo(tipocomida):
	p.consult("rest.pl")
	resultados=[]
	print ("Restaurantes que venden "+tipocomida+":")
	for restaurante in p.query("restaurantesXtipo(A,"+tipocomida+")"):
		resultados.append(str(restaurante["A"]))
		#print restaurante["A"]
	print resultados
	print "========== Fin de consulta =========="
	return resultados

'''
Busqueda de restaurantes por nombre	
Entradas: nombre del restaurante
'''
def buscaRestaurantesXNombre(nombre):
	p.consult("rest.pl")
	resultados=[]
	print ("Informacion de restaurantes llamados "+nombre+":")
	for restaurante in p.query("buscaRest("+nombre+",A,B,C,D)"):
		temporal=[]
		temporal.append("Tipo comida: " +restaurante["A"])
		temporal.append("Ubicacion: "+restaurante["B"])
		temporal.append('Telefono: '+str(restaurante["C"]))
		temporal.append("Jornada: "+restaurante["D"])
		temporal.append("========== Fin de restaurante ==========")
		resultados.append(temporal)
		temporal=[]
	print resultados
	print "========== Fin de consulta =========="
	return resultados

'''
Lista de restaurantes que tienen platillos de algun pais especifico
Entradas: pais a buscar
'''
def buscaRestaurantesXPais(pais):
	p.consult("plati.pl")
	resultados=[]
	print ("Restaurantes con platillos cuyo pais de origen es "+pais+":")
	for restaurante in p.query("buscaRestXPais(Nombre,"+pais+")"):
		#print "Nombre: " +restaurante["Nombre"]
		resultados.append("Nombre: " +restaurante["Nombre"])
	print resultados
	print "========== Fin de consulta =========="
	return resultados

'''
Lista de platillos de un restaurante especifico	
Entradas: nombre del restaurante a buscar
'''
def buscaPlatillosRest(restaurante):
	p.consult("plati.pl")
	resultados=[]
	print ("Platillos de:"+restaurante+":")
	for restaurante in p.query("platillosXrest("+restaurante+",Nombre,Sabor,Pais,Ingredientes)"):
		temporal=[]
		temporal.append("Nombre: " +restaurante["Nombre"])
		temporal.append("Sabor: " +restaurante["Sabor"])
		temporal.append("Pais de origen: " +restaurante["Pais"])
		temporal.append(["Ingredientes: "]+list(restaurante["Ingredientes"]))
		#temporal.append(restaurante["Ingredientes"])
		#for i in list(restaurante["Ingredientes"]):
		#	print i
		temporal.append("========== Fin de platillo ==========")
		resultados.append(temporal)
		temporal=[]
	print resultados
	print "========== Fin de consulta =========="
	return resultados

'''
Lista de platillos de un restaurante especifico que tengan un ingrediente en particular
Entradas: nombre del restaurante y el ingrediente que se desea buscar
'''
def platillosXrestIngrediente(restaurante,ingrediente):
	p.consult("plati.pl")
	resultados=[]
	resultados.append("Lista de platillos de "+restaurante+" que incluyen "+ingrediente+":")
	#platillosXrestIngrediente(X,Nombre,Sabor,Pais,Y)
	for restaurante in p.query("platillosXrestIngrediente("+restaurante+",Nombre,Sabor,Pais,"+ingrediente+")"):
		resultados.append(restaurante["Nombre"])
	print resultados
	print "========== Fin de consulta =========="
	return resultados

'''
Agrega un restaurante a la base de conocimientos
'''
def agregarRest(nombre,tipoComida,ubicacion,telefono,horario):
	arch = file("rest.pl","a")
	functor="restaurante("
	functor=functor+nombre+","+tipoComida+","+ubicacion+","+telefono+","+horario+")."
	arch.write(functor)
	p.assertz("'"+functor+"'") #con esto carga las varas a la base de conocimientos

'''
Agrega un platillo a la base de conocimientos
'''
def agregarPlatillo(rest,nombrePlat,sabor,PaisOrg,Ingredientes): #sabor puede ser picante, salado, dulce, agridulce, amargo
	arch = file("plati.pl","a")
	functor="platillo("
	functor=functor+rest+","+nombrePlat+","+sabor+","+PaisOrg+","+Ingredientes+")." #Ingredientes por ahora lo agrego como si fuera una lista de python, creo que en prolog el manejo es algo similar
	arch.write(functor)
	p.assertz("'"+functor+"'") #con esto carga las varas a la base de conocimientos

'''
Funcion de ejecucion de pruebas
'''

imprimirRest()
