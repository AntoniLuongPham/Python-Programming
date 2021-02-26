# Quay lại chương trình đăng kí nhận vaccine,
# thay vì chọn bạn đầu tiên đăng kí từ mỗi thành phố,
# bạn Trẩu muốn chọn một cách ngẫu nhiên, để đảm bảo công bằng hơn.
# Chúng ta hãy cùng giúp bạn Trẩu viết chương trình này nhé.

# Yêu cầu:
# - Tạo một hàm get_random_from_each_city nhận vào một mảng có định dạng như sau:
# ["student_1,city1", "student_2,city2", "student_3,city1", ...]
# - Thay vì chọn bạn đầu tiên như ở trên lớp, chọn một bạn bất kỳ đến từ mỗi thành phố
# - Hàm get_random_from_each_city trả về từ điển kết quả có định dạng như sau: 
# {"city1": "student_42", "city2": "student_11", ...}

# Gợi ý:
# - Trong hàm get_random_from_each_city, đầu tiên tạo một từ điển có định dạng như sau (tương tự như bài tập cơ bản):
# {"city1": [mảng chứa tên các bạn đến từ thành phố 1], "city2": [mảng chứa tên các bạn đến từ thành phố 2], ...}
# - Tạo một từ điển mới với chứa tên thành phố và tên bạn được chọn một cách ngẫu nhiên đến từ thành phố ấy, sử dụng hàm get_random_item mà ta đã viết trong bài thực hành số 3. Định dạng của từ điển sẽ như sau:
# {"city1": "student_42", "city2": "student_11", ...}

import random


def get_random_item(items):
    return random.choice(items)


def group_by_city(applicants):
    result = {}
    for applicant in applicants:
        name, city = applicant.split(',')
        if city not in result:
            result[city] = [name]
        else:
            result[city].append(name)
    return result


def get_random_from_each_city(applicants):
    grouped_applicants = group_by_city(applicants)
    result = {}
    for city, list_of_applicants_in_that_city in grouped_applicants.items():
        result[city] = get_random_item(list_of_applicants_in_that_city)
    return result


applicants = [
    "Hoa,Ha Noi",
    "Thuy,Ho Chi Minh",
    "Thao,Nam Dinh",
    "Dung,Ha Noi",
    "Manh,Ha Noi",
    "Van,Ho Chi Minh"
]
grouped_applicants = get_random_from_each_city(applicants)
print(grouped_applicants)

# in ra {'Ha Noi': 'Manh', 'Ho Chi Minh': 'Thuy', 'Nam Dinh': 'Thao'} (thay doi theo moi lan chay vi chung ta chon ngau nhien)
