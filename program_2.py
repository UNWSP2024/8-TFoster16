#Timothy Foster, 3/4/25, Word Separator Program

#Define function.
def get_user_phrase():

    #Get user input.
    user_phrase = str(input('Enter a phrase without spaces but with each new word capitalized. "StopAndSmellTheRoses" would be an example.'))

    #Return the string.
    return user_phrase

#Define main function.
def main():

    #Define the phrase variable
    phrase = get_user_phrase()

    #Define the true phrase variable.
    truePhrase = ""

    #Get the number of letters in the string.
    letter_count = len(phrase)

    #Run a for loop for the number of letters.
    for i in range(letter_count):

        #If a letter in the phrase is uppercase and not the first character, there is a space added and it is made lowercase.

        if phrase[i].isupper() and i != 0:
            truePhrase = truePhrase + " "
            truePhrase = truePhrase + phrase[i].lower()

        #Otherwise, just add the character to the phrase.

        else:
            truePhrase = truePhrase + phrase[i]

#Print the results.
    print(truePhrase)

if __name__ == "__main__":
    main()
