# Username & Email Generator

This is a **flexible Python script** that generates thousands of potential usernames (and optionally emails) based on:
- First name
- Last name
- Year of birth (optional)

It supports both **interactive input** and **batch generation** from a text file.

---

##  Features

- Generates **hundreds or thousands of unique usernames** per person.
- Combines initials, abbreviations, full names, and common separators like `.`, `_`, `-`.
- Adds numeric suffixes: full year (e.g., `1986`) and short year (`86`).
- Supports **custom email domain** (e.g., `@gmail.com`, `@company.com`).
- Optionally **saves results to `.txt` files**.

---

##  Requirements

- Python 3.6 or higher
- No external libraries needed

---

##  How to Run

```
python username_generator.py
```

Example:
(If no date is entered, it will start to generate based on a range of years.)
You can also pass a users.txt list written in this way
```
juan,marcelo,1992
,lucas,1880
tas,lucas,
ecc..
```

![{10A1083C-5973-41A2-BDAF-18A7B14F8335}](https://github.com/user-attachments/assets/8b531d39-3116-4281-8a59-a821588f3b84)
