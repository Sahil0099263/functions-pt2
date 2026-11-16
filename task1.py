def calculate_average(scores):
    return sum(scores) / len(scores)
def get_highest_score(scores):
    return max(scores)
def get_lowest_score(scores):
    return min(scores)
scores = [90, 80, 70]

print(calculate_average(scores))
print(get_highest_score(scores))
print(get_lowest_score(scores))
