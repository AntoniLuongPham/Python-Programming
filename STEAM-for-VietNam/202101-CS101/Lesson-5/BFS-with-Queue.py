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


# CONSTANTS
# =========

# ĐỊNH NGHĨA CÁC MẢNG MÊ CUNG
w = 'WALL'   # tường
r = 'ROAD'   # đường đi chưa ghé thăm
S = 'START'   # điểm bắt đầu
E = 'END'   # điểm kết thúc


MAZE_0 = [
    [w, w, w, w, w, w, w, w, w, w],
    [S, r, r, r, r, r, w, w, w, w],
    [w, w, r, w, w, r, w, r, r, w],
    [w, w, r, w, w, r, w, r, w, w],
    [w, w, r, r, r, r, r, r, r, w],
    [w, w, w, r, w, w, w, w, r, w],
    [w, w, w, r, w, w, w, r, r, w],
    [w, w, w, r, w, r, w, r, w, w],
    [w, w, w, w, w, r, r, r, w, w],
    [w, w, w, w, w, E, w, w, w, w]
]

MAZE_1 = [
    [w, w, w, w, w, w, w, w, w, w],
    [S, r, r, r, r, r, w, w, w, w],
    [w, w, r, w, w, r, w, r, r, w],
    [w, w, r, w, w, r, w, r, w, w],
    [w, w, r, r, r, r, r, r, r, w],
    [w, w, w, r, w, w, w, w, r, w],
    [w, w, w, r, w, w, w, r, r, w],
    [w, w, w, r, w, r, w, r, w, w],
    [w, w, w, w, w, r, r, r, r, r],
    [w, w, w, w, w, w, w, w, w, E]
]

MAZE_2 = [
    [S, w, w, w, w, w, w, w, w, w],
    [r, r, r, r, r, r, w, w, w, w],
    [w, w, r, w, w, r, w, r, r, w],
    [w, w, r, w, w, r, w, r, w, w],
    [w, w, r, r, r, r, r, r, r, w],
    [w, w, w, r, w, w, w, w, r, w],
    [w, w, w, r, w, w, w, r, r, w],
    [w, w, w, r, w, r, w, r, w, w],
    [w, w, r, r, w, r, r, r, w, w],
    [w, w, E, w, w, w, w, w, w, w]
]

MAZE_3 = [
    [S, w, w, w, w, w, w, w, w, w],
    [w, r, r, r, r, r, w, w, w, w],
    [w, w, r, w, w, r, w, r, r, w],
    [w, w, r, w, w, r, w, r, w, w],
    [w, w, r, r, r, r, r, r, r, w],
    [w, w, w, r, w, w, w, w, r, w],
    [w, w, w, r, w, w, w, r, r, w],
    [w, w, w, r, w, r, w, r, w, w],
    [w, w, w, w, w, r, r, r, w, w],
    [w, w, w, w, w, E, w, w, w, w]
]


CAN_GO_TO_VALUES = {r, S, E}

ALREADY_TRIED = 'ALREADY_TRIED'   # đường đi đã ghé thăm
ON_SHORTEST_PATH = 'ON_SHORTEST_PATH'


# FUNCTIONS
# =========

# Hàm vẽ hình vuông, dùng để vẽ mỗi ô vuông trong mê cung
# x, y là toạ độ của điểm góc trên bên trái của hình vuông
# size là độ dài của cạnh
# border_color là màu của đường viền
# fill_color là màu của hình vuông
def draw_square(x, y, size, border_color, fill_color):
    penup()   # Nhấc bút vẽ lên
    goto(x, y)   # Đi đến toạ độ vị trí góc trên bên trái của hình vuông
    setheading(0)   # Đặt hướng cho turtle
    speed('fastest')   # Đặt tốc độ vẽ của turtle
    pendown()   # Đặt bút xuống để vẽ

    # Chỉnh màu
    color(border_color, fill_color)

    begin_fill()

    # Vẽ 4 cạnh
    for _ in range(4):
        forward(size)   # Vẽ 1 cạnh
        right(90)   # Quay một góc 90 độ để vẽ cạnh tiếp theo

    end_fill()


def measure_maze_dims(maze):
    return (len(maze), len(maze[0]))


# Hàm vẽ toàn bộ mê cung
# đầu vào maze là một mảng hai chiều
def draw_maze(maze):
    screensize(400, 400)   # Kích thước mê cung tính theo pixel
    top = 200   # Toạ độ điểm trên cùng
    left = -200   # Toạ độ điểm phía bên trái cùng
    cell_size = 400 / len(maze)   # Kích thước mỗi ô vuông

    n_rows, n_cols = measure_maze_dims(maze=maze)

    # Duyệt từng phần tử ở trong mảng hai chiều để tiến hành vẽ từng ô vuông
    for row in range(n_rows):
        for col in range(n_cols):
            cell_value = maze[row][col]

            # Tính toạ độ của mỗi ô vuông
            x = left + col * cell_size
            y = top - row * cell_size

            # Vẽ ô vuông theo các trạng thái khác nhau
            if cell_value == w:   # tường
                draw_square(
                    x=x,
                    y=y,
                    size=cell_size,
                    border_color='white',
                    fill_color='black')

            elif cell_value == r:   # Đường đi chưa ghé thăm
                draw_square(
                    x=x,
                    y=y,
                    size=cell_size,
                    border_color='black',
                    fill_color='white')

            elif cell_value == S:   # Điểm bắt đầu
                draw_square(
                    x=x,
                    y=y,
                    size=cell_size,
                    border_color='white',
                    fill_color='green')

            elif cell_value == E:   # Điểm kết thúc
                draw_square(
                    x=x,
                    y=y,
                    size=cell_size,
                    border_color='white',
                    fill_color='red')

            elif cell_value == ALREADY_TRIED:   # Đường đi đã ghé thăm
                draw_square(
                    x=x,
                    y=y,
                    size=cell_size,
                    border_color='black',
                    fill_color='yellow')

            elif cell_value == ON_SHORTEST_PATH:
                draw_square(
                    x=x,
                    y=y,
                    size=cell_size,
                    border_color='white',
                    fill_color='cyan')

    update()   # Hiển thị mê cung ra màn hình


