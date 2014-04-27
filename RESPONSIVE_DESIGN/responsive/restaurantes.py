from pyswip import *

p=Prolog()
#p.consult("rest.pl") #El consult lo que hace es carga el archivo .pl con todas las reglas
#p.consult("plati.pl")

'''
Lista de restaurantes
'''
def imprimirRest():
	p.consult("rest.pl")
	for i in p.query("restaurante(A,_,_,_,_)"): #hago una consulta e imprimo todos los que cumplen la consulta
		print i["A"]
	print "========== Fin de restaurantes =========="

'''
Lista de platillos
'''
def imprimirPlato():
	p.consult("plati.pl")
	for plato in p.query("platillo(_,A,_,_,_)"):
		print plato["A"]
	print "========== Fin de platillos =========="

'''
Lista de restaurantes filtrados por tipo de comida
Entradas: tipo de comida a buscar (comidaRapida,comidaGourmet,pizzeria,etc)
'''
def restaurantesXtipo(tipocomida):
	p.consult("rest.pl")
	print ("Restaurantes que venden "+tipocomida+":")
	for restaurante in p.query("restaurantesXtipo(A,"+tipocomida+")"):
		print restaurante["A"]
	print "========== Fin de consulta =========="

'''
Busqueda de restaurantes por nombre	
Entradas: nombre del restaurante
'''
def buscaRestaurantesXNombre(nombre):
	p.consult("rest.pl")
	print ("Informacion de restaurantes llamados "+nombre+":")
	for restaurante in p.query("buscaRest("+nombre+",A,B,C,D)"):
		print "Tipo comida: " +restaurante["A"]
		print "Ubicacion: "+restaurante["B"]
		print 'Telefono: '+str(restaurante["C"])
		print "Jornada: "+restaurante["D"]
		print "========== Fin de restaurante =========="
	print "========== Fin de consulta =========="

'''
Lista de restaurantes que tienen platillos de algun pais especifico
Entradas: pais a buscar
'''
def buscaRestaurantesXPais(pais):
	p.consult("plati.pl")
	print ("Restaurantes con platillos cuyo pais de origen es "+pais+":")
	for restaurante in p.query("buscaRestXPais(Nombre,"+pais+")"):
		print "Nombre: " +restaurante["Nombre"]
	print "========== Fin de consulta =========="

'''
Lista de platillos de un restaurante especifico	
Entradas: nombre del restaurante a buscar
'''
def buscaPlatillosRest(restaurante):
	p.consult("plati.pl")
	print ("Platillos de:"+restaurante+":")
	for restaurante in p.query("platillosXrest("+restaurante+",Nombre,Sabor,Pais,Ingredientes)"):
		print "Nombre: " +restaurante["Nombre"]
		print "Sabor: " +restaurante["Sabor"]
		print "Pais de origen: " +restaurante["Pais"]
		print "Ingredientes: "
		for i in list(restaurante["Ingredientes"]):
			print i
		print "========== Fin de platillo =========="
	print "========== Fin de consulta =========="

'''
Lista de platillos de un restaurante especifico que tengan un ingrediente en particular
Entradas: nombre del restaurante y el ingrediente que se desea buscar
'''
def platillosXrestIngrediente(restaurante,ingrediente):
	p.consult("plati.pl")
	print ("Lista de platillos de "+restaurante+" que incluyen "+ingrediente+":")
	#platillosXrestIngrediente(X,Nombre,Sabor,Pais,Y)
	for restaurante in p.query("platillosXrestIngrediente("+restaurante+",Nombre,Sabor,Pais,"+ingrediente+")"):
		print restaurante["Nombre"]
	print "========== Fin de consulta =========="

'''
Agrega un restaurante a la base de conocimientos
'''
def agregarRest(nombre,tipoComida,ubicacion,telefono,horario):
	arch = file("rest.pl","a")
	functor="\nrestaurante("
	functor=functor+nombre+","+tipoComida+","+ubicacion+","+telefono+","+horario+")."
	arch.write(functor)
	#p.assertz("'"+functor+"'") #con esto carga las varas a la base de conocimientos

'''
Agrega un platillo a la base de conocimientos
'''
def agregarPlatillo(rest,nombrePlat,sabor,PaisOrg,Ingredientes): #sabor puede ser picante, salado, dulce, agridulce, amargo
	arch = file("plati.pl","a")
	functor="\nplatillo("
	functor=functor+rest+","+nombrePlat+","+sabor+","+PaisOrg+","+Ingredientes+")." #Ingredientes por ahora lo agrego como si fuera una lista de python, creo que en prolog el manejo es algo similar
	arch.write(functor)
	#p.assertz("'"+functor+"'") #con esto carga las varas a la base de conocimientos

'''
Funcion de ejecucion de pruebas
'''
def pruebas():
	agregarRest("mC","hamburguesas","cartago","25354545","tod_el_dia")
	#imprimirRest()
	#restaurantesXtipo("comidaRapida")
	#restaurantesXtipo("comidaGourmet")
	#buscaRestaurantesXNombre("mcDonalds")
	#buscaRestaurantesXPais("alemania")
	#buscaPlatillosRest("bk")
	#platillosXrestIngrediente("bk","pan")
	#platillosXrestIngrediente("mcDonadls","carne")

#pruebas()
