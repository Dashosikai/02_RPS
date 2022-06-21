# Function go here
def choice_checker(questoin):

    valid = False
    while not valid:

         # Ask user for choice
         response = input(questoin)

         if response == "r" or response == "rock":
             return response


# Main routine gose here

# Ask user for choice and check it's valid
user_choice = choice_checker("Choose rock / paper / "
                             "scissors (r/p/s): ")
                             

