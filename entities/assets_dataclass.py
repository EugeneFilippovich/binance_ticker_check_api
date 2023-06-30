from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Cryptocurrency:
    symbol: str
    name: str


@dataclass
class AssetsConfig:
    cryptocurrencies: List[Cryptocurrency] = field(default_factory=lambda: [
        Cryptocurrency(symbol="BTCUSDT", name="Bitcoin"),
        Cryptocurrency(symbol="SUIUSDT", name="Sui"),
        Cryptocurrency(symbol="WAVESUSDT", name="Waves"),
        Cryptocurrency(symbol="APTUSDT", name="Aptos"),
        Cryptocurrency(symbol="ARBUSDT", name="Arbitrum")
    ])


assets_config = AssetsConfig()
