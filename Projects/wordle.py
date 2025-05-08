import random

# Pick a word at random
#word_list = ["ryder","prime","spray","james","green","gator","livin","soren","clark",
def read_file_to_list(file_path):
    """Reads a text file and returns a list of lines."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]  # Remove newline characters
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
         return f"An error occurred: {e}"

# Example usage:
file_path = 'Projects/words.txt' 
word_list = read_file_to_list(file_path)

if isinstance(word_list, str):
    print(word_list) # Print the error message
else:
    print(word_list) # Print the list of lines
hidden_word = random.choice(word_list)

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")