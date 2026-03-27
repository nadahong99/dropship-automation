from src.models import PricedProduct


def apply_moq_risk(priced: list[PricedProduct], moq):
    for p in priced:
        risk = (p.moq / moq.max_moq) * moq.risk_weight
        p.moq_risk_score = round(min(risk, 1.0), 2)
    return priced
