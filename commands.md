# Seabreeze Inn Midterm Commands

## 1. Building the Project
```
cd ~/Documents
mkdir ism3232-midterm
cd ism3232-midterm
git init
git branch -M main
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
touch business_rules.py
touch main.py
touch README.md
touch commands.md
mkdir -p tests
touch tests/__init__.py
touch tests/test_business_rules.py
echo ".DS_Store" >> .gitignore
printf '\n.venv/\n__pycache__/\n.pytest_cache/\n.ruff_cache/\n' >> .gitignore
pip freeze > requirements.txt
git remote add origin https://github.com/Jason15-ctrl/ism3232-midterm.git
git remote -v
git add .
git commit -m "Add Seabreeze Inn business rules"
git push -u origin main
```

## 2. The virtual environment

```
which python3
```

```
/Users/jasonnguyen/Documents/ism3232-midterm/.venv/bin/python3
```

The .venv folder in the output shows that my virtual environment is active.

## 3. The project structure

```
tree -L 2
```

```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The __pycache__ folder is only on my computer because git ignores it.
## 4. Every function and test

```
rg 'def '
```

```
tests/test_business_rules.py
13:def test_room_cost():
17:def test_discount_under_4_nights():
21:def test_discount_4_nights():
25:def test_discount_13_nights():
29:def test_discount_14_nights():
33:def test_discount_corporate():
37:def test_cleaning_fee_under_limit():
41:def test_cleaning_fee_at_limit():
45:def test_cleaning_fee_over_limit():
49:def test_credit_check():
53:def test_credit_check_under():
57:def test_credit_check_boundary():
61:def test_welcome_package_under_nights():
65:def test_welcome_package_over_nights():
69:def test_welcome_package_under_total():
73:def test_welcome_package_boundary_total():
77:def test_total_reserved():
85:def test_largest_stay():
93:def test_largest_stay_tie():
101:def test_largest_stay_empty():
106:def test_format_stay_line():
111:def test_format_stay_line_opposite():

business_rules.py
15:def calculate_room_cost(nightly_rate: float, nights: int) -> float:
20:def get_stay_discount(nights: int, corporate: bool = False) -> float:
30:def calculate_stay_total(
42:def requires_credit_check(total: float) -> bool:
47:def gets_welcome_package(nights: int, total: float) -> bool:
52:def total_reserved(stays: list) -> float:
64:def largest_stay(stays: list) -> str:
81:def format_stay_line(
```

My business_rules.py defines 8 functions and my tests/test_business_rules.py defines 22 tests.

## 5. Which files print

```
rg -l 'print'
```

```
main.py
```

main.py is shown here instead of business_rules.py is because main.py contains all the print statements and business_rules.py contains only the calculations and return values.

## 6. The commit history

```
git log --oneline
```

```
362a518 (HEAD -> main, origin/main) Change stay line to use yes or no
b4d7e7f Add pytest tests for Seabreeze Inn
648153b Simplify stay report formatting
bc89668 Add Seabreeze Inn stay report
f02f0fd Add Seabreeze Inn business rules
```
I've committed only 5 times so far before committing commands.md
