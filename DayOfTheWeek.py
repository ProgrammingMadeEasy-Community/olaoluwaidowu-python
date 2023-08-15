"""
    Author: Olaoluwa Idowu
    Date: 15-08-23
    Title: PME-DaysOfTheWeek task2
"""


# import library
from enum import Enum


# enum of days of the week
class weekdays(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


# method 1 to display the corresponding day of the week
def DaysOfTheWeek(weekday):
    return weekdays(weekday).name


# method 2 to handle 2 or 3 inputs
def DaysOfTheWeek_2(list_of_days):
    
    days_dict = {}
    
    for weekday in list_of_days:

        # check if user inputs are between 1-7
        if weekday < 1 or weekday > 7:
            return False

        # call method 1 and
        # fill up the dictionary to store the days and their counts
        if DaysOfTheWeek(weekday) in days_dict:
            days_dict[DaysOfTheWeek(weekday)] += 1
        else:
            days_dict[DaysOfTheWeek(weekday)] = 1

    return days_dict


def main():

    # loop to handle user input, reiterates if user input does not meet requirements
    while True:

        # ask user for input
        user_input  = input("Input weekday or days (1-7): ")
        input_count = len(str(user_input))

        # ensure user enters whole number or numbers
        try:
            user_input = int(user_input)
        except Exception as e:
            print(f"enter whole number(s): {e}\n")
            continue
        
        

        # reiterate if user enters more than 3 numbers
        if input_count > 3:
            print("Do not enter more than three whole numbers\n")
            continue
        
        # call method 1 if user enters one digit
        elif input_count == 1:
            if user_input > 0 and user_input < 8:
                print(DaysOfTheWeek(user_input))
                break
            else:
                print("Please enter number between 1-7\n")
                continue
        else:
            # handle 2 or 3 entries
            try:
                list_of_days = [int(x) for x in str(user_input)]
            except ValueError:
                print("Enter postive number\n")
                continue

            # call method 2
            if DaysOfTheWeek_2(list_of_days):
                print(DaysOfTheWeek_2(list_of_days))
                break
            else:
                print("Please enter number between 1-7\n")
                continue


# call main function
if __name__ == "__main__":
    main()

