# 🧪 Lab 1: Object-Oriented Programming (OOPs) in Python

## 📘 Problem Statement

You are working as a **Data Scientist** in a **retail analytics firm**. Your task is to design a system using **Object-Oriented Programming (OOP)** that models a simple **retail store's product and customer behavior**.

---

## 🧱 Objectives

- Model real-world entities using OOP
- Apply class and object concepts
- Demonstrate encapsulation
- (Optional) Use inheritance for PremiumCustomer logic

---

## 🏗️ Classes and Attributes

### 📦 `Product` Class

Attributes:
- `product_id` (int)
- `name` (str)
- `price` (float)
- `stock_quantity` (int)

### 👤 `Customer` Class

Attributes:
- `customer_id` (int)
- `name` (str)
- `cart` (list of dicts with product & quantity)

---

## 🛠️ Functionalities to Implement

- Add product to inventory
- Display available products
- Add product to customer cart (with stock check)
- Calculate total bill
- Display purchase summary
- Encapsulation using private attributes
- `__str__` method for representation
- (Optional) Inheritance for `PremiumCustomer` with discounts
