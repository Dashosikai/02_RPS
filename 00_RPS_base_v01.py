import random


# Function go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please tytpe either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

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

# List of valid responses
