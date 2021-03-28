import random
# Class thể hiện đối tượng Câu hỏi
# Một đối tượng Question gồm có 2 fields: 
# - question: đề bài
# - answer: đáp án
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

        
# Class thể hiện trạng thái hiện tại của trò chơi
class GameState:
    # Điểm số hiện tại
    score = 0
# Khởi tạo đối tượng cụ thể lưu trạng thái của trò chơi
state = GameState()

# Khai báo dữ liệu câu hỏi và đáp án
def read_data():
    # Đọc câu hỏi và đáp án từ Files.
    # Số lượng câu hỏi
    num_questions = 6
    # Ban đầu, mảng dữ liệu là trống
    data = []
    # Các file câu hỏi đánh số là q1.txt, q2.txt, q3.txt,...
    # Các file câu trả lời đánh số là a1.txt, a2.txt, a3.txt,...
    # Ta dùng hàm range(1, x + 1) để duyệt qua các số 1, 2, ..., x
    for i in range(1, num_questions + 1):
        # Đọc câu hỏi, dùng encoding='utf-8' để đọc tiếng Việt
        filename = 'q' + str(i) + '.txt'
        f = open(filename, 'r', encoding='utf-8')
        question = f.read()
        f.close()    
        
        # Đọc đáp án
        filename = 'a' + str(i) + '.txt'
        f = open(filename, 'r', encoding='utf-8')
        answer = f.read()
        f.close()    

        # Tạo đối tượng Question và thêm vào mảng dữ liệu data
        data.append(Question(question, answer))
    # Trả về mảng dữ liệu data     
    return data


# In câu hỏi ra màn hình
def ask_question(question):
    # In ra dấu * ngăn cách giữa hai câu hỏi
    print("***************************")
    print(question.question)
    result = input("Câu trả lời của bạn là gì?\n")
    # So sánh kết quả của người chơi nhập vào với đáp án
    check_result(result, question.answer)
# So sánh câu trả lời với đáp án
def check_result(result, answer):
    if result == answer:
        # Cộng điểm nếu người chơi trả lời đúng
        state.score += 10
        print("Đúng rồi")
    else:
        print("Sai rồi")

    print("Điểm hiện tại của bạn là: ", state.score)

data = read_data()        
# Xáo trộn các câu hỏi một cách ngẫu nhiên
random.shuffle(data)
for question in data:
    ask_question(question)

