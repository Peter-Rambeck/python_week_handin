
# helper to auto_generate_data_sheet -> auto_generate_students
def auto_generate_courses():
    courses = []
    course1 = Course('Robots', 101, 'Teacher1', 100, 9)
    course2 = Course('Robot', 102, 'Teacher2', 10, 10)
    course3 = Course('Python', 103, 'Teacher3', 10, 12)
    my_course_list = [course1, course2, course3]
    for i in range(2):
        courses.append(random.choice(my_course_list))
    return courses

# helper to auto_generate_students
def auto_generate_data_sheet():
    data_sheet = DataSheet(auto_generate_courses())
    return data_sheet