from agents import Agent 
from tools import get_tickers , get_markets_coin,get_tickers_id ,get_tickers_symbols,get_crypto_info

Crypto_Agent=Agent(
    name="Crypto Currency Agent",
    instructions="""you are a crypto currency agent response the query from the provided tools and your name is Crypto Currency Agent""",
    tools=[get_tickers,get_markets_coin,get_tickers_id, get_tickers_symbols ,get_crypto_info]
) 

