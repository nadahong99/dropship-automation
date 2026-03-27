from src.models import ProductCandidate, PricedProduct


def price_products(candidates: list[ProductCandidate], pricing):
    priced = []
    for c in candidates:
        cost = c.unit_cost_krw + pricing.shipping_cost_krw
        platform_fee = pricing.platform_fee_pct["smartstore"]
        settlement_fee = pricing.settlement_fee_pct
        advertising_fee = pricing.advertising_fee_pct
        total_fee_pct = platform_fee + settlement_fee + advertising_fee

        # price to hit target margin
        target_margin = pricing.target_gross_margin_pct / 100
        sell_price = int(cost / (1 - target_margin - (total_fee_pct / 100)))

        gross_margin_pct = ((sell_price - cost) / sell_price) * 100

        priced.append(
            PricedProduct(
                sku=c.sku,
                title=c.title,
                source_site=c.source_site,
                source_url=c.source_url,
                unit_cost_krw=c.unit_cost_krw,
                moq=c.moq,
                image_url=c.image_url,
                category=c.category,
                sell_price_krw=sell_price,
                gross_margin_pct=round(gross_margin_pct, 2),
                moq_risk_score=0.0,
            )
        )
    return priced
