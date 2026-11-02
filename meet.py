#Name: Meet Choubey
#ERP: RU2602603
#Section: B2
#Email: meet.choubey@rungta.org
import numpy as np

PASS_MARK = 40


def get_marks():
    items = input("Marks: ").split()

    if not items:
        print("Please enter at least one mark.")
        return None

    marks = []
    for item in items:
        try:
            marks.append(float(item))
        except ValueError:
            print(f"Invalid marks '{item}'. Enter numbers only.")
            return None

    if not all(0 <= mark <= 100 for mark in marks):
        print("Marks must be between 0 and 100.")
        return None

    return np.array(marks)


def analyze_marks(marks):
    total = len(marks)
    mean = np.mean(marks)
    passed = int(np.sum(marks >= PASS_MARK))

    return {
        "total": total,
        "mean": mean,
        "median": np.median(marks),
        "highest": np.max(marks),
        "lowest": np.min(marks),
        "std": np.std(marks),
        "passed": passed,
        "failed": total - passed,
        "pass_percentage": passed / total * 100,
        "above_average": int(np.sum(marks > mean)),
    }


def print_report(result):
    print(f"Mean: {result['mean']:.2f} | Median: {result['median']:.2f}")
    print(f"Max: {result['highest']:g} | Min: {result['lowest']:g} | StdDev: {result['std']:.2f}")
    print(f"Passed: {result['passed']} of {result['total']} | Failed: {result['failed']} | "
          f"Pass percentage: {result['pass_percentage']:.2f}%")
    print(f"Above average: {result['above_average']} students")


def main():
    marks = get_marks()
    if marks is None:
        return
    result = analyze_marks(marks)
    print_report(result)


if __name__ == "__main__":
    main()
