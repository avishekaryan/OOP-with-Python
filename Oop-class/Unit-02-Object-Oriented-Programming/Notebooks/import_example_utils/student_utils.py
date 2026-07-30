PASSING_SCORE = 60

class Student:
    def __init__(self, name, score):
        self.name  = name
        self.score = score
    def get_grade(self):
        if self.score >= 90: return "A"
        if self.score >= 75: return "B"
        if self.score >= 60: return "C"
        return "F"

def class_average(students):
    return sum(s.score for s in students) / len(students)

def top_n(students, n=3):
    return sorted(students, key=lambda s: s.score, reverse=True)[:n]


if __name__ == "__main__":
    # This block ONLY runs when the file is executed directly
    # It does NOT run when student_utils is imported by another module
    test_students = [Student("Alice", 85), Student("Bob", 72)]
    print(f"Average: {class_average(test_students):.1f}")