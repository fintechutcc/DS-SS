def bubble_sort(data):
    for outer in range(len(data)-1, 0, -1):
        for i in range(outer):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]


num_list = [20, 34, 17, 19, 4]
bubble_sort(num_list)
print(num_list)