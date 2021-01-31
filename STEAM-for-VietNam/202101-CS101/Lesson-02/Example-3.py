data = [
    [80, 85, 87],
    [72, 75, 78],
]


def get_vaccine_score(trials):
    total = 0
    for value in trials:
        total = total + value
    return total / len(trials)


scores = []
for trials in data:
    score = get_vaccine_score(trials)
    scores.append(score)


best_score = scores[0]
best_index = 0
index = 0
while index < len(scores):
    if scores[index] > best_score:
        best_score = scores[index]
        best_index = index
    index = index + 1

print("Vaccine tot nhat la loai so", best_index, "voi diem la", best_score)
