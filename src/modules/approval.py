from src.models import PricedProduct


def require_approval(priced: list[PricedProduct], approval):
    if not approval.require_manual_approval:
        return priced
    # In dry-run, simulate approval by filtering high-risk items
    return [p for p in priced if p.moq_risk_score <= 0.7]
