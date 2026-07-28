# Student database
students = []


def add_student(name, age, scores):
    """Add a new student"""
    student = {"id": len(students) + 1, "name": name, "age": age, "scores": scores, "avg": sum(scores) / len(scores)}
    students.append(student)
    print(f"{name} added")


def show_all():
    """Display all students"""
    if not students:
        print("No students registered.")
        return

    print("\n" + "=" * 50)
    print(f"{'#':3} {'Name':19} {'Age':^10} {'Average':^8} {'Status':^15}")
    print("=" * 50)

    for s in students:
        status = "Passed" if s["avg"] >= 60 else "Failed"
        print(f"{s['id']:3} {s['name']:19} {s['age']:6} {s['avg']:9.1f} {status:^20}")

    print("=" * 50)


def find_student(name):
    """Search for a student"""
    for s in students:
        if s["name"] == name:
            return s
    return None


def class_stats():
    """Display class statistics"""
    if not students:
        return

    avgs = [s["avg"] for s in students]

    print("\n=== Class Statistics ===")
    print(f"Students: {len(students)}")
    print(f"Class Average: {sum(avgs) / len(avgs):.1f}")
    print(f"Highest Average: {max(avgs):.1f}")
    print(f"Lowest Average: {min(avgs):.1f}")

    passed = sum(1 for a in avgs if a >= 60)
    print(f"Passed: {passed} | Failed: {len(students) - passed}")


# ── Run the system ────────────────
add_student("Ali Rezaei", 15, [85, 90, 78, 92])
add_student("Sara Ahmadi", 14, [95, 88, 97, 100])
add_student("Reza Karimi", 16, [55, 62, 48, 70])
add_student("Niloufar Sadegh", 15, [78, 82, 90, 88])

show_all()
class_stats()

# Search
result = find_student("Sara Ahmadi")
if result:
    print(f"\nFound: {result['name']} | Scores: {result['scores']}")
