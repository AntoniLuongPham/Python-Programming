teacher_list = ["Duc Ngo", "Zi Vu", "Harry Doan", "Ken Nguyen"]


def search_teacher(name):
    for teacher in teacher_list:
        if name == teacher:
            print("Đã tìm thấy thầy/cô " + name)
            break


name = input("Input a name: ")
search_teacher(name)
