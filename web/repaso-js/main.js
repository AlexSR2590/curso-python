var curso ="Repasando JavaScript";
var año = "2021";
var año2 = 2020;
var contador = 0;
var concatenacion = curso + " " + año;
/*
var datos = document.getElementById("datos");


datos.innerHTML = `
	<h1>Soy la caja de datos</h1>
	<h2>Esto es: ${concatenacion} </h2>
`;

if(año2 == 2021){
	datos.innerHTML += '<h1>Año actual</h1>';
}else{
	datos.innerHTML += '<h1>Año diferente</h1> '
}

for(var i = 1990; i<=2020; i ++){
	datos.innerHTML += '<h2>Estamos en el año: '+ i;
	
	contador ++;

}
datos.innerHTML += '<h2>contador: </h2>'+ contador;
*/
function muestraInfo(curso, año){
	var misDatos = `
	<h1>Soy la caja de datos</h1>
	<h2>Esto es: ${curso} en el año ${año} </h2>
`;
	return misDatos;

}

function imprimir(){
	var datos = document.getElementById("datos");
	datos.innerHTML = muestraInfo("Master en Python, repaso JS, html y css", "2021");
}

imprimir();

var nombres = ['Juan', 'Victor', 'Luara'];

/*
for(i=0; i< nomnbres.length; i++){
	document.write(nomnbres[i] + '<br/>')
}
*/
nombres.forEach((nombre) => {
	document.write(nombre + '<br/>');
)};