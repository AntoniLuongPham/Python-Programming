# Yêu cầu:
# - Tạo một hàm group_by_city nhận vào một mảng có định dạng như sau:
# ["student_1,city_1", "student_2,city_2", "student_3,city_1", ...]
# - Hàm trả về một từ điển có định dạng như sau:
# {"city_1": [mảng chứa tên các bạn đến từ thành phố 1],
#  "city_2": [mảng chứa tên các bạn đến từ thành phố 2], ...}

def group_by_city(applicants):
    result = {}
    for applicant in applicants:
        name, city = applicant.split(',')
        if city not in result:
            result[city] = [name]
        else:
            result[city].append(name)
    return result


applicants = [
    "Hoa,Ha Noi",
    "Thuy,Ho Chi Minh",
    "Thao,Nam Dinh",
    "Dung,Ha Noi",
    "Manh,Ha Noi",
    "Van,Ho Chi Minh"
]
grouped_applicants = group_by_city(applicants)
print(grouped_applicants)
