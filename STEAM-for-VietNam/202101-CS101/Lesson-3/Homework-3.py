# Ta có thể sử dụng hàm remove() để loại bỏ một phần tử ra khỏi mảng.

# Ví dụ:
# thuc_an_trong_tu_lanh = ["trung", "kem", "banh hamburger", "xuc xich"]
# thuc_an_trong_tu_lanh.remove("kem")
# print(thuc_an_trong_tu_lanh)

# Bạn hãy viết hàm “remove_max” nhận vào một mảng các con số và loại bỏ số lớn
# nhất ra khỏi mảng đó.

# Gợi ý: bạn hãy sử dụng hàm “find_max” mà bạn vừa làm ở bài tập trước
def find_max(number_array):
    m = None
    for i in number_array:
        if (m is None) or (i > m):
            m = i
    return m


def remove_max(number_array):
    number_array.remove(find_max(number_array))
    return number_array


print(find_max([4, 1, 5, 2, 3, 7]))

print(find_max([100, 33, 88, 44, 99]))

print(remove_max([4, 2, 5, 9, 3, 7]))  # in ra [4, 2, 5, 3, 7]

print(remove_max([100, 88, 44, 22, 66, 99]))  # in ra [88, 44, 22, 66, 99]

print(remove_max([0, 1, 2, 3, 4, 5]))  # in ra [0, 1, 2, 3, 4]
