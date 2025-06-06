# Predefined cryptocurrency data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10,
        "description": "The original cryptocurrency, known for its high market capitalization but also high energy consumption."
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10,
        "description": "A leading platform for decentralized applications, transitioning to a more energy-efficient model."
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10,
        "description": "Known for its focus on sustainability and a research-driven approach to development."
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10,
        "description": "A high-performance blockchain known for its speed and low transaction fees, with a good sustainability profile."
    },
    "Polkadot": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7.5/10, # Slightly better than Solana
        "description": "Aims to enable a completely decentralized web where users are in control, with a strong focus on low energy use."
    },
    "EcoCoin": { # Fictional example for high sustainability
        "price_trend": "stable",
        "market_cap": "low",
        "energy_use": "very low",
        "sustainability_score": 9.5/10,
        "description": "A (fictional) coin designed with maximum energy efficiency and positive environmental impact in mind."
    }
}

# Chatbot's Personality
BOT_NAME = "CryptoAdvisor"
BOT_TONE_GREETING = f"Hey there! I'm {BOT_NAME}. Let’s find you a green and growing crypto! 🌿📈"
BOT_TONE_PROFESSIONAL = "Analyzing data to provide you with informed cryptocurrency insights."
BOT_DISCLAIMER = "Remember, cryptocurrency investments are risky. Always do your own thorough research before investing! This is not financial advice."

def get_crypto_details(coin_name):
    """Returns a formatted string of details for a given coin."""
    if coin_name in crypto_db:
        details = crypto_db[coin_name]
        return (f"{coin_name}:\n"
                f"  Price Trend: {details['price_trend']}\n"
                f"  Market Cap: {details['market_cap']}\n"
                f"  Energy Use: {details['energy_use']}\n"
                f"  Sustainability Score: {details['sustainability_score']*10}/10\n"
                f"  Description: {details['description']}")
    return f"Sorry, I don't have information on {coin_name}."

def recommend_by_profitability():
    """Recommends coins based on profitability rules."""
    profitable_coins = []
    for coin, data in crypto_db.items():
        # Profitability: Prioritize coins with price_trend = "rising" and market_cap = "high" or "medium".
        if data["price_trend"] == "rising" and (data["market_cap"] == "high" or data["market_cap"] == "medium"):
            profitable_coins.append((coin, data["sustainability_score"])) # Store with sustainability for tie-breaking

    if not profitable_coins:
        return "Hmm, no coins currently stand out strongly for profitability based on my current data. Market conditions might be shifting."

    # Sort by market cap (implicitly, as high/medium are selected) then by sustainability as a secondary factor
    profitable_coins.sort(key=lambda x: (crypto_db[x[0]]["market_cap"] == "high", x[1]), reverse=True)

    best_coin = profitable_coins[0][0]
    return f"For potential profitability, consider {best_coin}! It's trending up and has a solid market cap. ({get_crypto_details(best_coin)}) 🚀"

