import subprocess
from nltk.sentiment import SentimentIntensityAnalyzer
import emoji

def get_commits(repo_path):
    # Get the commit messages using Git
    command = ['git', 'log', '--pretty=%B']
    result = subprocess.run(command, cwd=repo_path, capture_output=True, text=True)
    commit_messages = result.stdout.split('\n')

    return commit_messages

def analyze_sentiment(message):
    # Use NLTK SentimentIntensityAnalyzer for sentiment analysis
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(message)['compound']

    return sentiment_score

def react_with_emoji(sentiment_score):
    # React with emoji based on sentiment score
    if sentiment_score >= 0.05:
        return emoji.emojize(':smile:', use_aliases=True)
    elif sentiment_score <= -0.05:
        return emoji.emojize(':disappointed:', use_aliases=True)
    else:
        return emoji.emojize(':neutral_face:', use_aliases=True)

if __name__ == "__main__":
    # Replace 'repo_path' with the path to your Git repository
    repo_path = '/path/to/your/repo'

    # Get commit messages
    commit_messages = get_commits(repo_path)

    # Analyze sentiment and react with emoji for each commit
    for message in commit_messages:
        sentiment_score = analyze_sentiment(message)
        reaction = react_with_emoji(sentiment_score)
        print(f"Commit Message: {message}\nSentiment Score: {sentiment_score}\nReaction: {reaction}\n")
