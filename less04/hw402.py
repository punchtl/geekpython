list_number = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [list_number[i] for i in range(len(list_number)) if list_number[i - 1] < list_number[i]]

print("Исходный список: " + str(list_number))
print("Результат: " + str(new_list))
