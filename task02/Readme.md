# ⚖️ Python BMI Calculator

A lightweight, terminal-based health tool that calculates Body Mass Index (BMI) and provides a health category classification based on World Health Organization (WHO) standards.



## 📋 Overview
This project is a simple Python script designed to help users monitor their health by calculating their BMI using weight (kg) and height (cm). It includes robust error handling to prevent crashes from invalid inputs.

## 🧮 How it Works
The program follows the standard metric formula for BMI:

$$BMI = \frac{weight (kg)}{height (m)^2}$$

### Health Categories
| BMI Range | Category |
| :--- | :--- |
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight |
| 30.0 or Higher | Obese |

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed.

### Running the Program
1. Clone this repository or download the `bmi_calculator.py` file.
2. Open your terminal/command prompt.
3. Run the script:
   ```bash
   python bmi_calculator.py
💻 Code Logic
Input Handling: Accepts weight in kg and height in cm for user convenience.

Metric Conversion: Automatically converts height to meters for the calculation.

Validation: Uses try-except blocks to ensure the user only enters numbers.

Precision: Results are rounded to 2 decimal places for clarity.

🛠️ Planned Enhancements
[ ] Add support for Imperial units (Pounds and Inches).

[ ] Create a Graphical User Interface (GUI) using Tkinter.

[ ] Export results to a CSV file to track history.
