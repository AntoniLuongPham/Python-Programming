data = [
    [80, 85, 87],
    [72, 75, 78],
]


# 1. Ham tinh diem vaccine
def get_vaccine_score(trials):
    total = 0
    for value in trials:
        total = total + value

    vaccine_score = total / len(trials)
    return vaccine_score


# 2. Tinh diem tat ca vaccine
scores = []
for trials in data:
    score = get_vaccine_score(trials)
    scores.append(score)
