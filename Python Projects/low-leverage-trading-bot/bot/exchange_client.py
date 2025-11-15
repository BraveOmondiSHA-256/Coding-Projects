import os

import ccxt
from dotenv import load_dotenv


class ExchangeClient:
    """
    Simple wrapper around ccxt so the rest of the bot uses one clean interface.
    Lazily creates the underlying ccxt client the first time it's needed.
    """

    def __init__(self) -> None:
        # Load variables from .env into environment
        load_dotenv()

        # Store config on the object
        self.exchange_name = (os.getenv("EXCHANGE", "bybit") or "bybit").lower()
        self.api_key = os.getenv("API_KEY") or None
        self.api_secret = os.getenv("API_SECRET") or None
        self.use_testnet = (os.getenv("USE_TESTNET", "true").lower() == "true")

        # Start with no client; we'll build it when needed
        self.client = None

    def _ensure_client(self):
        """
        Create the ccxt client if it doesn't exist yet.
        This makes the class more robust if __init__ ever changes.
        """
        if self.client is not None:
            return  # already built

        print(f"[ExchangeClient] Creating client for exchange='{self.exchange_name}' (testnet={self.use_testnet})")

        if self.exchange_name == "bybit":
            client = ccxt.bybit({
                "apiKey": self.api_key,
                "secret": self.api_secret,
                "enableRateLimit": True,
            })
            client.set_sandbox_mode(self.use_testnet)
            self.client = client

        elif self.exchange_name == "blofin":
            client = ccxt.blofin({
                "apiKey": self.api_key,
                "secret": self.api_secret,
                "enableRateLimit": True,
            })
            # BloFin public endpoints work without explicit sandbox toggle.
            self.client = client

        else:
            raise ValueError(f"Unsupported EXCHANGE: {self.exchange_name}")

    # --- Public helper methods ---

    def fetch_ohlcv(self, symbol: str, timeframe: str = "1h", limit: int = 200):
        """
        Fetch historical candles (open-high-low-close-volume).
        Returns a raw list from ccxt.
        """
        self._ensure_client()
        return self.client.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    def get_balance(self, code: str = "USDT") -> float:
        """
        Return total balance for a specific currency (e.g. 'USDT').

        Will only work if you set API key/secret AND the exchange
        allows balance calls with those permissions.
        """
        self._ensure_client()
        balances = self.client.fetch_balance()
        total = balances.get("total", {})
        return float(total.get(code, 0.0))

    def get_server_time(self):
        """
        Convenience helper to make sure our connection is alive.
        """
        self._ensure_client()
        return self.client.milliseconds()
