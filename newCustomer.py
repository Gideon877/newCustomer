newCustomer = input("New customer? (Y/N) ")


def castle():
    #Castler | adult = R75, R25

    qtyAdults= int(input("How many adults? "))
    qtyKidsInput = int(input("How many kids? "))

    qtyKids = qtyAdults - qtyKidsInput;  # -1

    if (qtyKids < 0):
        qtyKids = qtyKids * (-1);


        if (qtyAdults >= 0 and qtyKids >= 0):
            totalPrice = (qtyAdults * 75) + (qtyKids * 25);
            print("Total cost for ", qtyAdults, "adult(s) and ", qtyKidsInput, " children for Castle: R", totalPrice);

        else:
            print('Invalid input');

def cableCar():
    #Cable Car | adult = R150, R100

    qtyAdults = int(input("How many adults? "))
    qtyKidsInput = int(input("How many kids? "))

    qtyKids = qtyAdults - qtyKidsInput;  # -1

    if (qtyKids < 0):
        qtyKids = qtyKids * (-1);


        if (qtyAdults >= 0 and qtyKids >= 0):
            totalPrice = (qtyAdults * 150) + (qtyKids * 100);
            print("Total cost for ", qtyAdults, "adult(s) and ", qtyKidsInput, " children for Cableway: R", totalPrice);

        else:
            print('Invalid input');

def aquarium():
    # Aquarium: Adult R150 and Kid R60
    qtyAdults = int(input("How many adults? "))
    qtyKidsInput = int(input("How many kids? "))

    qtyKids = qtyAdults - qtyKidsInput;  # -1

    if (qtyKids < 0):
        qtyKids = qtyKids * (-1);

        if (qtyAdults >= 0 and qtyKids >= 0):
            totalPrice = (qtyAdults * 150) + (qtyKids * 60);
            print("Total cost for ", qtyAdults, "adult(s) and ", qtyKidsInput, " children for Aquarium: R", totalPrice);

        else:
            print('Invalid input');

def kisternbosch():

    #Kirstenbosch | adult = R50, R15

    qtyAdults = int(input("How many adults? "))
    qtyKidsInput = int(input("How many kids? "))

    qtyKids = qtyAdults - qtyKidsInput;  # -1

    if (qtyKids < 0):
        qtyKids = qtyKids * (-1);


        if (qtyAdults >= 0 and qtyKids >= 0):
            totalPrice = (qtyAdults * 50) + (qtyKids * 15);
            print("Total cost for ", qtyAdults, "adult(s) and ", qtyKidsInput, " children for Kirstenbosch: R", totalPrice);

        else:
            print('Invalid input');

if (newCustomer == 'Y' or newCustomer == 'y'):
    location = input("A = Aquarium | B = Cable Car | C = Castle | K = Kirstenbosch \nX = Stop\nEnter location: ")

    if (location == 'A' or location == 'a'):
        aquarium()
    elif (location == 'B' or location == 'b'):
        cableCar()
    elif (location == 'C' or location == 'c'):
        castle()
    elif (location == 'K' or location == 'k'):
        kisternbosch()

    else:
        print("Invalid option")

elif (newCustomer == 'N' or newCustomer == 'n'):
    print()

else:
    newCustomer = input("Invalid option, please enter y or n ")
