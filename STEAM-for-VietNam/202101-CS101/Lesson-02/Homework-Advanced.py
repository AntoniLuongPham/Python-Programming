# Yeu cau: (Xem tren LMS)
# Goi y:
# Tao mot mang gom 52 phan tu de chua 2 bang chu cai
# Dung mang moi tao de ma hoa va giai ma
# Dung cau lenh ord() de chuyen ki tu sang ma ASCII
# Them ki tu vao chuoi bang cach dung phep cong:
#     Vi du: Muon them ki tu 'A' vao chuoi plaintext = 'ABC'
#     plaintext = plaintext + 'A'
#     Ket qua: plaintext se tro thanh 'ABCA'

# Hoc sinh chi nop ham caesar_encrypt() va ham caesar_decrypt()
# TODO: Ham caesar_encrypt(text, k) ma hoa chuoi ki tu text bang cach dich sang
# phai k ki tu
def caesar_encrypt(text, k):
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    plaintext = ''
    for letter in text:
        letter = letters[ord(letter) - 65 + k]
        plaintext = plaintext + letter

    return plaintext


# TODO: Ham caesar_decrypt(text, k) giai ma chuoi ki tu text bang cach dich
# sang trai k ki tu
def caesar_decrypt(text, k):
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    plaintext = ''
    for letter in text:
        letter = letters[ord(letter) - 65 - k]
        plaintext = plaintext + letter

    return plaintext


# Chi nop doan code phia tren dong lenh nay
# Cac cau lenh duoi day chi giup hoc sinh kiem tra bai lam truoc khi nop bai

# Ket qua mong muon khi chay cau lenh nay la VTCW
print(caesar_encrypt('TRAU', 2))

# Ket qua mong muon khi chay cau lenh nay la TRAU
print(caesar_decrypt('VTCW', 2))
