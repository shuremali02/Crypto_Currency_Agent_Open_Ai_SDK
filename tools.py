from agents import function_tool
from dotenv import load_dotenv 
import requests 
import os 

load_dotenv()


base_url=os.getenv("COINLORE_BASE_URL")
@function_tool
def get_tickers(start:int=0,limit:int=10):
    url=f"{base_url}/tickers?start={start}&limit={limit}"
    response=requests.get(url)
    return response.json()["data"]


@function_tool
def get_markets_coin(market_cap_id):
    url=f"{base_url}/coins/markets?id={market_cap_id}"
    response=requests.get(url)
    return response.json()


@function_tool
def get_tickers_id(ticker_id:str):
    url=f"{base_url}/tickers?id={ticker_id}"
    response=requests.get(url)
    return response.json()


@function_tool
def get_tickers_symbols(ticker_symbols:str):
    url=f"{base_url}/tickers?symbol={ticker_symbols}"
    response=requests.get(url)
    return response.json()["data"]

@function_tool
def get_crypto_info():
    url=f"{base_url}/global"
    response=requests.get(url)
    return response.json()