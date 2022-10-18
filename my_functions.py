# Some functions are placeholder functions, others have a more specific use
def get_non_empty_string(prompt):
    while True:
        answer = input(prompt)
        if len(answer) != 0:
            break

    return answer  # keep it OUTSIDE the while loop


def take_only_percentage(prompt):
    while True:
        try:
            answer = float(input(prompt))
            if 0 <= answer <= 100:
                return answer
        except ValueError:
            print("Use a number please!")


def take_only_word(prompt):
    while True:
        try:
            answer = input(prompt)
            if answer.isalpha():
                return answer
        except:
            print("Type words please!")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                break
        except:
            print("You must provide a positive whole number")

    return value


def get_positive_int_in_range_min_max(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                return value
            else:
                print(f"You must provide a positive number between {min} and {max}. No symbols")
                print()

        except ValueError:
            print("No symbols or letters, numbers only please!")
            print()


def read_floating_point(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if user_input >= 0:
                return user_input
        except ValueError:
            print("Sorry, floating point numbers only!")


def read_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= 0:
                return user_input
        except ValueError:
            print("Sorry, whole numbers only")


def read_from_races(races_file):
    connection = open(races_file)
    list_of_venues = connection.readlines()
    connection.close()
    list_of_venues = [list_of_venues[i].strip() for i in range(len(list_of_venues))]
    return list_of_venues


def read_from_runners(runners_file):
    connection = open(runners_file)
    list_runners = connection.readlines()
    connection.close()
    runner_names = []
    runner_ids = []

    for i in range(len(list_runners)):
        split_runner_list = list_runners[i].split(',')
        runner_names.append(split_runner_list[0])
        runner_ids.append((split_runner_list[1]))
        runner_ids = [runner_ids[i].strip() for i in range(len(runner_ids))]

    return runner_names, runner_ids


# a function to read whichever venue file is specified
# in the "show_results_for_race()" function.
def read_from_venue(venue_file):
    connection = open(venue_file)
    list_venue = connection.readlines()
    connection.close()
# creating two blank lists
    runner_id = []
    run_time = []
# splitting each comma separated value into its own list
    for i in range(len(list_venue)):
        split_venue_list = list_venue[i].split(',')
        runner_id.append(split_venue_list[0])
        run_time.append(int(split_venue_list[1]))
        # not used - run_time = [run_time[i].strip() for i in range(len(run_time))]

    return runner_id, run_time


def show_results_for_race():
    print('Option 1:')
    which_venue = input('Which venue do you want to see? ')
    # using the read_from_venue
    racer_ID, run_time = read_from_venue(which_venue + ".txt")

    # find index of the minimum run time
    index_of_minimum = run_time.index(min(run_time))

    # create variable for the fastest runner. Racer ID with the minumum run time
    fastest_runner = racer_ID[index_of_minimum]
    print()
    print(f"Results for {which_venue} \n"
          "==================================== \n"
          f"{racer_ID[0]} -- {run_time[0] // 60} minutes {run_time[0] % 60:>3} seconds \n"
          f"{racer_ID[1]} -- {run_time[1] // 60} minutes {run_time[1] % 60:>3} seconds \n"
          f"{racer_ID[2]} -- {run_time[2] // 60} minutes {run_time[2] % 60:>3} seconds \n"
          f"{racer_ID[3]} -- {run_time[3] // 60} minutes {run_time[3] % 60:>3} seconds \n"
          f"=================================== \n"
          f"Winner is: {fastest_runner}")
    print()
    return racer_ID, run_time


def add_results_to_race(races):
    # open the races.txt file in append mode
    file = open("races.txt", "a+")
    adding = input("What race are you adding to? ")
    # appending the location to the file
    file.write(f"\n{adding}")
    file.close()

    # this is where I unsuccessfully tried to get the runners into
    # their own lists in this function, so I could show the user the runner names
    # and give the option to add a racing time to it.
    runner_info = open("runners.txt", "a+")
    runner_list = runner_info.readlines()

    runner_id = []
    run_time = []

    for i in range(len(runner_list)):
        split_run_list = runner_list[i].split(',')
        runner_id.append(split_run_list[0])
        run_time.append(int(split_run_list[1]))
        return runner_id, run_time

    for i in range(len(runner_list)):
        run_time = int(input(f"What is the time for {runner_id[0]} ? "))

    runner_info.close()

# #option 3
# def show_competitors_by_county():
#
#
# # option 4
# def show_winners_each_race():
#
# # option 5
# def show_racetimes_per_competitor():
#
# # option 6
# def show_competitors_who_won_a_race():