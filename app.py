import argparse
import os
from dotenv import load_dotenv
import tweepy
from openai import OpenAI

load_dotenv()

def main(args):
    print(f"Number: {args.n}")
    n = args.n

    api_key_secret = os.getenv('API_KEY_SECRET')
    api_key = os.getenv('API_KEY')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret= os.getenv('ACCESS_TOKEN_SECRET')

    Client = tweepy.Client(consumer_key=api_key,consumer_secret=api_key_secret,access_token=access_token,access_token_secret=access_token_secret)
    
    for i in range(n):
        prompt = "You're a viral tweet generator which returns a viral tech tweet without hastags, quotes or exclamation mark. The reply should only be tweet which can be directly copy-pasted."
        tweet = chat(prompt)
        print(tweet)
        Client.create_tweet(text=tweet)


def chat(user_message):

    openai_client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY'),
    )

    try:
        response = openai_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="gpt-4o-mini",
        )
        reply = response.choices[0].message.content
        return(reply)
    except Exception as e:
        print(f"Error: {e}")
        return 'Abort'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some parameters.")
    parser.add_argument('--n', type=int, required=True, help='Number of tweets')

    args = parser.parse_args()
    main(args)