// Código personalizado do projeto
console.log('🚀 Projeto Bootstrap via NPM carregado!');
// Exemplo de uso: data atual
document.addEventListener('DOMContentLoaded', function() {
const dataElement = document.createElement('div');
dataElement.className = 'text-center mt-3 text-muted';
dataElement.innerHTML = `Projeto criado em ${new Date().toLocaleDateString('pt-BR')}`;
document.querySelector('.container').appendChild(dataElement);
});