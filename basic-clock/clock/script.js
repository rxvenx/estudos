const PONTEIROHORA = document.querySelector("#hour");
const PONTEIROMINUTO = document.querySelector("#minute");
const PONTEIROSEGUNDO = document.querySelector("#second");



var data = new Date(); //criar variavel e salvar conteudo numa variavel tipo data
console.log(data);

let hora = data.getHours();
let minuto = data.getMinutes();
let segundo = data.getSeconds();
console.log(" hora: " + hora + " /minuto: " + minuto + " /segundo: " + segundo);

let posicaoHoras = (hora*360/12)+(minuto*360/60)/12;
let posicaoMinutos = (minuto*360/60)+(segundo*(360/60)/60);
let posicaoSegundos = segundo*360/60;

    function executeClock () {
    
    posicaoHoras = posicaoHoras+(3/360);
    posicaoMinutos = posicaoMinutos+(6/60);  
    posicaoSegundos = posicaoSegundos+6;

    PONTEIROHORA.style.transform = "rotate(" + posicaoHoras + "deg)";
    PONTEIROMINUTO.style.transform = "rotate(" + posicaoMinutos + "deg)";
    PONTEIROSEGUNDO.style.transform = "rotate(" + posicaoSegundos + "deg)";
    
}


var interval = setInterval (executeClock, 1000);
