#!/usr/bin/env python3
# Lesson 3 - Mailroom... part 1

donations = [ ["Bill Gates", 10.50], ["Bill Gates", 123.45], ["Bill Gates",    1111.11], ["Jeff Bezos", 7.65], ["Jeff Bezos", 1000], ["Paul Allen", 145.90], ["John Nordstrom", 45.67], ["John Nordstrom", 6519.65], ["Mark Zuck", 789.12] ]


### Function Definitions ###
def prompt(which = 0):
    if which == 0:
        response = input("Welcome Chris! What would you like to do?\n(S)end a Thank You / (C)reate a Report / (Q)uit\n--> ")
    else:
        response = input("What would you like to do next?\n(S)end a Thank You / (C)reate a Report / (Q)uit\n--> ")

    while True:
        if response == "S":
            send_thank_you()
            break
        elif response == "C":
            print_report()
            break
        else:
            print("Goodbye Sir!")
            break


def send_thank_you():
    response = input("Please enter full name of person you'd like to thank:\nBy the way, you can also type 'list' to get a list of donors or 'Q' to quit\n--> ")

    if response == "list":
        print()
        list_donors()
        send_thank_you()
    elif response not in donor_names():
        new_donor = response
        donation_response = input(f"Please enter a donation amount for {new_donor}: ")
        donations.append([new_donor, float(donation_response)])
        print_email(new_donor, donation_response)
    else:
        donor = response
        donation_response = input(f"Please enter a donation amount for {donor}: ")
        donations.append([donor, float(donation_response)])
        print_email(donor, donation_response)


def print_email(donor, amount):
    print()
    print(f"Dear {donor},\nThank you so very much for you kind donation of ${amount}. We can assure you that it will be put to great use.\nBest,\nChris")
    print()
    prompt(1)


def list_donors():
    donor_list = donor_names()

    print("List of donors:")
    for i in donor_list:
        print(i)

    print()


def donor_names():
    name_list = []
    for i, j in donations:
        if i not in name_list:
            name_list.append(i)

    return name_list


def print_report():
    header = '{:20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print("-" * 68)

    for name in donor_names():
        print('{:20}${:>15.2f}{:>15}{:>15.2f}'.format(name, total_given(name), num_gifts(name), avg_gift(name)))

    print()
    prompt(1)


def total_given(donor):
    sum = 0
    for i, j in donations:
        if i == donor:
            sum += j
    return sum

def num_gifts(donor):
    count = 0
    for i, j in donations:
        if i == donor:
            count += 1
    return count

def avg_gift(donor):
    return (total_given(donor)/num_gifts(donor))
