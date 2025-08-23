Thank you for sharing the Kattis problem link. Based on the official problem description, here's an updated README tailored to the Egypt problem:
https://open.kattis.com/problems/egypt
---

# 🧭 Egypt Problem – README

## 📘 Problem Overview

The ancient Egyptians discovered that a triangle with sides of lengths 3, 4, and 5 forms a right triangle. Your task is to determine if other given sets of three side lengths also form right triangles.

## 🔢 Problem Details

* **Input:** Several test cases, each containing three positive integers representing the sides of a triangle. The input ends with a line containing `0 0 0`.

* **Output:** For each test case, output "right" if the sides form a right triangle, and "wrong" otherwise.

* **Constraints:**

  * Up to 1,000 test cases.
  * Side lengths are positive integers not exceeding 30,000.

  ---

  ## 🛠️ Developer Notes: How to Test `egypt.py`

  To test the solution locally using the provided `test_input.txt` file, run the following command in PowerShell:

  ```
  Get-Content Egypt\test_input.txt | python Egypt\egypt.py
  ```

  This will feed the test cases from `test_input.txt` into your script and display the results in the terminal.

## ✅ Approach

1. **Input Parsing:** Read each line of input until `0 0 0` is encountered.

2. **Validation:** Ensure each line contains exactly three positive integers.

3. **Sorting:** Sort the three integers to identify the largest side.

4. **Pythagorean Theorem:** Check if the sum of the squares of the two smaller sides equals the square of the largest side.

5. **Output:** Print "right" if the condition is satisfied; otherwise, print "wrong".

## 🧪 Example

**Input:**

```
6 8 10
25 52 60
5 12 13
0 0 0
```

**Output:**

```
right
wrong
right
```

## 💡 Teaching Notes

* **Input Validation:** Emphasize the importance of validating input to ensure the program handles unexpected or malformed data gracefully.

* **Sorting:** Sorting the sides simplifies the process of identifying the hypotenuse.

* **Pythagorean Theorem:** Reinforce the mathematical concept that defines right triangles.

* **Edge Cases:** Discuss scenarios like duplicate side lengths or non-triangular inputs.

## 📄 License

MIT License

---

Feel free to adjust the content as needed for your audience or use case.
