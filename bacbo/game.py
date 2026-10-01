import random


def roll_dice(count=2, sides=6):
    """Sorteia dados virtuais."""
    if count < 1 or sides < 2:
        raise ValueError("A quantidade de dados e de faces deve ser válida.")
    return tuple(random.randint(1, sides) for _ in range(count))


def determine_winner(player_total, banker_total):
    if player_total > banker_total:
        return "PLAYER"
    if banker_total > player_total:
        return "BANKER"
    return "EMPATE"


def play_round():
    player_dice = roll_dice()
    banker_dice = roll_dice()
    player_total = sum(player_dice)
    banker_total = sum(banker_dice)
    return {
        "player_dice": player_dice,
        "player_total": player_total,
        "banker_dice": banker_dice,
        "banker_total": banker_total,
        "winner": determine_winner(player_total, banker_total),
    }
