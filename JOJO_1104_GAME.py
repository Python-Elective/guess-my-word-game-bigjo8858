import string
import random
WORDLIST_FILENAME = "word_list.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list


def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    result = ''

    for i in secret_word:
        if i in letters_guessed:
            result += i

    if result == secret_word:
        return True
    return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''

    String = ""
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            String += secret_word[letter]
        else:
            String += "_"

    return String


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_character = string.ascii_lowercase
    for letters in letters_guessed:
        all_character = all_character.replace(letters, "")

    return all_character


def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Let the game begin!")
    print("I am thinking of a word with " +
          str(len(secret_word)) + " letters.")
    count_time = 8
    available_letter = string.ascii_lowercase
    result = get_guessed_word(secret_word, [])
    list_answer = []
    right_answer = []
    while count_time > 0:
        print("You have " + str(count_time) + " guesses remaining.")
        print("Letters available to you: " + available_letter)
        letter_input = input("Guess a letter: ")
        list_answer.append(letter_input)
        available_letter = get_available_letters(list_answer)
        if letter_input not in secret_word:
            count_time = count_time - 1
            print("Incorrect, this letter is not in my word: " + result)
            print("\n")
        else:
            result = get_guessed_word(
                secret_word=secret_word,
                letters_guessed=list_answer
            )
            print("Correct: " + result)
            print("\n")

            if is_word_guessed(secret_word=secret_word, letters_guessed=list_answer):
                break

    if (count_time == 0):
        print("GAME OVER ! The word was " + secret_word)
    else:
        print("You WIN !")


# Test case
print("Test case problem 1")
print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
print(is_word_guessed('durian', ['h', 'a', 'c', 'd',
                                 'i', 'm', 'n', 'r', 't', 'u']))
print(is_word_guessed('carrot', ['b', 'g', 'd', 'z',
                                 'w', 'y', 'v', 'm', 'i', 'k']))
print(is_word_guessed('lettuce', ['k', 'v', 'a', 'e',
                                  'n', 'd', 'b', 'f', 'u', 'c']))
print(is_word_guessed('pineapple', []))
print(is_word_guessed('mangosteen', ['z', 'x', 'q', 'm',
                                     'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n']))

print('\n')
print("Test case problem 2")
print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
print(get_guessed_word(
    'durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))
print(get_guessed_word('grapefruit', [
      'k', 'm', 'b', 'j', 'e', 'w', 's', 'z', 'u', 'x']))

print(get_guessed_word('coconut', [
      'w', 'l', 'i', 'p', 'c', 'u', 'j', 'h', 'v', 'z']))

print(get_guessed_word('banana', []))

print(get_guessed_word('broccoli', [
      'e', 'c', 'g', 'u', 'r', 'x', 's', 'a', 'p', 'j']))


print('\n')
print("Test case problem 3")
print(get_available_letters([]))
print(get_available_letters(['r', 'y', 'd', 'u', 't']))
print(get_available_letters(['t', 'w', 'v', 'b', 'k', 'n']))
print(get_available_letters(['a']))
print(get_available_letters(
    ['p', 'r', 'f', 'd', 'k', 'h', 'c', 'a', 'i', 'y', 'w', 'b']))

print('\n')


def main():
    word_list = load_words()
    print('\n')
    secret_word = choose_word(word_list)
    game_loop(secret_word)


if __name__ == "__main__":
    main()
