def softuni_students(*args, **kwargs):
    students = {}
    invalid = []

    for k, v in kwargs.items():
        for data in args:
            if k == data[0]:
                students[data[1]] = v
    for element in args:
        if element[1] not in students.keys():
            invalid.append(element[1])

    invalid = sorted(invalid)
    students = dict(sorted(students.items()))
    result = []
    for k, v in students.items():
        result.append(f"*** A student with the username {k} has successfully finished the course {v}!")
    if invalid:
        result.append(f"!!! Invalid course students: {', '.join([name for name in invalid])}")
    return '\n'.join(result)


print(softuni_students((
    'id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced'
))