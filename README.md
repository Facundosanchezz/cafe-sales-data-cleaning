# Cafe Sales Data Cleaning

Data cleaning and quality validation project using Python and Pandas.

## Project Overview

This project analyzes and cleans a dataset containing
10,000 cafe sales transactions.

The objective is to identify data quality issues,
recover missing information when mathematically justified,
and validate the cleaned dataset.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Pytest

## Data Cleaning

The cleaning process includes:

- Missing value detection
- Numerical data recovery
- Product identification using reference prices
- Category standardization
- Date conversion
- Mathematical consistency validation
- Change tracking

## Results

- Total transactions: 10,000
- Documented corrections: 1,951
- Numerically complete transactions: 9,974
- Numerical completeness: 99.74%
- Automated tests: 6

## Remaining Missing Values

| Column | Missing |
|---|---:|
| Item | 480 |
| Quantity | 23 |
| Price Per Unit | 6 |
| Total Spent | 23 |
| Payment Method | 3,178 |
| Location | 3,961 |
| Transaction Date | 460 |

Missing values were preserved when there was insufficient
information to recover them reliably.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Running Tests

```bash
python -m pytest -v
```

## Project Status

Work in progress. Final audit verification, documentation
and dataset exports are pending.
