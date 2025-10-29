def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    string_list = x.split(",")
    float_list = []
    for string in string_list:
        float_num = float(string)
        float_list.append(float_num)
    return (float_list)

    # floats = [float(i) for i in y]
    # print (floats)
    # return (floats)

def calc_average(list):
    average = sum(list)/len(list)
    print (average)
    return (average)

def find_min_max(list):
    min_max = []
    min_max.append(min(list))
    min_max.append(max(list))
    print (min_max)
    return (min_max)

def sort_temperature():
    
    print("sort_temperature")

def calc_median_temperature(list):
    if len(list) % 2 == 1:
        index = int((len(list) / 2) - 0.5)
        median = list[index]
    else:
        index = int(len(list) / 2)
        median = (list[index] + list[index - 1]) / 2
    print(median)

def main():
    print ("ET0735 (DevOps for AIot) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature()
    calc_median_temperature(num_list)
    

if __name__ == "__main__":
    main()