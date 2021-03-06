import random


# Function go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please tytpe either <enter> or an " \
                      "or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to 
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # If response
            except ValueError:
                print(round_error)
                continue

            return response



def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and pit choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item 
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

                # output error if item not in list 
                print(error)
                print()


# Main routine gose here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0
choose_instruction = "Please choose rock (r) , paper  (p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode 
rounds = check_rounds()
 
end_game = "no"
while end_game == "no":

    # Start of game Loop

    # Round Heading 
    print()
    if rounds == "":
         heading = "Continuous Mode: " \
                    "Round {}".format(rounds_played + 1)
    else:
         heading =  "Round {} of " \
                    "{}".format(rounds_played + 1, rounds)
     
    print(heading)
    choose_instruction = "Please choose rock (r), " \
                         "paper (p) or scissors (s) " \
                         "or 'xxx' to exit"
    choose_error = "Please choose from rock " \
                   "paper / scissors (or xxx to quit)"

    # Ask user for choice and check it's valid
    choose = choose_instruction(choose_instruction, rps_list,
                                 choose_error)
    
    # get computerm choice 
    
    # compare choices
    
    # End game if exit code is typed
    if choose == "xxx":
        break
