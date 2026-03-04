# Salary Prediction using Linear Regression

## Overview

This project demonstrates how **Linear Regression** can be used to predict an employee's salary based on their **years of experience**.

Using a small dataset of past employee salaries, a machine learning model learns the relationship between experience and salary and predicts salary for new employees.

---

## Problem Statement

Companies often want to estimate how salary increases with experience. Instead of manually guessing, we can train a **Linear Regression model** to learn the pattern from historical data.

The model learns the mathematical relationship:

```
Salary = m × Experience + b
```

Where:

* **m (Slope)** → How much salary increases for each additional year of experience
* **b (Intercept)** → Base salary when experience = 0

---

## Dataset

The dataset used in this project contains two variables:

| Experience (Years) | Salary |
| ------------------ | ------ |
| 1                  | 20000  |
| 2                  | 25000  |
| 3                  | 30000  |
| 4                  | 35000  |
| 5                  | 40000  |
| 6                  | 45000  |
| 7                  | 55000  |
| 8                  | 60000  |
| 9                  | 75000  |
| 10                 | 80000  |

* **Experience** → Independent Variable (Input)
* **Salary** → Dependent Variable (Output)

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## Machine Learning Model

This project uses:

**Linear Regression (from Scikit-learn)**

The model finds the **best fitting straight line** that represents the relationship between experience and salary.

Training is performed using:

```
model.fit(X, y)
```

This calculates:

* **Slope (m)**
* **Intercept (b)**

---

## Features of the Project

* Create and organize dataset using **Pandas DataFrame**
* Train a **Linear Regression model**
* Predict salary for new experience values
* Visualize relationship using **Scatter Plot**
* Display best-fit regression line
* Show **salary distribution using Histogram**
* Color-coded salary ranges
* Display number of employees in each salary range

---

## Visualization

### Scatter Plot (Regression Model)

Shows the relationship between experience and salary.

* Blue dots → Actual employee data
* Line → Best fit regression line

### Histogram (Salary Distribution)

Displays how predicted salaries are distributed across ranges.

Each colored bar represents a salary range and shows how many employees fall into that range.

---

## Example Prediction

The model predicts salary for a new employee.

Example:

```
Experience = 5 years
Predicted Salary ≈ 43151
```

---

## Project Structure

```
salary-linear-regression
│
├── main.py
├── output.png
└── requirements.txt
```

---

## How to Run the Project

1. Install dependencies

```
pip install -r requirements.txt
```

2. Run the program

```
python main.py
```

---

## Learning Outcomes

This project helps understand:

* Supervised Machine Learning
* Linear Regression
* Model Training
* Model Prediction
* Data Visualization
* Histogram Analysis

---

## Author

Vicky

Machine Learning & Python Enthusiast 🚀
# Salary Prediction using Linear Regression

## Overview

This project demonstrates how **Linear Regression** can be used to predict an employee's salary based on their **years of experience**.

Using a small dataset of past employee salaries, a machine learning model learns the relationship between experience and salary and predicts salary for new employees.

---

## Problem Statement

Companies often want to estimate how salary increases with experience. Instead of manually guessing, we can train a **Linear Regression model** to learn the pattern from historical data.

The model learns the mathematical relationship:

```
Salary = m × Experience + b
```

Where:

* **m (Slope)** → How much salary increases for each additional year of experience
* **b (Intercept)** → Base salary when experience = 0

---

## Dataset

The dataset used in this project contains two variables:

| Experience (Years) | Salary |
| ------------------ | ------ |
| 1                  | 20000  |
| 2                  | 25000  |
| 3                  | 30000  |
| 4                  | 35000  |
| 5                  | 40000  |
| 6                  | 45000  |
| 7                  | 55000  |
| 8                  | 60000  |
| 9                  | 75000  |
| 10                 | 80000  |

* **Experience** → Independent Variable (Input)
* **Salary** → Dependent Variable (Output)

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## Machine Learning Model

This project uses:

**Linear Regression (from Scikit-learn)**

The model finds the **best fitting straight line** that represents the relationship between experience and salary.

Training is performed using:

```
model.fit(X, y)
```

This calculates:

* **Slope (m)**
* **Intercept (b)**

---

## Features of the Project

* Create and organize dataset using **Pandas DataFrame**
* Train a **Linear Regression model**
* Predict salary for new experience values
* Visualize relationship using **Scatter Plot**
* Display best-fit regression line
* Show **salary distribution using Histogram**
* Color-coded salary ranges
* Display number of employees in each salary range

---

## Visualization

### Scatter Plot (Regression Model)

Shows the relationship between experience and salary.

* Blue dots → Actual employee data
* Line → Best fit regression line

### Histogram (Salary Distribution)

Displays how predicted salaries are distributed across ranges.

Each colored bar represents a salary range and shows how many employees fall into that range.

---

## Example Prediction

The model predicts salary for a new employee.

Example:

```
Experience = 5 years
Predicted Salary ≈ 43151
```

---

## Project Structure

```
salary-linear-regression
│
├── main.py
├── output.png
└── requirements.txt
```

---

## How to Run the Project

1. Install dependencies

```
pip install -r requirements.txt
```

2. Run the program

```
python main.py
```

---

## Learning Outcomes

This project helps understand:

* Supervised Machine Learning
* Linear Regression
* Model Training
* Model Prediction
* Data Visualization
* Histogram Analysis

---

## Author

Vicky

Machine Learning & Python Enthusiast 🚀
