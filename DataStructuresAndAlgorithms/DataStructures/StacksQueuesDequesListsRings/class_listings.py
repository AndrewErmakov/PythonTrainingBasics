# Задача №49. Списки по классам
# https://informatics.mccme.ru/mod/statements/view3.php?id=206&chapterid=49#1


import sys


class SchoolMagazine:
    def __init__(self):
        self.ninth_graders = []
        self.tenth_graders = []
        self.eleventh_graders = []

    def add_to_magazine(self, person):
        if int(person[0]) == 9 and person not in self.ninth_graders:
            self.ninth_graders.append(person)

        elif int(person[0]) == 10 and person not in self.tenth_graders:
            self.tenth_graders.append(person)

        elif int(person[0]) == 11 and person not in self.eleventh_graders:
            self.eleventh_graders.append(person)

    def print_results(self):
        if len(self.ninth_graders) != 0:
            self.output_loop(self.ninth_graders)

        if len(self.tenth_graders) != 0:
            self.output_loop(self.tenth_graders)

        if len(self.eleventh_graders) != 0:
            self.output_loop(self.eleventh_graders)

    def output_loop(self, children):
        for child in children:
            for elem in child:
                print(elem, end=' ')
            print()


if __name__ == '__main__':
    school_magazine = SchoolMagazine()
    for schoolboy in sys.stdin.readlines():
        schoolboy = schoolboy.split()
        school_magazine.add_to_magazine(schoolboy)

    school_magazine.print_results()


