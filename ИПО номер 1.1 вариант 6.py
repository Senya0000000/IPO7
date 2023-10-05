array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Команда множества
max_element = max(array) # Команда приравнивает элемент к множеству
count_greater = 0 # считает большее значение
count_smaller = 0 # считает меньшее значение
for element in array:
 if element > max_element:
  count_greater += 1
 elif element < max_element:
  count_smaller += 1
print("Количество элементов, больших максимального: ", count_greater) # выводит большее значение
print("Количество элементов, меньших максимального: ", count_smaller) # выводит меньшее значение
