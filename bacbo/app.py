import streamlit as st

from analytics import bankroll_dataframe, calculate_statistics, history_dataframe
from bankroll import BankrollManager
from game import play_round
from strategies import analyze_patterns


st.set_page_config(page_title="Bac Bo Simulator", page_icon="🎲", layout="wide")


def initialize_session():
    defaults = {"history": [], "bankroll": None, "last_round": None, "selected_side": None}
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_session(initial_balance, bet_amount, stop_loss, stop_win, max_rounds):
    st.session_state.history = []
    st.session_state.bankroll = BankrollManager(
        initial_balance, bet_amount, stop_loss, stop_win, max_rounds
    )
    st.session_state.last_round = None
    st.session_state.selected_side = None


def result_icon(result):
    return {"PLAYER": "🔴", "BANKER": "🔵", "EMPATE": "⚪"}.get(result, "❓")


initialize_session()
st.title("🎲 Bac Bo Simulator")
st.caption("Simulador educacional com créditos virtuais. Nenhuma integração com dinheiro real ou cassinos.")

with st.sidebar:
    st.header("⚙️ Configuração da sessão")
    initial_balance = st.number_input("Banca virtual inicial", min_value=10.0, value=1000.0, step=10.0)
    bet_amount = st.number_input("Valor fixo da aposta virtual", min_value=1.0, value=10.0, step=1.0)
    stop_loss = st.number_input("Stop Loss virtual", min_value=1.0, value=100.0, step=10.0)
    stop_win = st.number_input("Meta / Stop Win virtual", min_value=1.0, value=100.0, step=10.0)
    max_rounds = st.number_input("Número máximo de rodadas", min_value=1, value=50, step=1)
    analysis_mode = st.selectbox("Modo de análise", ["SURF", "ZIG-ZAG", "PARES", "SEQUÊNCIA", "OBSERVAÇÃO LIVRE"])
    dragon_minimum = st.slider("Mínimo para considerar Dragão", min_value=4, max_value=12, value=6)
    if st.button("🔄 Reiniciar treinamento", use_container_width=True):
        reset_session(initial_balance, bet_amount, stop_loss, stop_win, max_rounds)
        st.rerun()

if st.session_state.bankroll is None:
    reset_session(initial_balance, bet_amount, stop_loss, stop_win, max_rounds)

bankroll = st.session_state.bankroll
status = bankroll.status()

st.subheader("💳 Sessão virtual")
metric_columns = st.columns(4)
metric_columns[0].metric("Banca atual", f"{status['balance']:.2f} créditos")
metric_columns[1].metric("Lucro / Prejuízo", f"{status['profit']:+.2f} créditos")
metric_columns[2].metric("Rodadas", f"{status['rounds_played']} / {bankroll.max_rounds}")
metric_columns[3].metric("Aposta virtual", f"{bankroll.bet_amount:.2f} créditos")

if not status["session_active"]:
    st.warning(f"🛑 Sessão de treinamento encerrada: {status['reason']}")

st.subheader("🎯 Escolha para treinamento")
choice_columns = st.columns(2)
if choice_columns[0].button("🔴 PLAYER", use_container_width=True, disabled=not status["session_active"]):
    st.session_state.selected_side = "PLAYER"
if choice_columns[1].button("🔵 BANKER", use_container_width=True, disabled=not status["session_active"]):
    st.session_state.selected_side = "BANKER"
if st.session_state.selected_side:
    st.info(f"Lado selecionado: **{st.session_state.selected_side}**")

if st.button("🎲 INICIAR NOVA RODADA", use_container_width=True,
             disabled=not status["session_active"] or st.session_state.selected_side is None):
    selected_side = st.session_state.selected_side
    round_data = play_round()
    change = bankroll.register_result(selected_side, round_data["winner"])
    record = {**round_data, "round": bankroll.rounds_played, "selected_side": selected_side,
              "bet": bankroll.bet_amount, "change": change, "balance": bankroll.balance}
    st.session_state.history.append(record)
    st.session_state.last_round = record
    st.session_state.selected_side = None
    st.rerun()

