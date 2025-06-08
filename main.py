from nodes.csv_input import load_tickers
from nodes.fetch_news import fetch_news_for_tickers
from nodes.deduplicate import deduplicate_news
from nodes.llm_analysis import analyze_news_items
from nodes.ranking import rank_news_items
from nodes.alert import send_alerts

def agent_run():
    print("[INFO] Starting Market Pulse Agent...")
    tickers = load_tickers("sample_portfolio.csv")
    print(f"[INFO] Loaded {len(tickers)} tickers.")

    # Fetch news
    news_items = fetch_news_for_tickers(tickers)
    print(f"[INFO] Fetched {len(news_items)} news items.")

    unique_news = deduplicate_news(news_items)
    print(f"[INFO] {len(unique_news)} unique news items after deduplication.")

    # Analyze news with LLM (adds 'sentiment' key)
    analyzed_news = analyze_news_items(unique_news)
    print(f"[INFO] Analyzed {len(analyzed_news)} news items.")

    # Save to Excel with sentiment summary
    fetch_news_for_tickers(tickers, analyzed_news)  # <--- Add this here

    ranked_news = rank_news_items(analyzed_news)
    print(f"[INFO] Ranked news items.")

    send_alerts(ranked_news)
    print("[INFO] Run complete.\n")

if __name__ == "__main__":
    agent_run()
