import statistics


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

def sort_temperature(floats):
    asc = sorted(floats)
    return asc


def calc_median_temperature(asc):
    mn = statistics.median(asc)
    print("The Median is " + str(mn))


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    x = display_main_menu()
    num_list = get_user_input(x)
    calc_average(num_list)
    find_min_max(num_list)
    asc = sort_temperature(num_list)
    calc_median_temperature(asc)


if __name__ == "__main__":
    main()