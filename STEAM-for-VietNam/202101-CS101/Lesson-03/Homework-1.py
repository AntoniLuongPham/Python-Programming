# Viết hàm create_profile nhận vào 2 tham số name và age và trả về một từ điển có dạng 
# {“name": …, “age": …}.

def create_profile(name, age):
    return {'name': name, 'age': age}


print(create_profile('antoni', 6))
