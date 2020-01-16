number_students = int(input())

set_lang_least_one_student = set()
set_lang_each_student = set()

for i in range(number_students):
    number_languages_for_each_student = int(input())
    set_lang_one_student = set()
    for lang in range(number_languages_for_each_student):
        name_lang = input()
        set_lang_least_one_student.add(name_lang)

        set_lang_one_student.add(name_lang)

    if i == 0:
        set_lang_each_student |= set_lang_one_student
    else:
        set_lang_each_student &= set_lang_one_student

print(len(set_lang_each_student))
for i in sorted(set_lang_each_student):
    print(i)

print(len(set_lang_least_one_student))
for i in sorted(set_lang_least_one_student):
    print(i)


