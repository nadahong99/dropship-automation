from rich.console import Console
from src.db import init_db
from src.modules.sourcing import get_candidates
from src.modules.moq import apply_moq_risk
from src.modules.competitor import enrich_with_competitor_prices
from src.modules.pricing import price_products
from src.modules.approval import require_approval
from src.modules.adapters import build_listing_payloads

console = Console()

def run_pipeline(config):
    init_db()
    candidates = get_candidates(config.sourcing)
    console.print(f"[cyan]Sourcing candidates: {len(candidates)}[/cyan]")

    priced = price_products(candidates, config.pricing)
    priced = apply_moq_risk(priced, config.moq)
    priced = enrich_with_competitor_prices(priced)

    approved = require_approval(priced, config.approval)
    payloads = build_listing_payloads(approved)

    console.print(f"[green]Approved for listing: {len(payloads)}[/green]")
    console.print("[yellow]Dry-run complete. No external API calls were made.[/yellow]")
