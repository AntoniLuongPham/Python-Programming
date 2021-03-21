# Class thể hiện đối tượng Câu hỏi
# Một đối tượng Question gồm có 2 fields: 
# - question: đề bài
# - answer: đáp án
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

        
# Khai báo dữ liệu câu hỏi và đáp án
data = [
    Question("""
Một con vịt xòe ra ____ cái cánh
a. hai
b. ba
c. bốn
d. năm
""", "a"),
    Question("""
Meo meo meo rửa mặt như ____
a. Vịt
b. Hổ
c. Mèo
d. Thỏ
""", "c"), 
    Question("""
Doraemon là bạn thân của ____
a. Songoku
b. Siêu Nhân
c. Trạng Tí
d. Nobita 
""", "d")]

# In câu hỏi ra màn hình
index = 0
print(data[index].question)

# Chờ người dùng nhập câu trả lời từ bàn phím
result = input("Câu trả lời của bạn là gì?\n")

# So sánh câu trả lời với đáp án
if result == data[index].answer:
    print("Đúng rồi")
else:
    print("Sai rồi")
