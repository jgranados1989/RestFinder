%Consulta de restaurantes que tienen platillos de algún país específico
buscaRestXPais(Nombre,X):-platillo(Nombre,_,_,X,_).
%Consulta de todos los platillos de un restaurante
platillosXrest(X,Nombre,Sabor,Pais,Ingredientes):-platillo(X,Nombre,Sabor,Pais,Ingredientes).
%Consulta de platillos de X restaurante que incluyen Y ingrediente
platillosXrestIngrediente(X,Nombre,Sabor,Pais,Y):-platillo(X,Nombre,Sabor,Pais,Ingredientes),member(Y,Ingredientes).
%Base de conocimientos de platillos
platillo(mcDonadls,bigMac,salado,alemania,[pan,tomate,carne]).
platillo(bk,whopper,salado,alemania,[pan,tomate,carne]).
