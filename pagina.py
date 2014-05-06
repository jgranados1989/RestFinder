from flask import Flask, render_template, request, url_for
import restaurantes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/agregarPlatillo',methods=['POST'])
def agregarPlatillo():
	rest=request.form['restPlatillo']
	nombrePlat=request.form['nombrePlatillo']
	sabor=request.form['saborPlatillo']
	PaisOrg=request.form['paisPlatillo']
	Ingredientes=request.form['ingredientesPlatillo']
	Ingredientes=str(Ingredientes).split()
	ing="["
	for i in Ingredientes:
		ing+=i+','
	largo=len(ing)
	ing=ing[:largo-1]
	ing+="]"
	lista=restaurantes.buscaRestaurantesXNombre(rest)
	if len(lista)==0:
		return render_template("resConsulta.html",entradas=['El restaurante que digitaste no ha sido ingresado anteriormente','Los platillos deben pertener a un restautante registrado con anterioridad'])
	else:
		restaurantes.agregarPlatillo(str(rest).lower(),str(nombrePlat).lower(),str(sabor).lower(),str(PaisOrg).lower(),ing.lower())
		return render_template("resConsulta.html",entradas=['Platillo agregado exitosamente'])

@app.route('/agregarRestaurante',methods=['POST'])
def agregarRestaurante():
	nombreRest=request.form['nombreRest']
	tipoComida=request.form['tipoComida']
	ubicacionrest=request.form['ubicacionrest']
	numeroRest=request.form['numeroRest']
	horarioRest=request.form['horarioRest']
	restaurantes.agregarRest(str(nombreRest).lower(),str(tipoComida).lower(),str(ubicacionrest).lower(),str(numeroRest).lower(),str(horarioRest).lower())
	return render_template("resConsulta.html",entradas=['Restaurante agregado exitosamente'])

@app.route('/todosRestaurantes',methods=['POST'])
def todosRestaurantes():
	lista=restaurantes.imprimirRest()
	if len(lista)>0:
		return render_template("resConsulta.html",entradas=lista)
	else:
		return render_template("resConsulta.html",entradas=["No hay resultados"])

@app.route('/consultaTipo',methods=['POST'])
def consultaTipo():
	tipocomida=request.form['tipoComida']
	lista=restaurantes.restaurantesXtipo(tipocomida.lower())
	if len(lista)>0:
		return render_template("resConsulta.html",entradas=lista)
	else:
		return render_template("resConsulta.html",entradas=["No hay resultados"])

@app.route('/consultaNombreRest',methods=['POST'])
def consultaNombreRest():
	nombre=request.form['nombreRest']
	lista=restaurantes.buscaRestaurantesXNombre(nombre.lower())
	if len(lista)>0:
		return render_template("resConsulta.html",entradas=lista)
	else:
		return render_template("resConsulta.html",entradas=["No hay resultados"])

@app.route('/consultaPaisPlatillo',methods=['POST'])
def consultaPaisPlatillo():
	pais=request.form['paisPlatillo']
	lista=restaurantes.buscaRestaurantesXPais(pais.lower())
	if len(lista)>0:
		return render_template("resConsulta.html",entradas=lista)
	else:
		return render_template("resConsulta.html",entradas=["No hay resultados"])

@app.route('/consultaRestPlatillos',methods=['POST'])
def consultaRestPlatillos():
	restaurante=request.form['RestaurantePlatillos']
	lista=restaurantes.buscaPlatillosRest(restaurante.lower())
	if len(lista)>0:
		return render_template("resConsulta.html",entradas=lista)
	else:
		return render_template("resConsulta.html",entradas=["No hay resultados"])

@app.route('/consultaRestIngrediente',methods=['POST'])
def consultaRestIngrediente():
	rest=request.form['RestxIngrediente']
	ingrediente=request.form['ingredienteRest']
	lista=restaurantes.platillosXrestIngrediente(rest.lower(),ingrediente.lower())
	if len(lista)>1:
		return render_template("resConsulta.html",entradas=lista)
	else:
		return render_template("resConsulta.html",entradas=["No hay resultados"])


if __name__ == '__main__':
    app.run(debug=False,host="192.168.1.103",port=9090)
