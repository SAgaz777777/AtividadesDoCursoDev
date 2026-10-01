function calcular() {

    alert("calculando...")


let altura = parseFloat(document.getElementById('Altura').value)
let peso = parseFloat(document.getElementById('Peso').value)

let imc = peso / (altura * altura)

let classificacao = ""

if (imc < 18.5) {
    classificacao = "Abaixo do peso"
} else if (imc >= 18.5 && imc < 25) {
    classificacao = "Peso normal"
} else {
    classificacao = "Acima do peso"
}

document.getElementById('Resultado').innerHTML =
`Seu IMC é ${imc.toFixed(2)} - ${classificacao}`
}
