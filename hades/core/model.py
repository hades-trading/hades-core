from datetime import datetime

from pydantic import BaseModel


class Tick(BaseModel):
    symbol: str
    price: float
    timestamp: datetime


class Bar(BaseModel):
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    vol: float


class Order(BaseModel):
    order_id: str
    order_type: str
    symbol: str
    instrument_type: str
    price: float
    status: str
    side: str
    quantity: float
    timestamp: datetime


class Position(BaseModel):
    symbol: str
    instrument_type: str
    side: str
    quantity: float
    unrealized_profit: float
    unrealized_profit_ratio: float
    mode: str
    price: float
    timestamp: datetime


class Balance(BaseModel):
    asset: str
    available_balance: float


class Trade(BaseModel):
    symbol: str
    id: str
    order_id: str
    side: str
    price: float
    quantity: float
    realized_pnl: float
    margin_asset: str
    quote_quantity: float
    commission: float
    commission_to_usdt: float
    commission_asset: str
    timestamp: datetime
    maker: bool
