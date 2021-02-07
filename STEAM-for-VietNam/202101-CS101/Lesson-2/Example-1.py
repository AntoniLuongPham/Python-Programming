trials = [80, 85, 87]

total = 0
for value in trials:
    total = total + value

vaccine_score = total / len(trials)
print("Diem vaccine: ", vaccine_score)
