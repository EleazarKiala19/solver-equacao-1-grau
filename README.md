# solver-equacao-1-grau
Simple Python program that solves linear equations of the first degree with input validation and loop execution.
# First Degree Equation Solver

A simple Python command-line program that solves linear equations of the form **ax + b = 0**.

## Overview

This project demonstrates basic programming logic in Python, including user input handling, control structures, and error validation. It is designed as a learning exercise for fundamental mathematical problem-solving in code.

## Features

- Automatic solution of linear equations
- Input validation to prevent invalid data
- Loop-based execution for multiple calculations
- Handles special mathematical cases:
  - Infinite solutions (indeterminate equations)
  - No solution (inconsistent equations)
- Clean terminal-based interaction

## How it works

The program requests values for **a** and **b**, then computes the value of **x** using the formula:

x = -b / a

Special conditions are evaluated when:
- a = 0 and b = 0 → infinite solutions
- a = 0 and b ≠ 0 → no solution

## How to run

1. Make sure Python is installed
2. Run the script:

```bash
python main.py
