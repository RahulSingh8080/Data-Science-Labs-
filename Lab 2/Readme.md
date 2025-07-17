# 🧪 Lab: Dynamic Data Transformation Pipeline for Real-Time Retail Analytics

## 📘 Problem Statement

You are working as a **Data Engineer** in a **Retail Analytics** team. Your task is to build a **dynamic and configurable data transformation engine** that can apply a sequence of user-defined operations (functions) to a real-time stream of product sales data using **functional programming constructs** and **advanced function arguments** in Python.

---

## 🎯 Objectives

- ✅ Apply `lambda` functions for dynamic data transformation  
- ✅ Use `map`, `filter`, and `reduce` for streaming transformations  
- ✅ Use arbitrary arguments (`*args`, `**kwargs`) to allow flexible function definitions  
- ✅ Use positional-only and keyword-only arguments for clean, controlled function signatures  
- ✅ Build a reusable and modular transformation pipeline  

---

## 🛠️ Tasks to Implement

### 🔹 1. Create a Transformation Engine

- Accept transformation functions using `*args`
- Each function must use `map`, `filter`, or `reduce`
- Support `lambda` functions for inline logic

### 🔹 2. Implement Filters Based on Custom Rules

- Create filter functions using `**kwargs`  
  e.g., `price > X`, `category == Y`
- Use **keyword-only arguments** for clarity and validation

### 🔹 3. Apply Discounts or Taxes Using Lambda & Map

- Use `map()` and `lambda` to apply rules
- Functions must use **positional-only** and **keyword-only** arguments

### 🔹 4. Summarize Total Revenue Using Reduce

- Use `reduce()` to compute:
  - Total sales revenue
  - Optional: Revenue per category using `groupby`-like logic

### 🔹 5. Build a Function Pipeline

- Accept a series of transformations via `*args`
- Ensure order of execution is maintained
- Allow easy plug-and-play of new transformation steps

---

## 📊 Expected Output

- ✅ Transformed product sales data (post-transformation)  
- ✅ Summary report including:
  - Total revenue
  - High-value transactions
  - Category-wise breakdown (optional)
- ✅ Log of operations applied (optional enhancement)

---

## 🚀 Real-World Simulation Goals

- Mimics **real-time data pipelines**
- Encourages **modular design**, **abstraction**, and **reusability**
- Applies **Pythonic** and **functional programming** idioms for performance and clarity

---

