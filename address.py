#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on January 2021
# This program uses functions to create
#   a mailing address


def Construct_address(addressee, street_number, street_name, city,
                      province, postal, apartment=None):
    # puts the mailing address together

    address = addressee + "\n"

    # process
    if apartment is not None:
        address = address + apartment + "-"

    address = address + street_number + " " + street_name + "\n" + \
        city + " " + province + "  " + postal

    # output
    return address


def main():
    # gets input and displays final output
    apartment = None

    addressee = input("Enter addressee: ")
    question = input("Do you have an apartment number? (yes/no): ")
    if question == 'yes':
        apartment = input("Enter apartment number: ")
    elif question != 'no':
        apartment = 'invalid'

    street_number = input("Enter street number: ")
    street_name = input("Enter street name: ")
    city = input("Enter city: ")
    province = input("Enter province: ")
    postal = input("Enter postal code: ")
    print("")

    # call function
    if apartment != 'invalid':
        if apartment is not None:
            full_address = Construct_address(addressee, street_number,
                                             street_name, city, province,
                                             postal, apartment)
        else:
            full_address = Construct_address(addressee, street_number,
                                             street_name, city, province,
                                             postal)
    else:
        print("Please enter yes or no: Do you have an apartment number?")

    # output
    print(full_address)


if __name__ == "__main__":
    main()
