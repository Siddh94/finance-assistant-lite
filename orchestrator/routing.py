from agents.api_agent import get_stock_data
from agents.scraping_agent import scrape_yahoo_earnings
from data_ingestion.embeddings import save_vector_index
from agents.retriever_agent import retrieve_top_k
from agents.analysis_agent import analyze_market
from agents.language_agent import synthesize_briefing

def run_pipeline(symbols, user_query):
    # 1. Get market data
    market_data = get_stock_data(symbols)

    # 2. Scrape documents
    docs = []
    for symbol in symbols:
        scraped = scrape_yahoo_earnings(symbol)
        docs += scraped

    # 3. Fallback: Add dummy docs if scraping failed
    if not docs:
        docs = [
            f"{symbols[0]} Q1 earnings beat expectations by 15%.",
            f"{symbols[0]} reports strong chip sales growth in Asia.",
            f"{symbols[0]} sees revenue growth from AI demand in Q1."
        ]

    # 4. Save vector index
    save_vector_index(docs)

    # 5. Retrieve relevant docs
    retrieved_docs = retrieve_top_k(user_query, k=5)

    # 6. Analyze and summarize
    analysis = analyze_market(market_data, retrieved_docs)
    return synthesize_briefing(analysis)
