def normalize_history(history):
    return [item.get("winner") if isinstance(item, dict) else item for item in history]


def get_non_tie_results(history):
    return [result for result in normalize_history(history) if result in ("PLAYER", "BANKER")]


def current_streak(history):
    results = get_non_tie_results(history)
    if not results:
        return None, 0
    side = results[-1]
    length = 0
    for result in reversed(results):
        if result != side:
            break
        length += 1
    return side, length


def detect_sequence(history, minimum=3):
    side, length = current_streak(history)
    if side and length >= minimum:
        return {"detected": True, "side": side, "length": length,
                "message": f"Tendência visual identificada: sequência de {side} com {length} resultados."}
    return {"detected": False, "message": "Nenhuma sequência significativa identificada."}


def detect_dragon(history, minimum=6):
    side, length = current_streak(history)
    if side and length >= minimum:
        return {"detected": True, "side": side, "length": length,
                "message": f"Possível Dragão identificado: {length} resultados consecutivos de {side}."}
    return {"detected": False, "message": "Nenhum Dragão identificado no momento."}


def detect_zigzag(history, minimum=6):
    results = get_non_tie_results(history)
    if len(results) < minimum:
        return {"detected": False, "message": "Histórico insuficiente para analisar zigue-zague."}
    recent = results[-minimum:]
    if all(recent[index] != recent[index - 1] for index in range(1, len(recent))):
        return {"detected": True, "length": minimum, "pattern": recent,
                "message": "Possível padrão de alternância identificado no histórico recente."}
    return {"detected": False, "message": "Nenhum zigue-zague claro identificado."}


def detect_pairs(history, minimum_pairs=2):
    results = get_non_tie_results(history)
    needed = minimum_pairs * 2
    if len(results) < needed:
        return {"detected": False, "message": "Histórico insuficiente para analisar pares."}
    recent = results[-needed:]
    pairs = [recent[index:index + 2] for index in range(0, needed, 2)]
    valid = all(pair[0] == pair[1] for pair in pairs)
    alternating = all(pairs[index][0] != pairs[index - 1][0] for index in range(1, len(pairs)))
    if valid and alternating:
        return {"detected": True, "pairs": pairs,
                "message": "Possível padrão de pares alternados identificado."}
    return {"detected": False, "message": "Nenhum padrão claro de pares identificado."}


def detect_break(history, minimum_streak=3):
    results = get_non_tie_results(history)
    if len(results) < minimum_streak + 1:
        return {"detected": False, "message": "Histórico insuficiente para detectar quebra."}
    previous_side = results[-2]
    previous_count = 0
    for result in reversed(results[:-1]):
        if result != previous_side:
            break
        previous_count += 1
    if previous_count >= minimum_streak and results[-1] != previous_side:
        return {"detected": True, "previous_side": previous_side, "previous_length": previous_count,
                "new_side": results[-1], "message": f"Possível quebra da sequência anterior de {previous_side}. "
                "Recomenda-se observar novas rodadas antes de interpretar uma nova estrutura."}
    return {"detected": False, "message": "Nenhuma quebra relevante identificada."}


def detect_surf(history, minimum=4):
    sequence = detect_sequence(history, minimum)
    if sequence["detected"]:
        return {"detected": True, "side": sequence["side"], "length": sequence["length"],
                "message": f"SURF: tendência visual recente detectada em {sequence['side']} "
                f"com {sequence['length']} resultados consecutivos."}
    return {"detected": False, "message": "SURF: nenhuma tendência recente suficientemente clara foi identificada."}


def analyze_patterns(history, dragon_minimum=6, sequence_minimum=3, zigzag_minimum=6, minimum_pairs=2):
    return {"sequence": detect_sequence(history, sequence_minimum), "dragon": detect_dragon(history, dragon_minimum),
            "zigzag": detect_zigzag(history, zigzag_minimum), "pairs": detect_pairs(history, minimum_pairs),
            "break": detect_break(history, sequence_minimum), "surf": detect_surf(history, sequence_minimum)}
