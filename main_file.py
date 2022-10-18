# Author: Aaron Canty
# Class: COMP1-DY
# Description: Week 12 Project

# Comment: I don't fully know what happened as I have been preparing.
# I will revisit this code over the summer to finish it correctly.
# Thanks a million for the semester! I have learned a lot :)

import my_functions


def main():
    MENU = "1: Show the results for a race \n" \
           "2: Add results for a race \n" \
           "3: Show all competitors by county \n" \
           "4: Show the winner of each race \n" \
           "5: Show all the race times for one competitor \n" \
           "6: Show all competitors who have won a race \n" \
           "7: Quit \n--> "

    option = my_functions.get_positive_int_in_range_min_max(MENU, 1, 7)

    while option != 7:
        if option == 1:
            print("Show the results for a race")
            my_functions.show_results_for_race()

        elif option == 2:
            print("Add results for a race")
            my_functions.add_results_to_race("Which race? ")
            runner_id, run_time = my_functions.add_results_to_race("races.txt")

        elif option == 3:
            print("Show all competitors by county")

        elif option == 4:
            print("Show the winner of each race")

        elif option == 5:
            print("Show all the race times for one competitor")

        elif option == 6:
            print("Show all competitors who have won a race")


my_functions.read_from_runners("runners.txt")
my_functions.read_from_races("races.txt")
# option2
runner_name, runner_ID = my_functions.read_from_runners("runners.txt")

# # option3
# runner_names,runner_IDs = my_functions.show_competitors_by_county()
#
# # option 4
# runner_id, run_time = my_functions.show_winners_each_race()
#
# # option 5
# runner_id, run_time = my_functions.show_racetimes_per_competitor()
# 
# # option 6
# my_functions.show_competitors_who_won_a_race()
if __name__ == '__main__':
    main()
