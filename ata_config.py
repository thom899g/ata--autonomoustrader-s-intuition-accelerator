"""
ATA Configuration Module
Centralizes all configuration parameters with validation and environment support
"""
import os
from dataclasses import dataclass
from typing import Dict, Any, Optional
from enum import Enum
import logging

class TradingMode(Enum):
    PAPER = "paper"
    LIVE = "live"
    BACKTEST = "backtest"

@dataclass
class ExchangeConfig:
    """Exchange-specific configuration"""
    name: str = "binance"
    api_key: Optional[str] = None
    api_secret: Optional[str] = None
    testnet: bool = True
    rate_limit: int = 10
    symbols: list = None
    
    def __post_init__(self):
        if self.symbols is None:
            self.symbols = ["BTC/US