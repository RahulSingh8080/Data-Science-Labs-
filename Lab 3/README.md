# ✅ Lab: Resource Monitoring and Logging System Using Python Decorators, Generators, and Context Managers

## 📘 Problem Statement

You are a Python Developer at a TechOps company. Your task is to develop a **modular and efficient system** to monitor, log, and manage operations on system resources or services (like API calls, file operations, or DB queries).  
The system should **log processing time, memory usage**, and **control resources** using Python's advanced programming features.

---

## 🧱 Objectives

- ✅ Use **decorators** to log execution time and memory usage  
- ✅ Use **generators** to simulate streaming/log processing  
- ✅ Use **context managers** for safe resource management (like files, DB connections)  
- ✅ Make **reusable, clean, and production-grade utility functions**

---

## 🛠 Tasks to Implement

### 🔹 1. Create Custom Decorators

- `@log_execution_time` → Logs function run-time  
- `@log_memory_usage` → Monitors memory footprint (using `tracemalloc` or `psutil`)

### 🔹 2. Implement Generators for Log Streaming

- Simulate logs with a **generator** that yields log lines (simulate real-time streaming)  
- Add **filtering or transformation** to the log stream (e.g., filter only errors)

### 🔹 3. Manage Resources Using Context Managers

Create a custom context manager for:

- ✅ File operations  
- ✅ Database connections (use **mock functions**)  
- ✅ API session handling (using `contextlib.contextmanager`)

### 🔹 4. Simulate Real-World Workflow

- Define **dummy resource-consuming functions** (API calls, data writes)  
- Wrap them with **decorators** and **context managers**  
- Log output stream using **generators**

---

## 🔄 Advanced Functional Design Hints

- Use `yield` for **memory-efficient log streaming**  
- Use `@wraps` in decorators to **preserve function metadata**  
- Use `with` statements for **managing resources safely**  

---

## 📊 Expected Output

- 📌 Logs with timestamps and memory stats  
- 📌 Simulated **real-time log monitoring** with filtering  
- 📌 Clean and readable **execution summary**  
- 📌 Properly **managed files/resources even on error**

---

## 🧪 Bonus (For More Advanced Users)

- 🧰 Create a **Decorator Factory** to configure logging thresholds  
- 🔗 Chain multiple decorators **dynamically**  
- 🧼 Use `functools.partial` or `contextlib.contextmanager` for clean, elegant control flow

---

## ✅ Concepts Covered

- 🎯 **Decorators** (basic, parameterized, and chaining)  
- 🔁 **Generators** and memory-efficient streaming  
- 🔐 **Context managers** (`with`, `__enter__`, `__exit__`)  
- 💡 **Real-time simulation**, abstraction, and modular design

---

## 🧪 Sample Execution Flow

```python
if __name__ == "__main__":
    simulate_workflow()

