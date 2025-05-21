import requests
import urllib3

# skip SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Wordle API URL
Base_URL = "https://wordle.votee.dev:8000"

def guess_daily(word: str, size:int= 5):
    """
    Function to guess the daily wordle.
    :param word: The word to guess.
    :param size: The size of the word. Default is 5.
    :return: The response from the server.
    """
    params = {"guess": word, "size": size}
    url = f"{Base_URL}/daily"
    response = requests.get(url, params=params, verify=False)
    response.raise_for_status()  # Raise an error for bad responses
    # Check if the response is JSON
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Invalid response from server", "status_code": response.status_code}
    
def guess_random(word: str, size:int= 5,seed:int=None):
    """
    Function to guess a random wordle.
    :param word: The word to guess.
    :param size: The size of the word. Default is 5.
    :param seed: The seed for the random number generator. Default is None.
    :return: The response from the server.
    """
    params = {"guess": word, "size": size}
    seed = seed if seed is not None else 0
    url = f"{Base_URL}/random"
    response = requests.get(url, params=params, verify=False)
    response.raise_for_status()  # Raise an error for bad responses
    # Check if the response is JSON
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Invalid response from server", "status_code": response.status_code}
    
def guess_word(word: str, target: str):
    """
    Function to guess a wordle.
    :param word: The word to guess.
    :param target: The target word.
    :return: The response from the server.
    """
    params = {"guess": word}
    url = f"{Base_URL}/word/{target}"
    response = requests.get(url, params=params, verify=False)
    response.raise_for_status()  # Raise an error for bad responses
    # Check if the response is JSON
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Invalid response from server", "status_code": response.status_code}
    
if __name__ == "__main__":
    # Daily wordle guess
    daily = guess_daily("apple")
    print("Daily Wordle Guess:", daily)

    # Random wordle guess
    random = guess_random("apple",seed=1)
    print("Random Wordle Guess:", random)

    # Wordle guess with target
    target = "apple"    
    word = "grape"
    spe = guess_word(word, target)
    print(f"Wordle Guess for target '{target}':", spe)