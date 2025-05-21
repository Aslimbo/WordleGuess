# WordleGuess
This project is a sample of Votee Wordle-like game API. It has three endpoints. So everyone can quickly submit guesses to daily guess, random guess and custome word guess.

# Project overview 

- **Votee Wordle APi**: Offering a Wordle game. Providing endpoints.
- This python client library handle the http requests and parses the JSON fb into py data structures.

## API Features

1. **Daily Guess**
    --**Endpoint** : 'Get /daily'

2. **Random Guess**
    --**Endpoint** : 'Get /random'

1. **Word Guess**
    --**Endpoint** : 'Get /word/{word}'

'''jsonc
[
    {
        "slot" : 0,
        "guess" : "apple",
        "result" : "present"    //Feedback ： "absent" | "present" | "correct"
    }
]

