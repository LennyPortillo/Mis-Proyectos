var nombre = prompt("Ingrese su Nombre:"," ");
var apellido = prompt("Ingrese su Apellido:"," ");
var gustos= 'Los lenguajes que mas te gustan son:'
var aca= 'Aqui se te brindara ademas de informacion video explicaciones sobre PHP, Java y Python'
var lenguajes=[prompt("Ingrese el primer lenguaje de programacion que mas le gusta"), prompt("ingrese el segundo"), prompt("ingrese el tercero") ]
lenguajes.sort();


var elemento1 = document.getElementById("java");


elemento1.innerHTML = '<p id="larma1">Bienvenido/a, ' +nombre+ ' ' + apellido+ '</p><p id="larma2">'+gustos+ ' ' + lenguajes + '</p><p id="larma2">' + aca + '</p>'       
                       


var color = prompt("Seleccione un color de fondo: Negro - gris oscuro- Azul ultra oscuro")

color = color.toLowerCase()

if(color=='negro') {
	elemento1.style.backgroundColor='#000'
}

if (color=='gris oscuro') {
	elemento1.style.backgroundColor='#2e2e2e'
}

if (color=='azul ultra oscuro') {
	elemento1.style.backgroundColor='#170130'
}
