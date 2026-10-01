function Mensagem() {
    
    let nome = String(document.getElementById('Nome').value)
    let idade = parseInt(document.getElementById('Idade').value)
    let cidade = String(document.getElementById('Cidade').value)
 
    
    let mensagem = `Olá, ${nome} Você tem ${idade} anos e mora em ${cidade}.`;

    
    document.getElementById('Mensagem').innerHTML = mensagem
}
