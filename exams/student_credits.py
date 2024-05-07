def students_credits(*data):

    credits_sum = 0
    info_dict = {}
    result = ''

    for element in data:
        current_list = [el for el in element.split("-")]

        name_course = current_list[0]
        credits_given = int(current_list[1])
        max_points = int(current_list[2])
        diyans_points = int(current_list[3])

        course_credit = (((diyans_points / max_points) * 100) * credits_given) / 100

        info_dict[name_course] = course_credit
        credits_sum += course_credit

    info_sorted = dict(sorted(info_dict.items(), key=lambda x: -x[1]))

    if credits_sum >= 240:
        result = f'Diyan gets a diploma with {credits_sum:.1f} credits.'
        for k, v in info_sorted.items():
            result += f"\n{k} - {v:.1f}"
    else:
        result = f"Diyan needs {240 - credits_sum:.1f} credits more for a diploma."
        for k, v in info_sorted.items():
            result += f"\n{k} - {v:.1f}"

    return result.strip()


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)