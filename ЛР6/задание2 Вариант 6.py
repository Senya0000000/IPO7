def multiply_positive_elements(arr):
    # Создаем новый двумерный список
    new_arr = [[x if x <= 0 else x * 2 for x in sub_arr] for sub_arr in arr]
    return new_arr
# Пример использования программы
array = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
print("Исходный массив:")
for sub_arr in array:
    print(sub_arr)
new_array = multiply_positive_elements(array)
print("Массив после перемножения положительных элементов:")
for sub_arr in new_array:
    print(sub_arr)