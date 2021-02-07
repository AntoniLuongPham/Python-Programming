# Yeu cau:
# Chuong trinh nghi ra mot so bat ky tu 0 den 10 (doan code nay da duoc viet
# san cho hoc sinh).
# Chuong trinh sau do cho phep cguoi choi doan toi da 3 lan
# Neu nguoi choi doan dung, chuong trinh in ra 'Dung roi!' va thoat
# (chu D viet hoa)
# Neu nguoi choi doan so thap hon so chuong trinh nghi ra, chuong trinh in ra
# 'Thap qua!' (chu T viet hoa)
# Neu nguoi choi doan so cao hon so chuong trinh nghi ra, chuong trinh in ra
# 'Cao qua!' (chu C viet hoa)

# answer la so ngau nhien tu 0 den 10 duoc may tinh tu dong sinh ra
# Goi y: Tuong tu nhu code cua giang vien

# TODO: Hoc sinh chi duoc lap trinh tu dong lenh nay tro xuong

import random
answer = random.randint(0, 10)
print("To dang nghi den 1 so nguyen nam trong khoang 0 den 10.")

counter = 0

while counter < 3:
    choice = int(input('Do ban biet to dang nghi den so nao? '))

    if choice < answer:
        print('Thap qua!')

    elif choice > answer:
        print('Cao qua!')

    else:
        print('Dung roi!')
        break

    counter += 1
