# A function is group of statements performing a specific task.

def percent(marks):
    pt = ((sum(marks)/500)*100)
    return pt


marks1 = [62, 72, 67, 67, 89]
percentage1 = percent(marks1)

marks2 = [72, 73, 53, 67, 78]
percentage2 = percent(marks2)

print(percentage1, percentage2)

