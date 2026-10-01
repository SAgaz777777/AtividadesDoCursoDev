function calcular() {


    //Declaração das variaveis
let n1 = parseInt(document.getElementById('n1').value)
let n2 = parseInt(document.getElementById('n2').value)

    // soma
soma = n1 + n2

// exibir o resultado

document.getElementById('Resultado').innerHTML=`Resultado: ${soma}`
}
