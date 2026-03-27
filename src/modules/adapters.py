from src.models import PricedProduct

# Dry-run: build payloads without calling APIs

def build_listing_payloads(approved: list[PricedProduct]):
    payloads = []
    for p in approved:
        payloads.append({
            "title": p.title,
            "price": p.sell_price_krw,
            "category": p.category,
            "images": [p.image_url],
            "source_url": p.source_url,
        })
    return payloads
