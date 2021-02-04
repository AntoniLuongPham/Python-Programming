# Viết hàm find_max nhận vào một mảng các con số và trả về số lớn nhất

def find_max(number_array):
    m = None
    for i in number_array:
        if (m is None) or (i > m):
            m = i
    return m


print(find_max([4, 1, 5, 2, 3, 7]))

print(find_max([100, 33, 88, 44, 99]))
