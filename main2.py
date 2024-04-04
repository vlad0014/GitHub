input_list = [1, 2, 3, 4, 5]
result_string = ''
for i in range(len(input_list)):
    result_string += str(input_list[i])
    if i != len(input_list) - 1:
        result_string += ','
print(result_string)
