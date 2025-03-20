#Timothy Foster, 3/4/25, Initials Program

#Define the function to get user input.
def get_user_name():

    #Define the list.
    user_name = []

    #Get user input.
    user_name.append(str(input("Enter your first name.")))
    user_name.append(str(input("Enter your middle name.")))
    user_name.append(str(input("Enter your last name.")))

    #Return the variable.
    return user_name

#Define the mainline.
def main():

    #Call the above function and assign it to a new list.
    names = get_user_name()

    #Assign the first parts of the user-inputed strings to new variables.
    firstinitial = names[0][0]
    middleinitial = names[1][0]
    lastinitial = names[2][0]

    #Print the results.
    print(f"Your intials are {firstinitial}. {middleinitial}. {lastinitial}.")


if __name__ == "__main__":
    main()
