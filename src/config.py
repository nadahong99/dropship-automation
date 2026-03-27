import yaml
from pydantic import BaseModel

class AppConfig(BaseModel):
    mode: str
    timezone: str
    currency: str
    daily_budget_krw: int

class SourcingConfig(BaseModel):
    preferred_sites: list[str]
    max_candidates: int

class PricingConfig(BaseModel):
    target_gross_margin_pct: float
    platform_fee_pct: dict
    settlement_fee_pct: float
    advertising_fee_pct: float
    shipping_cost_krw: int

class MOQConfig(BaseModel):
    max_moq: int
    risk_weight: float

class ApprovalConfig(BaseModel):
    require_manual_approval: bool

class TelegramConfig(BaseModel):
    enabled: bool
    bot_token: str
    chat_id: str

class Config(BaseModel):
    app: AppConfig
    sourcing: SourcingConfig
    pricing: PricingConfig
    moq: MOQConfig
    approval: ApprovalConfig
    telegram: TelegramConfig

def load_config(path: str = "config.example.yaml") -> Config:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return Config(**data)
