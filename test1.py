pass_credit = 0
defer_credit = 0
fail_credit = 0


def users():
    credit_range = (0, 20, 40, 60, 80, 100, 120)
    while True:
        try:
            global pass_credit
            pass_credit = int(input("Enter the no:of pass credits"))
            if pass_credit not in credit_range:
                print("Range Error")
            else:
                break
        except ValueError:
            print("Integers Required")  # displaying the value error
    while True:
        try:
            global defer_credit
            defer_credit = int(input("Enter the no:of defer credits"))
            if defer_credit not in credit_range:
                print("RangeError")
            else:

                break
        except ValueError:
            print("Integers Required")
    while True:
        try:
            global fail_credit
            fail_credit = int(input("Enter the no:of fail credits"))
            if fail_credit not in credit_range:
                print("Range Error")
            else:
                break
        except ValueError:
            print("Integers Required")


progress = 0
Trailing = 0
retriver = 120
exclude = 0

stop = ""
while stop != "q":
    users()

    while pass_credit + defer_credit + fail_credit != 120:
        print("Total incorrect")
        users()
    if pass_credit == 120:
        print("progress\n")
        progress += 1
    elif pass_credit == 100:
        print("progress-module trailer\n")
        Trailing += 1
    elif pass_credit == defer_credit >= 60:
        print("do not progress-module retriever\n")
        retriver += 1
    else:
        print("Exclude\n")
        exclude += 1

        stop = input("Enter q or Q to quit the program\nor press enter to continue\n:")
        stop = stop.lower()

print("\n________________________________________________________________________\n")

# Horizontal Histogram Code40

print(" Progress  Trailing  Retriver Exclude")


class Trailing(list):
    pass

    class ListClass(list):
        def __init__(self, *args):
            super().__init__(self, *args)
            self.append('progress,trailing,retriver,exclude')
            self.name = 'histogram_list'


    if progress > 0:
        print("\n*", end="")
    else:
        print("", end="")
    progress -= 1
    if Trailing >0:
        print("\n*", end="")
    else:
        print("", end="")
    Trailing -= 1

    if retriver >120:
        print("\n*", end="")
    else:
        print("", end="")
    retriver -= 1

    if exclude > 0:
        print("\n*", end="")
    else:
        print("", end="")
    exclude -= 1

print()