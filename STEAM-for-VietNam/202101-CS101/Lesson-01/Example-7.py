counter = 0

while counter < 3:
    passcode = input("Xin nhap vao mat khau: ")

    if passcode == "0042" or passcode == "2021":
        print("Chao mung ban den voi Sieu May Tinh!")
        break
    else:
        print("Mat khau sai!")

    counter = counter + 1
