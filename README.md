#  Subject Frequency Analyzer (Python)

## Overview

This project is a Python script that analyzes a given text and counts how often each word appears.
It demonstrates key programming concepts such as dictionaries, recursion, loops, and conditional logic.

---

##  Features

* Converts text to lowercase for consistency
* Removes punctuation from input text
* Splits text into individual words
* Counts word frequency using a dictionary
* Ignores common stop words (e.g. *the, is, a, to, and*)
* Uses a **recursive function** to process words

---

##  Technologies Used

* Python 3
* Built-in modules (`string`)

---

## Example Usage

```In console:
Enter your study list: "Python, JS ,and React also CSS."
```

### Output:

```
Python: 1
JS: 1
React: 1
CSS:1
```

---

##  How It Works

1. The input text is cleaned (lowercased and stripped of punctuation)
2. The text is split into a list of words
3. A recursive function processes each word
4. Words are stored in a dictionary with their frequency count
5. Stop words are skipped

---

## Learning Objectives

This project demonstrates:

* Dictionaries for data storage
* Conditional statements for logic control
* Loops for preprocessing text
* Recursive functions for iteration
* Usages of Lambdas

---

##  Future Improvements

* Sort words by frequency
* Display the top N most common words
* Load stop words from a file
* Turn into a CLI tool or web app

---

##  Author

Created as part of a Python learning journey and portfolio development.
