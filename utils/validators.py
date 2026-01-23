def is_valid_age(age):
    return age.isdigit() and int(age) > 0


def is_valid_grade(grade):
    return grade.isalpha()