# Đưa giá trị vào trong queue, mỗi phần tử trong queue sẽ là một cell.
# Cell là một mảng gồm 2 phần tử là hàng và cột, ví dụ (5, 3).
def enqueue(queue, items):
    queue.extend(items)
    # you can also do like this:
    # queue += items


# Lấy giá trị ra khỏi queue.
# Trả về một mảng gồm 2 phần tử là hàng và cột, ví dụ (5, 3).
def dequeue(queue):
    if len(queue) > 0:
        return queue.pop(0)
    else:
        return None


def find_start_cell(maze):
    n_rows, n_cols = measure_maze_dims(maze=maze)

    for row_number in range(n_rows):
        for col_number in range(n_cols):
            cell_value = maze[row_number][col_number]
            if cell_value == S:
                return (row_number, col_number)

    return None


def find_adjacent_cells(maze, current_cell):
    n_rows, n_cols = measure_maze_dims(maze=maze)
    current_row_number, current_col_number = current_cell

    # a list of cells
    result = []

    # Kiểm tra nếu có thể đi lên ô bên trên được không
    if (current_row_number > 0) and \
            (maze[current_row_number - 1][current_col_number]
             in CAN_GO_TO_VALUES):
        result.append((current_row_number - 1, current_col_number))

    # Kiểm tra ô bên phải
    if (current_col_number < n_cols - 1) and \
            (maze[current_row_number][current_col_number + 1]
             in CAN_GO_TO_VALUES):
        result.append((current_row_number, current_col_number + 1))

    # Kiểm tra ô bên dưới
    if (current_row_number < n_rows - 1) and \
            (maze[current_row_number + 1][current_col_number]
             in CAN_GO_TO_VALUES):
        result.append((current_row_number + 1, current_col_number))

    # Kiểm tra ô bên trái
    if (current_col_number > 0) and \
            (maze[current_row_number][current_col_number - 1]
             in CAN_GO_TO_VALUES):
        result.append((current_row_number, current_col_number - 1))

    return result


def solve_maze_by_bfs(maze):
    # Vẽ mê cung ban đầu
    draw_maze(maze)

    # find start cell
    start_cell = find_start_cell(maze=maze)
    # path tracing
    just_come_from = {start_cell: None}
    # init queue with start cell
    queue = [start_cell]

    # Chạy vòng lặp cho đến khi tìm được đích đến
    # hoặc không tìm được, phải quay về nơi xuất phát
    while True:
        # get the first cell in the queue
        current_cell = dequeue(queue=queue)

        if current_cell is not None:
            current_row_number, current_col_number = current_cell

            # Kiểm tra nếu ô đi đến là đích thì thoát khỏi vòng lặp,
            # dừng chương trình
            if maze[current_row_number][current_col_number] == E:
                break

            # Đánh dấu vị trí hiện tại là đã ghé thăm
            maze[current_row_number][current_col_number] = ALREADY_TRIED

            # find adjacent cells
            adjacent_cells = find_adjacent_cells(maze=maze,
                                                 current_cell=current_cell)
            # path tracing
            for adjacent_cell in adjacent_cells:
                just_come_from[adjacent_cell] = current_cell
            # then enqueue adjacent cells
            enqueue(queue=queue,
                    items=adjacent_cells)

            # Vẽ lại mê cung sau khi đã thay đổi trạng thái các ô
            draw_maze(maze)

            # Thời gian dừng giữa mỗi bước (tính theo giây) để dễ quan sát
            time.sleep(0.2)

        # else the maze is unsolvable
        else:
            break

    # highlight shortest path
    path_tracing_cell = current_cell
    while path_tracing_cell is not None:
        path_tracing_row_number, path_tracing_col_number = path_tracing_cell
        maze[path_tracing_row_number][path_tracing_col_number] = \
            ON_SHORTEST_PATH
        path_tracing_cell = just_come_from[path_tracing_cell]
    draw_maze(maze)


# MAIN PROGRAM
# ============
if __name__ == '__main__':
    hideturtle()
    tracer(0, 0)   # Ẩn quá trình vẽ của turtle để chương trình chạy nhanh hơn

    # solve the maze
    solve_maze_by_bfs(maze=MAZE_2)

    done()
