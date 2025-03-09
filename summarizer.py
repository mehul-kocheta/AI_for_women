import ollama
import json
import pandas as pd

df2 = pd.read_csv(r"C:\Users\ARYAN\Downloads\final_labels.csv")
df2 = df2[df2['split'] == 'train']
unique_subreddits = df2['subreddit'].unique()

# Create a list of strings, one per subreddit
subreddit_strings = []
for subreddit in unique_subreddits:
    text_string = df2[df2['subreddit'] == subreddit]['body'].dropna().str.cat(sep='\n')
    subreddit_strings.append({subreddit:text_string})

def summarize_subreddit_posts(posts):
    with open("subreddit_summaries.txt", "a", encoding="utf-8") as f:  # Open file in append mode
        for l1 in subreddit_strings:
            # print(l1)
            posts = l1[list(l1.keys())[0]]
            # print(posts)
            response = ollama.chat(
                model='llama3.2:latest',  # or your preferred model
                messages=[
                    {
                        'role': 'user',
                        'content': f"Summarize the following Reddit posts, briefly point out what is being discussed, DONOT give your opinions just tell me about the topics being discussed about:\n\n{posts}"
                    }
                ]
            )
            summary = response['message']['content'].strip()
            print("*** Summary ***")
            print(summary)
            print("*")
            print()
            print()

            subreddit_name = list(l1.keys())[0]
            f.write(f"Subreddit: {subreddit_name}\n")
            f.write(f"Summary:\n{summary}\n\n")
            f.write("------------------------------------\n")
            f.flush()  # Ensure the content is written to the file immediately

    return "Summaries saved to subreddit_summaries.txt"

# Example usage:
subreddit_posts = [
    "I just saw a cat doing a backflip! It was amazing!",
    "What are the best tips for learning Python?",
    "Anyone else having issues with their internet today?",
    "This new movie is absolutely terrible. Do not waste your money."
]

results = summarize_subreddit_posts(subreddit_posts)

print(results)
