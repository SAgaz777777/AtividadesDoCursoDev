function Mensagem() {
    alert("Suas informações foram cadastradas com sucesso")

    let nome = document.getElementById('nome').value;
    let sobrenome = document.getElementById('sobrenome').value;
    let idade = parseInt(document.getElementById('idade').value);
    let peso = parseFloat(document.getElementById('peso').value);

    let mensagem = `Olá, ${nome} ${sobrenome} Você tem ${idade} anos e pesa ${peso} kg.`;

    document.getElementById('mensagem').innerHTML = mensagem;
}
