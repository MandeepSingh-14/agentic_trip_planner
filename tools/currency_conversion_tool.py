import os 
from utils.currency_conversion import CurrencyConversionTool
from langchain.tools import tool
from typing import List
from dotenv import load_dotenv

class CurrencyConversionTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_conversion = CurrencyConversionTool(self.api_key)
        self.conversion_tool_list = self._setup_tools()
    
    def _setup_tools(self) -> List:
        """Setup all tools for the currency conversion tool"""
        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
            """Convert currency from one to another"""
            return self.conversion_service.convert(amount, from_currency, to_currency)
        
        return [convert_currency]