import requests
import pandas as pd
import os

print("=== Joke Generator ===")
print("1. Get a Random Joke")
print("2. Get Ten Jokes")
print("3. Exit")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)
    joke = response.json()

    print("\nSetup:", joke["setup"])
    print("Punchline:", joke["punchline"])

    save = input("\nDo you want to save this joke? (y/n): ")

    if save.lower() == "y":
        df = pd.DataFrame([joke])

        if not os.path.exists("joke"):
            os.makedirs("joke")

        df.to_csv("joke/random_joke.csv", index=False)
        print("Joke saved successfully!")

elif choice == "2":
    url = "https://official-joke-api.appspot.com/jokes/ten"

    response = requests.get(url)
    jokes = response.json()
    for i, joke in enumerate(jokes, start=1):
        print(f"\nJoke {i}")
        print("Setup:", joke["setup"])
        print("Punchline:", joke["punchline"])


    save = input("\nDo you want to save these jokes? (y/n): ")

    if save.lower() == "y":
        df = pd.DataFrame(jokes)

        if not os.path.exists("joke"):
            os.makedirs("joke")

        df.to_csv("joke/ten_jokes.csv", index=False)
        print("Jokes saved successfully!")

elif choice == "3":
    print("Thank you for using Joke Generator!")

else:
    print("Invalid choice!")