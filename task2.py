
def welcome():
    in_name = input("Input Your Name: ")
    check_inp_str(in_name)

    in_age = input("Input your Age: ")
    check_inp_int(in_age)

    in_place = input("Input your home place: ")
    check_inp_str(in_place)

    in_num = input("Input your phone nunmber: ")
    check_inp_int(in_num)

    print(in_name, in_age, in_place, in_num)
    print("Thank u for register to this page")

def check_inp_str(input):
    try:
        is_ok = int(input)
        print("Wrong input")
        exit()
    except ValueError:
        print("Continue")

def check_inp_int(input):
    try:
        is_ok = int(input)
        print("Continue")
    except ValueError:
        print("Wrong input")
        exit()

welcome()