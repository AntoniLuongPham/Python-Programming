# Yeu cau:
# Hoc sinh hien thuc ham sort_profile_high_to_low voi 1 tham so:
#  - students: la mang chua cac tu dien, moi tu dien luu thong tin cua mot ban
# hoc sinh
# Ham search_profile_with_better_score tra ve mang chua ten cac ban hoc sinh
# co diem
# mon tin hoc duoc sap xep theo thu tu diem so giam dan

# Goi y:
# - Dung mot mang ten ordered_list de luu danh sach ten cac ban duoc sap xep
# diem tu cao xuong thap
# - Tim ban co diem so cao nhat trong mang students, them ten ban vao danh sach
# ordered_list bang ham append()
# - Xoa ban co diem so cao nhat do ra khoi mang students bang lenh remove()
# - Lap lai cho den khi mang students khong con phan tu nao ca thi dung lai

# Luu y: code duoc nop chi bao gom ham sort_profile_high_to_low
def find_max(students):
    m = None
    for i in students:
        if (m is None) or (i['score'] > m['score']):
            m = i
    return m


def sort_profile_high_to_low(students):
    result = []

    while len(students) > 0:
        m = find_max(students)
        result.append(m['name'])
        students.remove(m)

    return result


# khong nop doan code ben duoi
number_of_students = int(input('Lop chung ta co bao nhieu hoc sinh nhi? '))
students = []
counter = 0
while counter < number_of_students:
    name = input('Ten cua hoc sinh so {} '.format(counter+1))
    score = int(input('Diem tin hoc cua hoc sinh so {} '.format(counter+1)))
    student = {'name': name, 'score': score}
    students.append(student)

    counter += 1

print('Danh sach hoc sinh ')
for student in students:
    print(student)
print('Hoc sinh co diem so mon tin hoc tu cao den thap la ')
print(sort_profile_high_to_low(students))
