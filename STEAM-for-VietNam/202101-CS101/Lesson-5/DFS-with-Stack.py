import time
from turtle import (
    begin_fill,
    color,
    done,
    end_fill,
    forward,
    goto,
    hideturtle,
    pendown, penup,
    right,
    screensize, setheading, speed,
    tracer,
    update
)


hideturtle()

# ===================================
# === BẮT ĐẦU PHẦN CODE STACK =======
# ===================================

# Khởi tạo stack là một mảng trống
stack = []


# Đưa giá trị vào trong stack, mỗi phần tử trong Stack sẽ là một cell.
# cell là một mảng gồm 2 phần tử là hàng và cột. Ví dụ [2, 3]
def push_to_stack(cell):
    stack.append(cell)


# Lấy giá trị ra khỏi stack
# Trả về một mảng gồm 2 phần tử là hàng và cột. Ví dụ [2, 3]
def pop_from_stack():
    if stack_len() > 0:
        return stack.pop()
    else:
        return None


# Trả ra số phần tử hiện có trong stack
def stack_len():
    return len(stack)


# ===================================

# ===================================
# =========== CÁC HÀM VẼ ============
# ===================================

# Hàm vẽ hình vuông, dùng để vẽ mỗi ô vuông trong mê cung
# x, y là toạ độ của điểm góc trên bên trái của hình vuông
# size là độ dài của cạnh
# border_color là màu của đường viền
# fill_color là màu của hình vuông
def draw_square(x, y, size, border_color, fill_color):
    # Chỉnh đến vị trí góc trên bên trái của hình vuông
    penup()   # Nhấc bút vẽ lên
    goto(x, y)   # Đi đến toạ độ xác định
    setheading(0)   # Đặt hướng cho turtle
    speed('fastest')   # Đặt tốc độ vẽ của turtle
    pendown()   # Đặt bút xuống để vẽ

    # Chỉnh màu
    color(border_color, fill_color)

    begin_fill()

    # Vẽ 4 cạnh
    for i in range(4):
        forward(size)   # Vẽ 1 cạnh\
        right(90)   # Quay một góc 90 độ để vẽ cạnh tiếp theo

    end_fill()


# Hàm vẽ toàn bộ mê cung
# đầu vào maze là một mảng hai chiều
def draw_maze(maze):
    screensize(400, 400)   # Kích thước mê cung tính theo pixel
    top = 200   # Toạ độ điểm trên cùng
    left = -200   # Toạ độ điểm phía bên trái cùng
    cell_size = 400/len(maze)   # Kích thước mỗi ô vuông

    # Duyệt từng phần tử ở trong mảng hai chiều để tiến hành vẽ từng ô vuông
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            # Tính toạ độ của mỗi ô vuông
            x = left + col * cell_size
            y = top - row * cell_size

            # Vẽ ô vuông theo các trạng thái khác nhau
            if (maze[row][col] == 0):  # tường
                draw_square(x, y, cell_size, 'white', 'black')
            elif (maze[row][col] == 1):  # Đường đi chưa ghé thăm
                draw_square(x, y, cell_size, 'black', 'white')
            elif (maze[row][col] == -1):  # Đường đi đã ghé thăm
                draw_square(x, y, cell_size, 'black', 'yellow')
            elif (maze[row][col] == -2):  # Đường cụt
                draw_square(x, y, cell_size, 'black', 'grey')
            elif (maze[row][col] == 2):  # Điểm bắt đầu
                draw_square(x, y, cell_size, 'white', 'green')
            elif (maze[row][col] == 3):  # Điểm kết thúc
                draw_square(x, y, cell_size, 'white', 'red')
    update()   # Hiển thị mê cung ra màn hình

# ===================================


# ==== ĐỊNH NGHĨA MẢNG MÊ CUNG =====
# -2: đường đi dẫn vào đường cụt
# -1: đường đi đã ghé thăm
# 0: tường
# 1: đường đi chưa ghé thăm
# 2: điểm bắt đầu
# 3: điểm kết thúc
maze_array = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0, 0]
]

tracer(0, 0)   # Ẩn quá trình vẽ của turtle để chương trình chạy nhanh hơn

# Vẽ mê cung ban đầu
draw_maze(maze_array)

# =========================================
# =========================================
# ==== BẮT ĐẦU QUÁ TRÌNH BIỂU DIỄN DFS ====
# =========================================
# =========================================

# =====================================
# === BƯỚC 1: ĐI ĐẾN ĐIỂM XUẤT PHÁT ===
# =====================================
# Trạng thái ban đầu tại ô xuất phát: hàng 1 cột 0
current_cell = [1, 0]

# Chạy vòng lặp cho đến khi tìm được đích đến
# hoặc không tìm được, phải quay về nơi xuất phát
while True:
    # ========================================
    # === BƯỚC 2: ĐÁNH DẤU VỊ TRÍ HIỆN TẠI ===
    # ========================================
    row = current_cell[0]   # Hàng tương ứng với vị trí hiện tại
    col = current_cell[1]   # Cột tương ứng với vị trí hiện tại

    # Kiểm tra nếu ô đi đến là đích (giá trị = 3) thì thoát khỏi vòng lặp,
    # dừng chương trình
    if (maze_array[row][col] == 3):
        break

    # Đánh dấu vị trí hiện tại là đã ghé thăm (giá trị = -1)
    maze_array[row][col] = -1
    # ====================================================================

    # ====================================================================
    # === BƯỚC 3: NHÌN TRÊN DƯỚI TRÁI PHẢI XEM CÓ ĐƯỜNG ĐI KHÔNG =========
    # ====================================================================
    next_cell = None

    # Kiểm tra nếu có thể đi lên ô bên trên được không
    if (row > 0 and maze_array[row - 1][col] > 0):
        # Gán ô tiếp theo sẽ là ô bên trên của ô hiện tại
        next_cell = [row - 1, col]
    elif (row < 9 and maze_array[row + 1][col] > 0):  # Kiểm tra ô bên dưới
        next_cell = [row + 1, col]
    elif (col > 0 and maze_array[row][col - 1] > 0):  # Kiểm tra ô bên trái
        next_cell = [row, col - 1]
    elif (col < 9 and maze_array[row][col + 1] > 0):  # Kiểm tra ô bên phải
        next_cell = [row, col + 1]
    # ====================================================================

    # Kiểm tra nếu tồn tại một ô để đi, có nghĩa chưa phải đường cụt
    if next_cell is not None:
        # =====================================================================
        # == BƯỚC 4: Đưa ô hiện tại vào Stack, rồi di chuyển đến ô tiếp theo ==
        # =====================================================================
        push_to_stack(current_cell)
        current_cell = next_cell

    else:  # Nếu không thể đi được tới ô nào cả
        # Chuyển ô hiện tại sang màu xám để báo đường cụt
        maze_array[row][col] = -2

        # =====================================================================
        # == BƯỚC 5: Quay lại vị trí trước đó bằng cách lấy một ô trong Stack==
        # =====================================================================

        # Lấy từ trong Stack ra một ô để quay lại vị trí ngay trước đó
        current_cell = pop_from_stack()

        if current_cell is None:
            # Nếu Stack mà không chứa bất cứ ô nào,
            # nghĩa là tất cả mọi đường đi đều cụt,
            # mê cung không có lối ra.
            # Thoát khỏi vòng lặp và dừng chương trình.
            break

    # Vẽ lại mê cung sau khi đã thay đổi trạng thái các ô
    draw_maze(maze_array)

    # Thời gian dừng giữa mỗi bước (tính theo giây) để dễ quan sát
    time.sleep(0.2)

done()
