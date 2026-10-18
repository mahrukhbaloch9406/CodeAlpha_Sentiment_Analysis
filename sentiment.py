print("=== CodeAlpha Sentiment Analysis ===")
print("By Mahrukh Baloch - BSIT MNSUAM\n")

# Simple AI Sentiment Logic - No library needed
positive_words = ["good", "great", "excellent", "happy", "love", "awesome", "best", "wonderful", "amazing", "nice", "beautiful", "perfect"]
negative_words = ["bad", "sad", "hate", "worst", "terrible", "awful", "poor", "boring", "angry", "disappoint", "fail", "ugly"]

def analyze_sentiment(text):
    text = text.lower()
    pos_count = sum(1 for w in positive_words if w in text)
    neg_count = sum(1 for w in negative_words if w in text)
    
    if pos_count > neg_count:
        return "Positive 😊", pos_count
    elif neg_count > pos_count:
        return "Negative 😢", neg_count
    else:
        return "Neutral 😐", 0

print("Type any sentence. Type 'bye' to exit.\n")

while True:
    user = input("You: ").strip()
    if not user:
        continue
    if user.lower() in ["bye", "exit", "quit"]:
        print("Bot: Allah Hafiz! Thanks for using sentiment analyzer.")
        break
    
    sentiment, score = analyze_sentiment(user)
    print(f"AI Result: {sentiment} (score: {score})\n")
