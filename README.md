# CryptoAdvisor Chatbot

**Version:** 1.0.0

## 🤖 About CryptoAdvisor

CryptoAdvisor is a simple, rule-based chatbot built in Python. It's designed to analyze a predefined dataset of cryptocurrency information and provide investment suggestions based on two main criteria:

1.  **Profitability:** Considers factors like price trends and market capitalization.
2.  **Sustainability:** Evaluates aspects like energy consumption and a project's sustainability score.

The chatbot engages users in a conversational manner, aiming to guide them towards cryptocurrencies that are potentially "green and growing."

**Disclaimer:** *CryptoAdvisor provides suggestions based on its predefined dataset and rules. It is for informational and educational purposes only and does not constitute financial advice. Cryptocurrency investments are inherently risky. Always conduct your own thorough research (DYOR) before making any investment decisions.*

## ✨ Features

* **Conversational Interface:** Interacts with users through a command-line interface.
* **Predefined Crypto Data:** Uses a built-in dictionary (`crypto_db`) containing information about several cryptocurrencies (Bitcoin, Ethereum, Cardano, Solana, Polkadot, and a fictional EcoCoin).
    * Data points for each coin include: `price_trend`, `market_cap`, `energy_use`, `sustainability_score`, and a brief `description`.
* **Rule-Based Recommendations:**
    * **Profitability:** Suggests coins that are "rising" in price and have a "high" or "medium" market cap.
    * **Sustainability:** Recommends coins with "low" or "very low" energy use and a sustainability score above 7/10.
    * **Long-Term Growth:** Provides suggestions based on a combined score that balances price trends (rising/stable) and sustainability metrics (score >= 6/10, not high energy use).
* **Specific Queries:**
    * Ask about coins that are "trending up."
    * Inquire about the "most sustainable" or "eco-friendly" coins.
    * Seek advice on coins for "profitability" or to "make money."
    * Ask for recommendations for "long-term growth."
    * Request "details for [coin name]" (e.g., "details for Bitcoin").
    * Ask the bot to "list all" coins it knows.
* **Chatbot Personality:**
    * **Name:** CryptoAdvisor
    * **Tone:** Friendly and informative (e.g., "Hey there! I'm CryptoAdvisor. Let’s find you a green and growing crypto! 🌿📈")

## 🛠️ Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Running the Chatbot

1.  **Save the Code:** Save the Python code provided into a file named `crypto_advisor.py` (or any other `.py` file).
2.  **Open a Terminal or Command Prompt:** Navigate to the directory where you saved the file.
3.  **Run the Script:** Execute the script using the Python interpreter:
    ```bash
    python crypto_advisor.py
    ```
4.  **Interact:** The chatbot will greet you, and you can start asking questions!

    Example Interaction:
    ```
    Hey there! I'm CryptoAdvisor. Let’s find you a green and growing crypto! 🌿📈
    Remember, cryptocurrency investments are risky. Always do your own thorough research before investing! This is not financial advice.
    ------------------------------
    You: Which crypto is trending up?
    CryptoAdvisor: The following cryptos are currently trending up: Bitcoin, Cardano, Solana. For potential profitability, consider Bitcoin! It's trending up and has a solid market cap. (Bitcoin:
      Price Trend: rising
      Market Cap: high
      Energy Use: high
      Sustainability Score: 3.0/10
      Description: The original cryptocurrency, known for its high market capitalization but also high energy consumption.) 🚀
    You: What's the most sustainable coin?
    CryptoAdvisor: For sustainability, EcoCoin is a top choice! 🌱 It’s eco-friendly (very low energy use) and has a great sustainability score (9.5/10). (EcoCoin:
      Price Trend: stable
      Market Cap: low
      Energy Use: very low
      Sustainability Score: 9.5/10
      Description: A (fictional) coin designed with maximum energy efficiency and positive environmental impact in mind.)
    You: bye
    CryptoAdvisor: Goodbye! Happy (and safe) investing! 👋
    Remember, cryptocurrency investments are risky. Always do your own thorough research before investing! This is not financial advice.
    ```

## 📂 Code Structure

* **`crypto_db` (Dictionary):** Stores the cryptocurrency data.
* **`BOT_NAME`, `BOT_TONE_GREETING`, `BOT_DISCLAIMER` (Strings):** Define the bot's personality and important messages.
* **`get_crypto_details(coin_name)` (Function):** Formats and returns details for a specific coin.
* **`recommend_by_profitability()` (Function):** Logic for profitability-based recommendations.
* **`recommend_by_sustainability()` (Function):** Logic for sustainability-based recommendations.
* **`recommend_for_long_term_growth()` (Function):** Logic for balanced long-term growth recommendations.
* **`chatbot_response(user_query)` (Function):** Core logic to process user input and generate responses.
* **`start_chat()` (Function):** Initializes and runs the main chat loop.
* **`if __name__ == "__main__":`:** Ensures `start_chat()` runs when the script is executed.

## 🚀 Potential Future Enhancements (Stretch Goals)

* **API Integration:** Pull real-time cryptocurrency data using APIs like CoinGecko or CoinMarketCap.
* **NLP (Natural Language Processing):** Integrate libraries like NLTK or spaCy to understand a wider range of natural language queries and improve intent recognition.
* **Expanded Dataset:** Include more cryptocurrencies and data points.
* **User-Specific Profiles:** Allow users to set their risk tolerance or investment preferences.
* **More Sophisticated Scoring:** Develop more complex algorithms for ranking and recommending cryptocurrencies.
* **Web Interface:** Create a simple web interface using Flask or Django for easier access.

## 📜 License

This project is for educational purposes. Feel free to use, modify, and distribute the code. No specific license is attached, but attribution is appreciated if you build upon it.
