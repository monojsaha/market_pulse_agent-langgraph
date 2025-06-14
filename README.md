# Market Pulse Agent

**Automated portfolio news monitoring and sentiment analysis with local LLMs, Excel export, and multi-channel alerts.**

---

## Features

- **Input:** Manual CSV file of tickers (e.g., `sample_portfolio.csv`)
- **News Fetching:** Uses [NewsAPI](https://newsapi.org/) to gather the latest news for each ticker/company
- **Deduplication:** Removes duplicate news
- **LLM Analysis:** Runs local LLM (via [Ollama](https://ollama.com/), e.g., `llama3:13b`) for summarization and sentiment scoring
- **Ranking:** Prioritizes news by impact
- **Alerting:** Sends formatted alerts via Email, Slack, and WhatsApp (Twilio integration)
- **Excel Export:** Each run saves news data and sentiment summary to a timestamped `.xlsx` file
- **Sentiment Summary:** Summarized sentiment breakdown for each ticker is included in both Excel and alerts
- **Automated Scheduling:** Supports scheduled runs via Windows Task Scheduler or Python's `schedule` package
- **Modular:** Node-based design, easy to refactor to a [LangGraph](https://github.com/langchain-ai/langgraph) DAG

---

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/market_pulse_agent.git
cd market_pulse_agent
pip install -r requirements.txt

For email, if using Gmail, set up App Passwords. - https://support.google.com/accounts/answer/185833    

Slack webhook setup guide. - https://api.slack.com/messaging/webhooks

Twilio WhatsApp sandbox setup guide. - https://www.twilio.com/docs/whatsapp/sandbox


Edit sample_portfolio.csv with your tickers:

Install and Start Ollama
Download Ollama from https://ollama.com/download and install for Windows/Mac/Linux.

Pull and run your chosen model (e.g., llama3:13b):

    ollama pull llama3:13b
    ollama run llama3:13b
Keep this terminal running.

copy your .env copy to .env file and do the required modification
python main.py

The script will:

    Fetch news

    Deduplicate and analyze sentiment

    Save results to news_TIMESTAMP.xlsx (with both "News" and "SentimentSummary" sheets)

    Send alerts via your configured channels (Email, Slack, WhatsApp)

    Print a sentiment summary per ticker