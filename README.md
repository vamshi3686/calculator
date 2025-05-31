# calculator
# Calculator – Command Line Based Python Calculator

## Overview

This project is a simple, interactive command-line calculator built using Python. It supports basic arithmetic operations including addition, subtraction, multiplication, and division. Users can perform continuous calculations using previous results or restart the calculator at any time.

## Features

* Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
* Interactive input-driven workflow with clean prompts.
* Option to:

  * Continue operations with the current result.
  * Restart the calculator.
  * Exit the application.

## How It Works

* The calculator starts by prompting the user for two numbers and an operation.
* After computing the result, the user can choose to:

  * Exit the program.
  * Continue calculating with the result.
  * Restart the calculator with new inputs.

## Requirements

* Python 3.x

No additional libraries or dependencies are required.

## Usage

1. **Run the script**
   You can execute the notebook or convert it to a Python script using tools like `nbconvert`.

2. **Sample Interaction**

   ```
   Enter First number: 10
   +
   -
   *
   /
   Select any operation: +
   Enter Second number: 5
   10 + 5 = 15
   Press 'x' to Exit, 'y' to perform other operations with 15 or 's' to restart the calculator:
   ```

3. **Choose Options**

   * `x` – Exit the calculator.
   * `y` – Continue operations using the current result.
   * `s` – Start fresh with new input.

## File Structure

* `Calculator.ipynb` – Main Jupyter Notebook containing the calculator logic.
