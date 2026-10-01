let input = document.getElementById("inputBox");

// seleciona todos os botões da página
let buttons = document.querySelectorAll("button");

// variável que armazena a expressão digitada
let string = "";

// converte a lista de botões (NodeList) em um array
let arr = Array.from(buttons);

// percorre cada botão para adicionar um evento de clique
arr.forEach(button => {
    button.addEventListener("click", (e) => {

        // se o botão clicado for "="
        if (e.target.innerHTML == "=") {
            // avalia a expressão matemática digitada
            string = eval(string);

            // mostra o resultado no display
            input.value = string;
        }

        // se o botão for "AC" (limpar tudo)
        else if (e.target.innerHTML == "AC") {
            string = ""; // limpa a expressão
            input.value = string; // limpa o display
        }

        // se o botão for "DEL" (apagar último caractere)
        else if (e.target.innerHTML == "DEL") {
            // remove o último caractere da string
            string = string.substring(0, string.length - 1);

            // atualiza o display
            input.value = string;
        }

        // para qualquer outro botão (números e operadores)
        else {
            // adiciona o valor do botão à expressão
            string += e.target.innerHTML;

            // atualiza o display com a nova expressão
            input.value = string;
        }
    });
});