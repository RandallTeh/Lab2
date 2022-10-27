def display_main_menu():
    x = input("Enter some numbers separated by commas (e.g. 5, 67, 32): ")
    return x


def get_user_input(x):
    user_input = x.split(",")
    floats = [float(item) for item in user_input]  # list comprehension
    return floats


def calc_average(floats):
    average = sum(floats) / len(floats)
    average = round(average, 2)
    print(average)


def find_min_max(floats):
    min_value = min(floats)
    max_value = max(floats)

    print("Lowest temp is: " + str(min_value))
    print("Highest temp is: " + str(max_value))
    print("find_min_max")

'''
def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")
'''

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    x = display_main_menu()
    num_list = get_user_input(x)
    calc_average(num_list)
    find_min_max(num_list)
#    sort_temperature()
#    calc_median_temperature()


if __name__ == "__main__":
    main()