if st.session_state.last_round:
    last = st.session_state.last_round
    st.divider()
    st.subheader("🎲 Última rodada")
    result_columns = st.columns(3)
    result_columns[0].write(f"### 🔴 PLAYER\nDados: {last['player_dice'][0]} + {last['player_dice'][1]}")
    result_columns[0].metric("Total", last["player_total"])
    result_columns[1].write(f"### 🔵 BANKER\nDados: {last['banker_dice'][0]} + {last['banker_dice'][1]}")
    result_columns[1].metric("Total", last["banker_total"])
    result_columns[2].write("### 🏆 RESULTADO")
    result_columns[2].metric("Vencedor", last["winner"])
    message = f"Resultado virtual: {last['change']:+.2f} créditos"
    (st.success if last["change"] > 0 else st.error if last["change"] < 0 else st.info)(message)

history = st.session_state.history
st.divider()
st.subheader("📊 Histórico visual")
st.markdown(" ".join(result_icon(item["winner"]) for item in history) if history else "Ainda não existem rodadas no histórico.")

st.divider()
st.subheader("🧠 ANÁLISE DO GRÁFICO")
if history:
    patterns = analyze_patterns(history, dragon_minimum=dragon_minimum, sequence_minimum=3, zigzag_minimum=6, minimum_pairs=2)
    selected_pattern = {"SURF": patterns["surf"], "ZIG-ZAG": patterns["zigzag"], "PARES": patterns["pairs"], "SEQUÊNCIA": patterns["sequence"]}.get(analysis_mode)
    if selected_pattern:
        (st.success if selected_pattern["detected"] else st.info)(selected_pattern["message"])
        if analysis_mode == "SEQUÊNCIA" and patterns["dragon"]["detected"]:
            st.warning(patterns["dragon"]["message"])
        if analysis_mode == "SEQUÊNCIA" and patterns["break"]["detected"]:
            st.warning(patterns["break"]["message"])
    else:
        st.info("Modo observação livre: os resultados são apresentados sem classificação de estratégia.")
else:
    st.info("Jogue algumas rodadas virtuais para iniciar a análise do histórico.")
st.caption("Aviso educacional: padrões históricos descrevem o histórico observado e não garantem o próximo resultado.")

st.divider()
st.subheader("📈 Estatísticas")
stats = calculate_statistics(history, bankroll)
stat_columns = st.columns(4)
for column, label, key in zip(stat_columns, ["Vitórias Player", "Vitórias Banker", "Empates", "Total de rodadas"], ["player_wins", "banker_wins", "ties", "total_rounds"]):
    column.metric(label, stats[key])
stat_columns = st.columns(4)
for column, label, key in zip(stat_columns, ["% Player", "% Banker", "Maior sequência Player", "Maior sequência Banker"], ["player_percentage", "banker_percentage", "longest_player_streak", "longest_banker_streak"]):
    value = f"{stats[key]:.2f}%" if "percentage" in key else stats[key]
    column.metric(label, value)
if stats["current_streak_side"]:
    st.info(f"Sequência atual: {stats['current_streak_length']} resultado(s) consecutivo(s) de {stats['current_streak_side']}.")

balance_columns = st.columns(3)
balance_columns[0].metric("Maior banca", f"{stats['highest_balance']:.2f}")
balance_columns[1].metric("Menor banca", f"{stats['lowest_balance']:.2f}")
balance_columns[2].metric("Resultado da sessão", f"{stats['profit']:+.2f}")

st.divider()
st.subheader("📉 Evolução da banca virtual")
bankroll_df = bankroll_dataframe(history)
if not bankroll_df.empty:
    st.line_chart(bankroll_df, x="Rodada", y="Banca")
else:
    st.info("O gráfico será exibido após a primeira rodada.")

st.divider()
st.subheader("📋 Histórico detalhado")
st.dataframe(history_dataframe(history), use_container_width=True, hide_index=True)
st.caption("Projeto educacional: utiliza exclusivamente créditos fictícios.")
