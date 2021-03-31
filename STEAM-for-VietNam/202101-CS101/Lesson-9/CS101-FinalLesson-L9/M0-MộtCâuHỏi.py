# Khai báo dữ liệu câu hỏi và đáp án
question = """
Một con vịt xòe ra ____ cái cánh
a. hai
b. ba
c. bốn
d. năm
"""
answer = "a"

# In câu hỏi ra màn hình
print(question)

# Chờ người dùng nhập câu trả lời từ bàn phím
result = input("Câu trả lời của bạn là gì?\n")

# So sánh câu trả lời với đáp án
if result == answer:
    print("Đúng rồi")
else:
    print("Sai rồi")
