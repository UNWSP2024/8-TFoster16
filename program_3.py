#Timothy Foster, 3/17/25, Capital Quiz Program

#Make a dictionary with the capitals.
capitals = {
   1: "Montgomery",
   2: "Juneau",
   3: "Phoenix",
   4: "Little Rock",
   5: "Sacramento",
   6: "Denver",
   7: "Hartford",
   8: "Dover",
   9: "Tallahassee",
   10: "Atlanta",
   11: "Honolulu",
   12: "Boise",
   13: "Springfield",
   14: "Indianapolis",
   15: "Des Moines",
   16: "Topeka",
   17: "Frankfort",
   18: "Baton Rouge",
   19: "Augusta",
   20: "Annapolis",
   21: "Boston",
   22: "Lansing",
   23: "St. Paul",
   24: "Jackson",
   25: "Jefferson City",
   26: "Helena",
   27: "Lincoln",
   28: "Carson City",
   29: "Concord",
   30: "Trenton",
   31: "Santa Fe",
   32: "Albany",
   33: "Raleigh",
   34: "Bismarck",
   35: "Columbus",
   36: "Oklahoma City",
   37: "Salem",
   38: "Harrisburg",
   39: "Providence",
   40: "Columbia",
   41: "Pierre",
   42: "Nashville",
   43: "Austin",
   44: "Salt Lake City",
   45: "Montpelier",
   46: "Richmond",
   47: "Olympia",
   48: "Charleston",
   49: "Madison",
   50: "Cheyenne"
}

#Make a dictionary with the states.
states = {
   1: "Alabama",
   2: "Alaska",
   3: "Arizona",
   4: "Arkansas",
   5: "California",
   6: "Colorado",
   7: "Connecticut",
   8: "Delaware",
   9: "Florida",
   10: "Georgia",
   11: "Hawaii",
   12: "Idaho",
   13: "Illinois",
   14: "Indiana",
   15: "Iowa",
   16: "Kansas",
   17: "Kentucky",
   18: "Louisiana",
   19: "Maine",
   20: "Maryland",
   21: "Massachusetts",
   22: "Michigan",
   23: "Minnesota",
   24: "Mississippi",
   25: "Missouri",
   26: "Montana",
   27: "Nebraska",
   28: "Nevada",
   29: "New Hampshire",
   30: "New Jersey",
   31: "New Mexico",
   32: "New York",
   33: "North Carolina",
   34: "North Dakota",
   35: "Ohio",
   36: "Oklahoma",
   37: "Oregon",
   38: "Pennsylvania",
   39: "Rhode Island",
   40: "South Carolina",
   41: "South Dakota",
   42: "Tennessee",
   43: "Texas",
   44: "Utah",
   45: "Vermont",
   46: "Viriginia",
   47: "Washington",
   48: "West Virginia",
   49: "Wisconsin",
   50: "Wyoming"
}

#Define the function.
def how_many_questions():

    #Get user input for number of questions.
    number_of_questions = input("How many states would you like to be quizzed on?")

    #If the input isn't a number, run the main function again and quit this iteration.
    if number_of_questions.isnumeric() == False:
        print("You must enter a positive integer.")
        main()
        quit()

    #Return the value if it is a number.
    else:
        return number_of_questions

#Define the main function.
def main():

    #Import the random module.
    import random

    #Assign the questions variable to the user response from the other function.
    questions = int(how_many_questions())

    #Define the variables.
    correct_questions = 0
    incorrect_questions = 0

    #Print instructions.
    print("Enter the states with proper capitalization and punctuation. 'St. Paul,' for instance, is the correct way to type out the capital of Minnesota.")

    #Run a for loop to do each question.
    for counter in range(questions):

        #Get a random number.
        number = random.randint(0,49)

        #Get the user's answer.
        answer = input(f"What is the capital of {states[number]}?")

        #If the answer is correct, print positive results and add to the number of correct questions.
        if answer == capitals[number]:
            print("Good job! That was correct.")
            correct_questions += 1

        #If the answer is incorrect, print negative results and add to number of incorrect questions.
        else:
            print(f"Too bad. That was incorrect. The correct response was {states[number]}.")
            incorrect_questions += 1

    #Print the results.

    print(f"In your quiz of {questions} questions, you answered {correct_questions} questions correctly and {incorrect_questions} questions incorrectly.")



if __name__ == "__main__":
    main()

