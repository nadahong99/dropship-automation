# dropship-automation

## Overview
Windows-first, Python-based automation scaffold for a Korea domestic wholesale-sourcing dropship business. This repository provides a **dry-run (no external API calls)** pipeline that simulates the full workflow:

- Sourcing candidates (stub connectors)
- MOQ risk scoring
- Competitor price analysis (stubbed provider)
- Fee/margin/price engine
- Approval gating
- Listing payload generation (Naver SmartStore / Coupang adapters in dry-run)
- SQLite database logging
- Telegram reporting (simulated)

> **Important**: Real API integrations are intentionally disabled until seller accounts, API keys, and legal access are confirmed.

## Quick start (Windows)
```bash
# from repo root
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python -m src.main --dry-run --config config.example.yaml
```

## What you can do now
- Run a full end-to-end simulation
- Review calculated prices/margins/MOQ risk
- See how approvals gate product registration
- Verify database logs

## Next steps (when accounts ready)
- Add real Telegram bot token
- Enable real connectors (permitted access only)
- Enable SmartStore/Coupang API adapters

## Repository structure
```
.
├─ src/
│  ├─ main.py
│  ├─ config.py
│  ├─ models.py
│  ├─ db.py
│  ├─ pipeline.py
│  └─ modules/
│     ├─ sourcing.py
│     ├─ pricing.py
│     ├─ moq.py
│     ├─ competitor.py
│     ├─ approval.py
│     └─ adapters.py
├─ config.example.yaml
├─ requirements.txt
└─ README.md
```

## Safety & compliance
- Only use allowed data access methods for supplier sites.
- Respect platform policies for SmartStore/Coupang.

## License
TBD
