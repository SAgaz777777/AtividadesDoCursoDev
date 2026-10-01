class BankrollManager:
    """Gerencia exclusivamente créditos virtuais da sessão."""

    def __init__(self, initial_balance, bet_amount, stop_loss, stop_win, max_rounds):
        if initial_balance <= 0 or bet_amount <= 0 or stop_loss <= 0 or stop_win <= 0 or max_rounds <= 0:
            raise ValueError("A banca, a aposta, os limites e as rodadas devem ser positivos.")
        self.initial_balance = float(initial_balance)
        self.balance = float(initial_balance)
        self.bet_amount = float(bet_amount)
        self.stop_loss = float(stop_loss)
        self.stop_win = float(stop_win)
        self.max_rounds = int(max_rounds)
        self.rounds_played = 0
        self.highest_balance = self.balance
        self.lowest_balance = self.balance

    @property
    def profit(self):
        return self.balance - self.initial_balance

    def can_bet(self):
        if self.balance < self.bet_amount:
            return False, "Créditos virtuais insuficientes para a aposta."
        if self.rounds_played >= self.max_rounds:
            return False, "Número máximo de rodadas atingido."
        if self.profit <= -self.stop_loss:
            return False, "Stop Loss atingido."
        if self.profit >= self.stop_win:
            return False, "Stop Win atingido."
        return True, ""

    def register_result(self, selected_side, winner):
        allowed, reason = self.can_bet()
        if not allowed:
            raise RuntimeError(f"Não é possível registrar a rodada: {reason}")
        self.rounds_played += 1
        if winner == "EMPATE":
            change = 0.0
        elif selected_side == winner:
            change = self.bet_amount
            self.balance += change
        else:
            change = -min(self.bet_amount, self.balance)
            self.balance += change
        self.highest_balance = max(self.highest_balance, self.balance)
        self.lowest_balance = min(self.lowest_balance, self.balance)
        return change

    def status(self):
        allowed, reason = self.can_bet()
        return {"balance": self.balance, "profit": self.profit, "rounds_played": self.rounds_played,
                "highest_balance": self.highest_balance, "lowest_balance": self.lowest_balance,
                "session_active": allowed, "reason": reason}
