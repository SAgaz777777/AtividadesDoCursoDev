const { calcularTotal } = require('./carrinho')

console.log("===EXECUTANDO TESTES MANUAIS (CAIXA PRETA) ===\n");

try {
    const res1 = calcularTotal([{preco: 100, quantidade: 1}], null);
    console.log(`[CT-01] Esp: 100 | Obtido: ${res1} -> ${res1 === 100 ? 'PASSOU' : 'FALHOU'}`);
} catch (e) {

    console.log('[CT-01] Erro: ${e.message}');
}

try {
    const res2 = calcularTotal([{preco: 60, quantidade: 1}], "PROMO10");
    console.log(`[CT-02] Esp: 60 | Obtido: ${res2} -> ${res2 === 60 ? 'PASSOU' : 'FALHOU'}`);
} catch (e) {

    console.log('[CT-01] Erro: ${e.message}');
}

try {
    const res3 = calcularTotal([{preco: 10, quantidade: -2}], null);
    console.log(`[CT-03] Esp: ERRO | Obtido: ${res3} -> FALHOU (Não gerou erro)`);
} catch (e) {

    console.log(`[CT-03] Esp ERRO | Obtido: ERRO (${e.message}) -> PASSOU`)
}

try {
    const res4 = calcularTotal([{preco: 33.333, quantidade: 1}], null);
    console.log(`[CT-04] Esp: 48.33 | Obtido: ${res4} -> ${res4 === 48.33 ? 'PASSOU' : 'FALHOU'}`)
} catch (e) {

    console.log('[CT-04] Erro: ${e.message}');
}

try {
    calcularTotal([], null);
    console.log(`[CT-05] Esp: ERRO | Obtido: Sem Erro -> FALHOU`)
} catch (e) {

    console.log(`[CT-05] Esp: ERRO | Obtido: ERRO (${e.message}) -> PASSOU`);
}

try {
    const res6 = calcularTotal([{preco: 80, quantidade: 1}], null);
    console.log(`[CT-06] Esp: 95 | Obtido: ${res6} -> ${res6 === 95 ? 'PASSOU' : 'FALHOU'}`)
} catch (e) {

    console.log('[CT-06] Erro: ${e.message}');
}


        
    
