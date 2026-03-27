from src.models import PricedProduct

# Stub: replace with allowed search/market data providers

def enrich_with_competitor_prices(priced: list[PricedProduct]):
    for p in priced:
        p.competitor_price_avg = int(p.sell_price_krw * 0.95)
    return priced
