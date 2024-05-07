def gather_credits(credits_f, *args):

    credits_collected = 0
    courses = {}

    for current_tuple in args:
        course_name, credits_course = current_tuple[0], int(current_tuple[1])
        if credits_collected < credits_f:
            if course_name not in courses.keys():
                courses[course_name] = credits_course
                credits_collected += credits_course
            else:
                continue
        else:
            break
    if credits_collected >= credits_f:
        return (f"Enrollment finished! Maximum credits: {credits_collected}.\n"
                f"Courses: {', '.join(sorted(courses))}")
    else:
        return (f"You need to enroll in more courses! "
                f"You have to gather {credits_f - credits_collected} credits more.")


print(gather_credits(
            80,
            ("Basics", 27),

))