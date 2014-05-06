from flask import Flask, render_template, request, url_for
import restaurantes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/agregarRestaurante',methods=['POST'])
def agregarRestaurante():
	nombreRest=request.form['nombreRest']
	tipoComida=request.form['tipoComida']
	ubicacionrest=request.form['ubicacionrest']
	numeroRest=request.form['numeroRest']
	horarioRest=request.form['horarioRest']
	restaurantes.agregarRest(str(nombreRest),str(tipoComida),str(ubicacionrest),str(numeroRest),str(horarioRest))
	return render_template("resultados.html",entradas=['Restaurante agregado exitosamente'])

@app.route('/todosRestaurantes',methods=['POST'])
def todosRestaurantes():
	lista=restaurantes.imprimirRest()
	if len(lista)>0:
		return render_template("resultados.html",entradas=lista)
	else:
		return render_template("resultados.html",entradas=["No hay resultados"])

@app.route('/consultaTipo',methods=['POST'])
def consultaTipo():
	tipocomida=request.form['tipoComida']
	lista=restaurantes.restaurantesXtipo(tipocomida)
	if len(lista)>0:
		return render_template("resultados.html",entradas=lista)
	else:
		return render_template("resultados.html",entradas=["No hay resultados"])

@app.route('/consultaNombreRest',methods=['POST'])
def consultaNombreRest():
	nombre=request.form['nombreRest']
	lista=restaurantes.buscaRestaurantesXNombre(nombre)
	if len(lista)>0:
		return render_template("resultados.html",entradas=lista)
	else:
		return render_template("resultados.html",entradas=["No hay resultados"])

@app.route('/consultaPaisPlatillo',methods=['POST'])
def consultaPaisPlatillo():
	pais=request.form['paisPlatillo']
	lista=restaurantes.buscaRestaurantesXPais(pais)
	if len(lista)>0:
		return render_template("resultados.html",entradas=lista)
	else:
		return render_template("resultados.html",entradas=["No hay resultados"])

@app.route('/consultaRestPlatillos',methods=['POST'])
def consultaRestPlatillos():
	restaurante=request.form['RestaurantePlatillos']
	lista=restaurantes.buscaPlatillosRest(restaurante)
	if len(lista)>0:
		return render_template("resultados.html",entradas=lista)
	else:
		return render_template("resultados.html",entradas=["No hay resultados"])

@app.route('/consultaRestIngrediente',methods=['POST'])
def consultaRestIngrediente():
	rest=request.form['RestxIngrediente']
	ingrediente=request.form['ingredienteRest']
	lista=restaurantes.platillosXrestIngrediente(rest,ingrediente)
	if len(lista)>1:
		return render_template("resultados.html",entradas=lista)
	else:
		return render_template("resultados.html",entradas=["No hay resultados"])


if __name__ == '__main__':
    app.run(debug=False,host="192.168.1.103",port=9090)
