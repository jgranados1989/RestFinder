buscaRestXPais(Nombre,X):-platillo(Nombre,_,_,X,_).

platillosXrest(X,Nombre,Sabor,Pais,Ingredientes):-platillo(X,Nombre,Sabor,Pais,Ingredientes).

platillosXrestIngrediente(X,Nombre,Sabor,Pais,Y):-platillo(X,Nombre,Sabor,Pais,Ingredientes),member(Y,Ingredientes).

platillo(mcDonadls,bigMac,salado,alemania,[pan,tomate,carne]).
platillo(bk,whopper,salado,alemania,[pan,tomate,carne]).
