# ISM3232 Midterm: Seabreeze Inn

- **Name:** Jason Nguyen
- **Version:** Delta
- **Date:** 10-19-2026

## What This Program Does
The program calculates the stay cost for Seabreeze Inn while taking into consideration discounts, cleaning fees when needed, and chooses if a guests needs either a welcome package or a credtit check. The program will show the total reserved amount, average stay cost, and what would happen if a guest stayed during the longest duration.
## Business Rules
1. The room cost is the nightly rate multiplied by number of nights.
2. Stays of 4 or more nights or corporate get a 6% discount.
3. Stays of 14 or more nights get 18% discount.
4. $40 cleaning fee is added when discounted amount is $300 or less.
5. A stay amount of $2000 or more needs a credit check.
6. Guest who stay 5 nights and amount more than $1000 gets a welcome package.
## How to Run

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

```
ruff format .
ruff check .
pytest -v
```

## Files in This Repository

-business_rules.py: contains the constants and eight functions
-main.py: contains the sample stays and prints the report
-tests/test_business_rules.py: contains the 22 pytest tests
-tests/__init__.py: allows the tests to import the functions
-commands.md: contains the terminal commands used for the project
-README.md: explains the project
-requirements.txt: lists the packages needed
-.gitignore: keeps unnecessary files out of the repository

## AI Statement

I did not use AI for my midterm.