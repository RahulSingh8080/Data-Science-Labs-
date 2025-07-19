import time
import tracemalloc
from contextlib import contextmanager
from functools import wraps
import random

# 1. Decorators

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIME] Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def log_memory_usage(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"[MEMORY] Function '{func.__name__}' used {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")
        return result
    return wrapper

# 2. Generator for Log Streaming

def generate_logs():
    logs = [
        "INFO: Process started",
        "DEBUG: Checking memory",
        "ERROR: Null pointer exception",
        "INFO: Process continued",
        "ERROR: Timeout occurred",
        "INFO: Process ended"
    ]
    for line in logs:
        time.sleep(0.2)  # simulate delay
        yield line

def filter_errors(log_lines):
    for line in log_lines:
        if "ERROR" in line:
            yield line

# 3. Context Manager

@contextmanager
def managed_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()
        print(f"[RESOURCE] File '{filename}' closed.")

@contextmanager
def mock_db_connection():
    print("[DB] Database connection opened.")
    try:
        yield "db_connection_object"
    finally:
        print("[DB] Database connection closed.")

@contextmanager
def mock_api_session():
    print("[API] API session started.")
    try:
        yield "api_session_object"
    finally:
        print("[API] API session ended.")


# 4. Simulated Workflow Functions

@log_memory_usage
@log_execution_time
def perform_api_call():
    time.sleep(random.uniform(0.1, 0.5))
    print("Performing API Call...")

@log_memory_usage
@log_execution_time
def write_to_file():
    with managed_file("output.txt", "w") as f:
        for i in range(5):
            f.write(f"Log entry {i}\n")
            time.sleep(0.1)

@log_memory_usage
@log_execution_time
def query_database():
    with mock_db_connection() as conn:
        print(f"Querying database using {conn}")
        time.sleep(0.3)

# -----------------------------
# Main Execution
# -----------------------------

def main():
    perform_api_call()
    write_to_file()
    query_database()

    print("\nStreaming Logs:")
    for log in filter_errors(generate_logs()):
        print("[STREAM]", log)

if __name__ == "__main__":
    main()
