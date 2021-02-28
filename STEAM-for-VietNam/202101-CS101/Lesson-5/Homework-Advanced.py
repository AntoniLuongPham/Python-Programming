# Bài tập nâng cao

# Một ứng dụng nữa của Stack là để kiểm tra xem một chuỗi các dấu ngoặc
# có chính xác hay không.

# Chuỗi dấu ngoặc chính xác phải đáp ứng được 2 yêu cầu sau:
# - Dấu ngoặc mở phải được đóng bằng dấu ngoặc cùng loại
# (Dấu "(" phải được đóng bằng ")", dấu "[" được đóng bằng "]",
# và dấu "{" được đóng bằng "}")
# - Các dấu ngoặc phải được đóng đúng theo thứ tự mà nó được mở.

# Yêu cầu:
# - Viết hàm check_valid_parentheses
# - Hàm nhận vào một chuỗi các dấu ngoặc
# - Hàm trả về True nếu chuỗi dấu ngoặc chính xác, và False nếu không


print(check_valid_parentheses("()"))
# True

print(check_valid_parentheses("()[]{}"))
# True

print(check_valid_parentheses("(]"))
# False

print(check_valid_parentheses("([)]"))
# False

print(check_valid_parentheses("("))
# False

print(check_valid_parentheses("{[]}"))
# True
