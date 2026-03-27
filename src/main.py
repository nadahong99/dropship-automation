from rich.console import Console
from src.config import load_config
from src.pipeline import run_pipeline

console = Console()

if __name__ == "__main__":
    config = load_config()
    console.print("[bold green]Dropship automation (dry-run) starting...[/bold green]")
    run_pipeline(config)
