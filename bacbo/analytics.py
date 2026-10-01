import pandas as pd


def get_results(history):
    return [item["winner"] for item in history]


def longest_streak(history, side):
    longest = current = 0
    for result in get_results(history):
        current = current + 1 if result == side else 0
        longest = max(longest, current)
    return longest


def current_streak(history):
    results = [item["winner"] for item in history if item["winner"] != "EMPATE"]
    if not results:
        return {"side": None, "length": 0}
    side = results[-1]
    length = 0
    for result in reversed(results):
        if result != side:
            break
        length += 1
    return {"side": side, "length": length}


def calculate_statistics(history, bankroll):
    total = len(history)
    player_wins = sum(item["winner"] == "PLAYER" for item in history)
    banker_wins = sum(item["winner"] == "BANKER" for item in history)
    ties = sum(item["winner"] == "EMPATE" for item in history)
    streak = current_streak(history)
    return {"total_rounds": total, "player_wins": player_wins, "banker_wins": banker_wins, "ties": ties,
            "player_percentage": player_wins / total * 100 if total else 0,
            "banker_percentage": banker_wins / total * 100 if total else 0,
            "longest_player_streak": longest_streak(history, "PLAYER"),
            "longest_banker_streak": longest_streak(history, "BANKER"), "current_streak_side": streak["side"],
            "current_streak_length": streak["length"], "profit": bankroll.profit,
            "highest_balance": bankroll.highest_balance, "lowest_balance": bankroll.lowest_balance}


def history_dataframe(history):
    columns = ["Rodada", "Dados Player", "Total Player", "Dados Banker", "Total Banker", "Resultado", "Aposta", "Banca"]
    rows = [{"Rodada": item["round"], "Dados Player": f"{item['player_dice'][0]} + {item['player_dice'][1]}",
             "Total Player": item["player_total"], "Dados Banker": f"{item['banker_dice'][0]} + {item['banker_dice'][1]}",
             "Total Banker": item["banker_total"], "Resultado": item["winner"], "Aposta": item["bet"], "Banca": item["balance"]}
            for item in history]
    return pd.DataFrame(rows, columns=columns)


def bankroll_dataframe(history):
    rows = [{"Rodada": item["round"], "Banca": item["balance"]} for item in history]
    return pd.DataFrame(rows, columns=["Rodada", "Banca"])
