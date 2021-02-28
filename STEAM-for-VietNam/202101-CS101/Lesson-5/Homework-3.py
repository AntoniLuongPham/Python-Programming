# Bài 3: Dequeue

# Chúng ta sẽ bắt đầu viết các hàm cho Queue, bao gồm hàm enqueue và dequeue.

# Yêu cầu:
# - Viết hàm enqueue và dequeue cho queue
# (Gợi ý: Hàm enqueue cho queue cũng tương tự như hàm push cho stack)
# - Hàm dequeue sẽ xóa phần tử ở vị trí đầu tiên của một mảng
# và trả về phần tử vừa xóa đó



queue = [2, 6, 9]

# ví dụ enqueue
print(enqueue(queue, 1))
# [2, 6, 9, 1]
print(enqueue(queue, 4))
# [2, 6, 9, 1, 4]
print(enqueue(queue, 3))
# [2, 6, 9, 1, 4, 3]

# ví dụ dequeue
print(dequeue(queue))
print(queue)
# 2
# [6, 9, 1, 4, 3]

print(dequeue(queue))
print(queue)
# 6
# [9, 1, 4, 3]

print(dequeue(queue))
print(queue)
# 9
# [1, 4, 3]