def recommend_by_sustainability():
    """Recommends coins based on sustainability rules."""
    sustainable_coins = []
    for coin, data in crypto_db.items():
        # Sustainability: Prioritize coins with energy_use = "low" or "very low" and sustainability_score > 7/10.
        if (data["energy_use"] == "low" or data["energy_use"] == "very low") and data["sustainability_score"] * 10 > 7:
            sustainable_coins.append(coin)

    if not sustainable_coins:
        return "It seems no coins currently meet the high sustainability criteria in my dataset. This is an evolving space!"

    # Find the coin with the absolute highest sustainability score among the filtered ones
    if sustainable_coins:
        recommend = max(sustainable_coins, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"For sustainability, {recommend} is a top choice! 🌱 It’s eco-friendly ({crypto_db[recommend]['energy_use']} energy use) and has a great sustainability score ({crypto_db[recommend]['sustainability_score']*10}/10). ({get_crypto_details(recommend)})"
    return "Could not find a top sustainable coin based on the criteria."


def recommend_for_long_term_growth():
    """Recommends coins based on a balance of profitability and sustainability for long-term growth."""
    candidates = []
    for coin, data in crypto_db.items():
        # Criteria for long-term growth:
        # - Price trend must be "rising" or "stable" (avoiding falling)
        # - Sustainability score should be decent (e.g., >= 6/10)
        # - Energy use should ideally not be "high"
        if (data["price_trend"] in ["rising", "stable"] and
            data["sustainability_score"] * 10 >= 6 and
            data["energy_use"] != "high"):
            # We can create a combined score, e.g., weighted average
            # Let's say sustainability is 60% weight, price trend (rising=1, stable=0.5) is 40%
            trend_score = 1 if data["price_trend"] == "rising" else 0.5
            combined_score = (data["sustainability_score"] * 0.6) + (trend_score * 0.4)
            candidates.append((coin, combined_score))

    if not candidates:
        return "I couldn't find a standout coin for long-term growth with the current data balancing profit and sustainability. Keep an eye on market developments!"

    # Sort by the combined score in descending order
    candidates.sort(key=lambda x: x[1], reverse=True)

    if candidates:
        best_coin_name = candidates[0][0]
        return (f"For long-term growth, considering both upward potential and sustainability, {best_coin_name} looks promising! "
                f"It has a price trend of '{crypto_db[best_coin_name]['price_trend']}' and a sustainability score of {crypto_db[best_coin_name]['sustainability_score']*10}/10. "
                f"({get_crypto_details(best_coin_name)}) 🚀🌱")
    return "No specific recommendation for long-term growth at the moment based on combined factors."


def chatbot_response(user_query):
    """Generates a response based on the user's query."""
    query = user_query.lower()

    if "hello" in query or "hi" in query or "hey" in query:
        return BOT_TONE_GREETING

    elif "trending up" in query or "price trend" in query or "rising" in query:
        trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending_coins:
            return f"The following cryptos are currently trending up: {', '.join(trending_coins)}. {recommend_by_profitability()}"
        else:
            return "No cryptos are listed as 'rising' in my current dataset."

    elif "sustainable" in query or "eco-friendly" in query or "green coin" in query or "sustainability score" in query:
        return recommend_by_sustainability()

    elif "profit" in query or "profitable" in query or "make money" in query :
        return recommend_by_profitability()

    elif "long-term growth" in query or "long term" in query or "future potential" in query:
        return recommend_for_long_term_growth()

    elif "details for" in query:
        try:
            # Assumes format "details for Bitcoin"
            coin_name = user_query.split("details for ")[1].strip().title() # .title() to capitalize like Bitcoin
            return get_crypto_details(coin_name)
        except IndexError:
            return "Please specify which coin you want details for, e.g., 'details for Bitcoin'."

    elif "all coins" in query or "list all" in query:
        all_info = "Here's all the crypto data I have:\n"
        for coin_name in crypto_db:
            all_info += "-------------------------\n"
            all_info += get_crypto_details(coin_name) + "\n"
        return all_info.strip()

    elif "thank you" in query or "thanks" in query:
        return f"You're welcome! Remember: {BOT_DISCLAIMER}"

    elif "bye" in query or "exit" in query or "quit" in query:
        return f"Goodbye! Happy (and safe) investing! 👋\n{BOT_DISCLAIMER}"

    else:
        return (f"Sorry, I didn't quite understand that. You can ask me about:\n"
                f"- 'Which crypto is trending up?'\n"
                f"- 'What’s the most sustainable coin?'\n"
                f"- 'Which coin is good for long-term growth?'\n"
                f"- 'Which crypto is most profitable?'\n"
                f"- 'Details for [coin name]'\n"
                f"- 'List all coins'\n"
                f"Or type 'bye' to exit.")

def start_chat():
    """Starts the chatbot interaction."""
    print(BOT_TONE_GREETING)
    print(BOT_DISCLAIMER)
    print("-" * 30)

    while True:
        user_input = input("You: ")
        if not user_input:
            print(f"{BOT_NAME}: Please say something!")
            continue

        response = chatbot_response(user_input)
        print(f"{BOT_NAME}: {response}")

        if "goodbye" in response.lower(): # Check if the bot said goodbye
            break
    print("-" * 30)

# Main execution
if __name__ == "__main__":
    start_chat()
    