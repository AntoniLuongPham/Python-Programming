# Class thể hiện đối tượng Câu hỏi
# Một đối tượng Question gồm có 2 fields: 
# - question: đề bài
# - answer: đáp án
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

        
# Khai báo dữ liệu câu hỏi và đáp án
def read_data():
    return [
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
def ask_question(question):
    print(question.question)
    result = input("Câu trả lời của bạn là gì?\n")
    # So sánh kết quả của người chơi nhập vào với đáp án
    check_result(result, question.answer)
# So sánh câu trả lời với đáp án
def check_result(result, answer):
    if result == answer:
        print("Đúng rồi")
    else:
        print("Sai rồi")

data = read_data()        
ask_question(data[0])
