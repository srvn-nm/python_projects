def check_numbers(numbers,array_lenght):
    danger_numbers = 0
    index = 0
    while(index < array_lenght):
        for number in range(index+1,array_lenght):
            if numbers[number] * 2 < numbers[index]:
                danger_numbers -=-1
        index -=-1

    print(danger_numbers,end="")



len_of_array = int(input())
number_string_array = input()
numbers_splited = map(int , number_string_array.replace(" ",""))

numbers = list(numbers_splited)
check_numbers(numbers,len_of_array)