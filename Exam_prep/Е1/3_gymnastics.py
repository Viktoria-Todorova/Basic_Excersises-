country = str(input())
mashine = str(input())
grade = 0

if country == 'Russia':
    if mashine == 'ribbon':
        hardness = 9.1
        presentation = 9.4
        grade += hardness + presentation
    elif mashine == 'hoop':
        hardness = 9.3
        presentation = 9.8
        grade = hardness + presentation
    elif mashine == 'rope':
        hardness = 9.6
        presentation = 9.0
        grade = hardness + presentation
elif country == "Bulgaria":
    if mashine == 'ribbon':
        hardness = 9.6
        presentation = 9.4
        grade += hardness + presentation
    elif mashine == 'hoop':
        hardness = 9.55
        presentation = 9.75
        grade = hardness + presentation
    elif mashine == 'rope':
        hardness = 9.5
        presentation = 9.4
        grade = hardness + presentation
elif country == 'Italy':
    if mashine == 'ribbon':
        hardness = 9.2
        presentation = 9.5
        grade = hardness + presentation
    elif mashine == 'hoop':
        hardness = 9.45
        presentation = 9.35
        grade = hardness + presentation
    elif mashine == 'rope':
        hardness = 9.7
        presentation = 9.15
        grade = hardness + presentation

if grade < 20:
    left_points = 20 - grade
    percent = (left_points / 20) * 100


print(f"The team of {country} get {grade:.3f} on {mashine}.")
print(f"{percent:.2f}%")