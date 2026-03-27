from src.models import ProductCandidate

# Stubbed sourcing connectors (replace with permitted access methods)

def get_candidates(config):
    max_candidates = config.max_candidates
    demo = [
        ProductCandidate(
            sku=f"DEMO-{i}",
            title=f"Demo Product {i}",
            source_site="ownerclan",
            source_url="https://www.ownerclan.com/",
            unit_cost_krw=5000 + (i * 200),
            moq=1 if i % 3 != 0 else 5,
            image_url="https://example.com/image.jpg",
            category="생활/가전"
        )
        for i in range(1, max_candidates + 1)
    ]
    return demo
