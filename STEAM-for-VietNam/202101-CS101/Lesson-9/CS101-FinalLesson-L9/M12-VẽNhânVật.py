import pygame
import random
import time
import turtle
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
    # Khởi động lại đồng hồ bấm giờ: cho giá trị bằng thời gian hiện tại
    def reset_timer(self):
        self.start_time = time.time()
    # Trả về thời gian trả lời câu hỏi (tính bằng giây), bằng cách lấy
    # thời gian đồng hồ trừ đi thời gian start_time đã lưu.
    def get_timer(self):
        return time.time() - self.start_time

# Khởi tạo đối tượng cụ thể lưu trạng thái của trò chơi
state = GameState()

# Dùng thư viện pygame để chơi âm thanh. 
def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
def play_sound(file):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play()
# Vẽ hình nhân vật.
avatar = turtle.Turtle()         
def draw_avatar(image):
    # Phải gọi lệnh turtle.addshape trước khi vẽ ảnh.
    turtle.addshape(image)  
    avatar.clear()
    avatar.penup()
    avatar.setposition(350, -100)
    # Lưu ý: turtle chỉ vẽ được ảnh có định dạng .gif
    avatar.shape(image)

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


# Sinh ra các câu hỏi tính nhẩm ngẫu nhiên Siêu Trí Tuệ
def generate_math_questions():
    # Ban đầu, danh sách câu hỏi trống.
    data = []
    # Số lượng câu hỏi sinh ra.
    num_questions = 3
    # Hai phép toán: cộng và nhân
    operators = ["+", "x"]    
    # Số lượng chữ số tối đa khi sinh câu hỏi ngẫu nhiên
    max_digits = 4
    for i in range(num_questions):
        # Chọn số ngẫu nhiên từ 0 đến 10^max_digits - 1
        a = random.randint(0, 10**max_digits)
        b = random.randint(0, 10**max_digits)
        # Chọn một phép toán ngẫu nhiên
        op = random.choice(operators)
        # Sinh ra đề bài
        question = str(a) + " " + op + " " + str(b) + " = ?"
        # Sinh ra đáp án
        if op == "+":
            answer = a + b
        elif op == "x":
            answer = a * b            
        # Thêm câu hỏi vào danh sách
        data.append(Question(question, str(answer)))
    # Trả về danh sách câu hỏi tính nhẩm Siêu Trí Tuệ.
    return data



# Trả về font chữ với kích thước được cho.
def get_font(font_size):
    return ("Arial", font_size, "normal")

# Khởi tạo cây bút chuyên dùng để vẽ Điểm số.
pen_score = turtle.Turtle()
def draw_score():
    # Ẩn con rùa.
    pen_score.hideturtle()
    # Nhấc bút lên.
    pen_score.penup()
    # Xoá, để khi vẽ điểm không bị đè lên nhau.
    pen_score.clear()
    # Đổi màu.
    pen_score.color('white')
    # Đặt vị trí.
    pen_score.setposition(340, 110)
    # Viết điểm số ra màn hình.
    pen_score.write(state.score, font=get_font(40))

# In câu hỏi ra màn hình
def ask_question(question):
    # In ra dấu * ngăn cách giữa hai câu hỏi
    print("***************************")
    print(question.question)
    # Xoá màn hình trước khi vẽ để chữ khỏi bị viết đè lên nhau
    turtle.clear()
    # Ẩn con rùa (hình tam giác) 
    turtle.hideturtle()
    # Nhấc bút lên (để khỏi để lại dấu vết)
    turtle.penup()
    # Đặt vị trí bút (để viết câu hỏi)
    turtle.setposition(-240, 20)
    # In câu hỏi ra màn hình Turtle và cho biết cỡ font chữ.
    turtle.write(question.question, font=get_font(15))
    # Gọi hàm viết điểm số ra màn hình.
    draw_score()
    # Vẽ hình nhân vật trạng thái bình thường 
    draw_avatar('KimNguu-normal.gif')
    # Trước khi hỏi câu hỏi mới, cần khởi động lại đồng hồ bấm giờ
    state.reset_timer()

    # Hỏi người dùng nhập câu trả lời qua giao diện Turtle
    result = turtle.textinput("Siêu Lập Trình", "Câu trả lời của bạn là gì?\n")    # So sánh kết quả của người chơi nhập vào với đáp án
    check_result(result, question.answer)
# So sánh câu trả lời với đáp án
def check_result(result, answer):
    # Thời gian người chơi trả lời câu hỏi (tính bằng giây).
    time_taken = state.get_timer()
    # Tính điểm thưởng nếu trả lời nhanh.
    if time_taken < 5:
        bonus = 5
    else:
        bonus = 0
    if result == answer:
        # Cộng điểm nếu người chơi trả lời đúng
        # Cộng điểm trả lời đúng và cả điểm thưởng nữa.
        state.score += 10 + bonus    
        # Chơi âm thanh cho biết trả lời đúng.
        play_sound("correct_answer.wav")

        # Vẽ hình nhân vật khi trả lời đúng.
        draw_avatar('KimNguu-correct.gif')
        print("Đúng rồi")
    else:
        # Chơi âm thanh cho biết trả lời sai.
        play_sound("wrong_answer.wav")

        # Vẽ hình nhân vật khi trả lời sai.
        draw_avatar('KimNguu-wrong.gif')
        print("Sai rồi")

    # Chờ một chút để thấy rõ nhân vật cử động.
    time.sleep(0.5)
    print("Thời gian trả lời câu hỏi là:", round(time_taken), "giây")
    if bonus > 0:
        print("Bạn nhận được điểm thưởng là", bonus, "vì trả lời nhanh")            
    print("Điểm hiện tại của bạn là: ", state.score)

# Thiết lập màn hình giao diện turtle
def setup_turtle():
    # Màn hình Turtle
    screen = turtle.Screen()
    # Thiết lập kích thước màn hình 
    screen.setup(1200, 600)
    # Thiết lập ảnh nền cho màn hình
    screen.bgpic('background.gif')
    # Thiết lập tiêu đề cho cửa sổ chương trình
    turtle.title("Siêu lập trình")
    
# Gọi hàm thiết lập màn hình    
setup_turtle()
# Chơi nhạc
play_music("music.wav")

# Kết hợp các câu đố vui đọc từ File với các câu tính nhẩm Siêu Trí Tuệ.
data = read_data() + generate_math_questions()


# Xáo trộn các câu hỏi một cách ngẫu nhiên
random.shuffle(data)
for question in data:
    ask_question(question)

