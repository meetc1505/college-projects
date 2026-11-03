# Class Marks Analyzer

A beginner-friendly Python 3 program that takes the marks of a class, validates them, and uses **NumPy** to calculate the mean, median, highest, lowest, standard deviation, pass count and the number of students above average.

| | |
|---|---|
| **PS No.** | 11 |
| **Project Title** | ClassMarksAnalyzer |
| **Language** | Python 3 |
| **Concepts** | NumPy, Lists, Functions, Statistics |

---

## Problem Statement

Create a program that takes the marks of a class as a list, validates them, and uses NumPy to calculate the mean, median, highest, lowest, standard deviation, pass count and the number of students above average.

**Note:**
- Marks are entered as numbers separated by spaces and must be from 0 to 100.
- Pass mark is 40.
- Standard deviation is the population value (`np.std` default).

### Bare Minimum Requirements

1. Write the solution in Python 3 (one `.py` file) and run it from the console.
2. Read the marks of the class into a list and convert it to a NumPy array.
3. Use NumPy to calculate the mean, median, maximum, minimum and standard deviation.
4. Write functions such as `get_marks()` and `analyze_marks()` to count passed, failed and above-average students.
5. Validate the marks (numbers only, from 0 to 100) and print the results in a neat format.

---

## Features

- Reads marks from a single line of space-separated numbers
- Rejects non-numeric input and marks outside 0 to 100
- Rejects empty input
- Calculates mean, median, highest, lowest and standard deviation with NumPy
- Counts passed, failed and above-average students
- Shows the pass percentage
- Clean, comment-free code split into small functions

---

## Requirements

- Python 3.8 or higher
- NumPy

```bash
pip install numpy
```

---

## How to Run

```bash
python class_marks_analyzer.py
```

Then type the marks separated by spaces when asked:

```
Marks: 40 50 60 70 80
```

---

## How the Program Works

The code is split into four small functions, each with one job.

### `get_marks()`
Reads one line of input and splits it into separate values. It checks that:
1. At least one mark is entered.
2. Every value is a number (otherwise it prints `Invalid marks '<value>'. Enter numbers only.`).
3. Every number is between 0 and 100 (otherwise it prints `Marks must be between 0 and 100.`).

If everything is fine, it returns the marks as a NumPy array. If anything is wrong, it prints the error and returns `None`.

### `analyze_marks(marks)`
Takes the NumPy array and does all the calculations. It returns them together in one dictionary so each result can be found by name:

| Key | Meaning | NumPy used |
|---|---|---|
| `total` | Number of students | `len()` |
| `mean` | Average mark | `np.mean()` |
| `median` | Middle mark | `np.median()` |
| `highest` | Maximum mark | `np.max()` |
| `lowest` | Minimum mark | `np.min()` |
| `std` | Population standard deviation | `np.std()` |
| `passed` | Students with marks >= 40 | `np.sum(marks >= 40)` |
| `failed` | Students with marks < 40 | `total - passed` |
| `pass_percentage` | Passed / total x 100 | plain division |
| `above_average` | Students with marks > mean | `np.sum(marks > mean)` |

### `print_report(result)`
Takes the dictionary from `analyze_marks()` and prints it in a neat format. It only handles output and does no calculations.

### `main()`
Connects everything: gets the marks, stops if the input was invalid, analyzes the marks, and prints the report.

---

## Test Cases

### Test Case 1: Normal Input

**Input**
```
Marks: 40 50 60 70 80
```
**Output**
```
Mean: 60.00 | Median: 60.00
Max: 80 | Min: 40 | StdDev: 14.14
Passed: 5 of 5 | Failed: 0 | Pass percentage: 100.00%
Above average: 2 students
```

### Test Case 2: Boundary / Minimum Input (one student)

**Input**
```
Marks: 75
```
**Output**
```
Mean: 75.00 | Median: 75.00
Max: 75 | Min: 75 | StdDev: 0.00
Passed: 1 of 1 | Failed: 0 | Pass percentage: 100.00%
Above average: 0 students
```

### Test Case 3: Invalid Input

**(a) Non-numeric value**
```
Marks: 50 abc 70
```
```
Invalid marks 'abc'. Enter numbers only.
```

**(b) Marks out of range**
```
Marks: 50 10 570
```
```
Marks must be between 0 and 100.
```

### Test Case 4: Different Valid Scenario

**Input**
```
Marks: 25 50 75 100
```
**Output**
```
Mean: 62.50 | Median: 62.50
Max: 100 | Min: 25 | StdDev: 27.95
Passed: 3 of 4 | Failed: 1 | Pass percentage: 75.00%
Above average: 2 students
```

### Extra: Empty Input

**Input**
```
Marks:
```
**Output**
```
Please enter at least one mark.
```

---

## Project Structure

```
.
├── class_marks_analyzer.py
└── README.md
```

---

## Concepts Used

- **NumPy arrays** for fast, simple statistics
- **Lists** to collect the marks before converting them to an array
- **Functions** to keep the code organised and easy to read
- **Statistics**: mean, median, standard deviation (population)
- **Input validation** using `try` / `except` and range checks

---

## Project Mentor

**Mentored by:** [Mr. Satyaprakash Sethy](https://github.com/SATYAPRAKASHSETHY)

**GitHub:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)

**Role:** Python Mentor / Technical Guide
