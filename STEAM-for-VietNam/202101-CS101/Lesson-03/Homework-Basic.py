# Yeu cau:
# Hoc sinh hien thuc ham search_profile_with_better_score voi 2 inputs
#  - students: la mang chua cac tu dien, moi tu dien luu thong tin cua mot ban hoc sinh
#  - score: diem so mon tin hoc
# Ham search_profile_with_better_score tra ve mang chua ten cac ban hoc sinh co diem
# mon tin hoc cao hon score

# Goi y:
# - Co the dung ham append() de them mot phan tu vao trong mang

# Luu y: code duoc nop chi bao gom ham search_profile_with_better_score
def search_profile_with_better_score(students, score):
    # filtered list, initialized as empty
    result = []

    # iterate over original list
    for student in students:
        # check if member of list is "good" or satisfies a condition
        if student['score'] > score:
            # append "good" member to filtered list
            result.append(student['name'])

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
print('Hoc sinh co diem so mon tin hoc cao hon 8 la ')
print(search_profile_with_better_score(students, 8))
