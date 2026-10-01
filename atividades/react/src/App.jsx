import { useState } from 'react'
import './components/FormCalculadora.css'

function App() {
  const [primeiro, setPrimeiro] = useState('')
  const [segundo, setSegundo] = useState('')
  const [operacao, setOperacao] = useState('+')
  const [resultado, setResultado] = useState(null)
  const [erro, setErro] = useState('')

  function calcular(event) {
    event.preventDefault()
    const primeiroNumero = Number(primeiro)
    const segundoNumero = Number(segundo)

    if (primeiro === '' || segundo === '') {
      setErro('Preencha os dois números para calcular.')
      setResultado(null)
      return
    }
    if (operacao === '/' && segundoNumero === 0) {
      setErro('Não é possível dividir por zero.')
      setResultado(null)
      return
    }

    setResultado({
      '+': primeiroNumero + segundoNumero,
      '-': primeiroNumero - segundoNumero,
      '*': primeiroNumero * segundoNumero,
      '/': primeiroNumero / segundoNumero,
    }[operacao])
    setErro('')
  }

  function limpar() {
    setPrimeiro('')
    setSegundo('')
    setOperacao('+')
    setResultado(null)
    setErro('')
  }

  return (
    <main className="calculator-page">
      <section className="calculator" aria-labelledby="calculator-title">
        <div className="calculator-heading">
          <h1 id="calculator-title">Calculadora</h1>
          <p>Resolva contas simples com clareza e agilidade.</p>
        </div>
        <form onSubmit={calcular}>
          <div className="form-grid">
            <label htmlFor="primeiro-numero">Primeiro número
              <input id="primeiro-numero" type="number" step="any" value={primeiro} onChange={(event) => setPrimeiro(event.target.value)} placeholder="Ex.: 24" />
            </label>
            <label htmlFor="operacao">Operação
              <select id="operacao" value={operacao} onChange={(event) => setOperacao(event.target.value)}>
                <option value="+">Somar (+)</option>
                <option value="-">Subtrair (-)</option>
                <option value="*">Multiplicar (*)</option>
                <option value="/">Dividir (/)</option>
              </select>
            </label>
            <label htmlFor="segundo-numero">Segundo número
              <input id="segundo-numero" type="number" step="any" value={segundo} onChange={(event) => setSegundo(event.target.value)} placeholder="Ex.: 6" />
            </label>
          </div>
          <div className="actions">
            <button className="calculate-button" type="submit">Calcular</button>
            <button className="clear-button" type="button" onClick={limpar}>Limpar</button>
          </div>
        </form>
        <div className="result" aria-live="polite">
          <span>Resultado</span>
          <strong>{resultado !== null ? resultado : '—'}</strong>
          {erro && <small>{erro}</small>}
        </div>
      </section>
    </main>
  )
}

export default App
