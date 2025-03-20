#Timothy Foster, 3/17/25, Course Info Program

#Define function.
def get_number_of_pairs():

    #Get user input for number of pairs.
    number_of_pairs = input("Enter the number of courses for which you would like to add info.")

    #Make sure the input is a positive integer.
    if number_of_pairs.isnumeric() == False:
        print("You must enter a positive integer.")
        main()
        quit()

    #Return the value.
    else:
        return number_of_pairs

#Define the main function.
def main():

    #Get the number of pairs.
    number = int(get_number_of_pairs())

    #Print instructions.
    print("The course ID should look like 'COS 2005,' while the course title should look like 'Python Programming.'")

    #Create an empty dictionary.
    courseInfo = {
    }

    #Run a for loop to allow the user to enter the course ID, course title pairs.
    for counter in range(number):
        course_ID = input("Enter the course ID.")
        course_number = input("Enter the course title.")

        #Assign the values to the dictionary above.
        courseInfo[course_ID] = course_number

    #Get the subject for which the user would like to search.
    subject_search = input("Enter the subject for which you would like to see the courses. An example would be 'COS.'")

    #Create a list of the keys in the dictionary.
    courseIDs = list(courseInfo)

    #Create another empty dictionary for the results.
    courses_with_subject = {
    }

    #Run a for loop.
    for counter in range(number):

        #Check if the course ID is of the desired subject.
        if list(courseInfo)[counter][:3] == subject_search[:3]:
            #Add the course ID, course title pair to the empty dictionary above.
            courses_with_subject[courseIDs[counter]] = courseInfo.get(courseIDs[counter])

    #Print the results.
    print(f"The following courses have the subject of {subject_search}: {courses_with_subject}")

if __name__ == "__main__":
    main()
