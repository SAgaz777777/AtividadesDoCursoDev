function calcular() {

    alert("Calculando...")
let Bm = parseInt(document.getElementById('Bm').value)
let bm = parseInt(document.getElementById('bm').value)
let H = parseInt(document.getElementById('H').value)


soma = ((Bm + bm) * H) / 2



document.getElementById('Resultado').innerHTML=`Resultado: a área do trapézio ${soma}`
}
