function calcular() {

    alert("Calculando...")

let n1 = parseInt(document.getElementById('n1').value)
let n2 = parseInt(document.getElementById('n2').value)
let n3 = parseInt(document.getElementById('n3').value)
let n4 = parseInt(document.getElementById('n4').value)



soma = (n1 + n2 + n3 + n4) / 4



document.getElementById('Resultado').innerHTML=`Resultado: A sua média final é ${soma}`
}
