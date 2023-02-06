"""EX02 - one_shot_wordle_designation."""

__author__ = "730365237"

secret_word : str = ("python")
guess : str = str(input(f"What is your {len(secret_word)}-letter guess? "))
index = 0
result = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

while index < len(secret_word):
    if secret_word[index] == guess[index]:
        result = result + GREEN_BOX
    else:
        other_index = 0
        found : bool = False
        while other_index < len(secret_word) and not found:
            if secret_word[other_index] == guess[index]:
                found = True
            else:
                other_index = other_index + 1
        if found:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    index = index + 1
print(result)

if guess != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")