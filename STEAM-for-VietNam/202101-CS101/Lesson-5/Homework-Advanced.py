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

# Gợi ý:
# - Các con có thể sử dụng Stack để lưu lại các giá trị đã thấy.
# - Khi đi qua các ký tự dấu ngoặc, khi gặp dấu đóng ngoặc,
# chúng ta phải kiểm tra xem ký tự ngay trước đấy có phải là
# dấu mở ngoặc tương ứng không.
# - Nếu không phải, vậy chuỗi dấu ngoặc này không chính xác,
# vậy chúng ta có thể trả về False và kết thúc hàm
#   - Nếu phải, con có thể xóa đi cặp dấu ngoặc đấy,
#   và tiếp tục xem tới các ký tự tiếp theo
#   - Một trường hợp đặc biệt là khi gặp dấu ngoặc đóng,
#   mà stack của chúng ta trống, vậy là chuỗi ký tự cũng không chính xác rồi.
# - Và cuối cùng, các con nhớ kiểm tra stack. Nếu trong stack còn các
# dấu ngoặc mở, mà chúng ta đã hết tất cả các dấu ngoặc đóng,
# vậy là chuỗi ký tự cũng không chính xác rồi.


def check_valid_parentheses(text):
    valid_opening = {')': "(", "]": "[", "}": "{"}

    opening_brackets_stack = []

    # iterate over text
    for char in text:
        # if the char is one of these "(", "[", "{"
        # then push it to opening_brackets_stack
        if char in valid_opening.values():
            opening_brackets_stack.append(char)

        # if the char is one of these ")", "]", "}"
        elif char in valid_opening.keys():
            # if there is no opening bracket left in opening_brackets_stack
            # then the text is invalid
            if opening_brackets_stack == []:
                return False

            else:
                # then pop the top of opening_brackets_stack
                opening_bracket = opening_brackets_stack.pop()

                # then check if that opening bracket is the correct opening
                # for char,
                # if not correct then the text is invalid
                if opening_bracket != valid_opening[char]:
                    return False

    # if opening_brackets_stack is empty then the text is valid
    return opening_brackets_stack == []


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
