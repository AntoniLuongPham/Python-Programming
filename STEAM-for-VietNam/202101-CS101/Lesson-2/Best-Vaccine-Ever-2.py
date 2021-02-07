def get_vaccine_score(trials):
    total = 0
    for gia_tri in trials:
        total = total + gia_tri

    score = total / len(trials)
    return score


data = [[80, 85, 87],
        [80, 80, 80],
        [90, 90, 90],
        [80, 90, 90]]

scores = []
for trials in data:
    score = get_vaccine_score(trials)
    scores.append(score)

print('scores:', scores)
