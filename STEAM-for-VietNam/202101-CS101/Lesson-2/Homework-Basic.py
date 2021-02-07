# Goi y:
# Dung ham len() de biet duoc so phan tu cua mang
# Dung return de xuat ra output sau khi xet dieu kien

# TODO: Hoc sinh cai tien ham get_vaccine_score() bang cach them 2 dieu kien
# de kiem tra dat yeu cau
#       Hoc sinh chi nop ham get_vaccine_score()
def get_vaccine_score(trials):
    total = 0
    for value in trials:
        if (len(trials) < 3) or (value < 50):
            return 0

        else:
            total = total + value
    return total / len(trials)


# Chi nop doan code phia tren dong lenh nay
# Cac cau lenh duoi day chi giup hoc sinh kiem tra bai lam truoc khi nop bai

# Ket qua mong muon khi chay cau lenh nay la 64.33333333333333
print(get_vaccine_score([66, 62, 65]))

# Ket qua mong muon khi chay cau lenh nay la 0
print(get_vaccine_score([100, 100]))
