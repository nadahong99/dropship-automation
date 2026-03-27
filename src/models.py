from pydantic import BaseModel
from typing import Optional

class ProductCandidate(BaseModel):
    sku: str
    title: str
    source_site: str
    source_url: str
    unit_cost_krw: int
    moq: int
    image_url: str
    category: str

class PricedProduct(BaseModel):
    sku: str
    title: str
    source_site: str
    source_url: str
    unit_cost_krw: int
    moq: int
    image_url: str
    category: str
    sell_price_krw: int
    gross_margin_pct: float
    moq_risk_score: float
    competitor_price_avg: Optional[int] = None
