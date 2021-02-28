# Bài tập cơ bản

# Như các con đã học trên lớp, Stack có thể được dùng để đảo ngược một mảng.
# Trong bài này, các con hãy viết hàm để đảo ngược một mảng

# Yêu cầu:
# - Viết hàm reverse_array
# - Hàm nhận vào một mảng
# - Hàm trả về một mảng với các ký tự trong mảng với thứ tự được đảo ngược

# Gợi ý:
# Các con hãy dùng hàm pop mà mình đã viết để lấy từng ký tự của mảng được cho.
# Sau đó, chúng ta có thể thêm từng ký tự đấy vào một mảng mới
# để đảo ngược thứ tự


def reverse_array(array):
    result = []
    for _ in range(len(array)):
        result.append(array.pop())
    return result


print(reverse_array(["o", "l", "l", "e", "h"]))
# [“h”, “e”, “l”, “l”, “o”]
print(reverse_array(["n", "a", "m", "e"]))
# [“e”, “m”, “a”, “n”]
