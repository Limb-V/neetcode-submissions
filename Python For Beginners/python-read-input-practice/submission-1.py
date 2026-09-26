def add_two_numbers() -> int:
    user_input = input()
    numbers = user_input.split(",")
    val = 0
    for i in numbers:
        val += int(i)
    return val



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
