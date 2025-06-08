# Advanced Python Practice Problems (Topic-wise)

## 1. Iterators and Generators

### Problem 1: Custom Range Generator

 Create a generator `custom_range(start, end, step)` that behaves like `range()` but supports float values.

### Problem 2: Prime Number Iterator

Create an iterator class that yields prime numbers less than a given number n.

## 2. Decorators

### Problem 1: Timing Decorator

Create a decorator `@timed` that prints the execution time of the decorated function.

### Problem 2: Retry Decorator

Create a decorator `@retry` that retries a function up to `n` times if it raises an exception.

## 3. Context Managers

### Problem 1: File Transaction

Create a context manager `transactional_file` that rolls back changes to a file if an exception occurs inside the `with` block.

### Problem 2: Timer Context

Create a context manager that prints the time taken to execute a code block.

## 4. Metaclasses

### Problem 1: Singleton Metaclass

Create a meta-class that ensures only one instance of a class is created.

### Problem 2: AutoAttributes Metaclass

Create a metaclass that automatically adds `__init__` and `__repr__` methods based on class annotations.

## 5. Coroutines and Asyncio

### Problem 1: Async Web Scraper

Write an async function using `aiohttp` to scrape multiple websites concurrently.

### Problem 2: Coroutine Pipeline

Implement a coroutine pipeline to process streaming data in stages (e.g., filter, transform, store).

## 6. Multiprocessing and Threading

### Problem 1: Parallel Image Processing

Use `multiprocessing` to apply filters to a set of images in parallel.

### Problem 2: Thread-safe Counter

Implement a thread-safe shared counter using `threading.Lock()`.

## 7. File and Data Handling

### Problem 1: JSON Flattening

Write a function to flatten a nested JSON into a flat dictionary.

### Problem 2: CSV Merge

Merge multiple CSV files in a directory based on a common key.

## 8. Data Structures and Algorithms

### Problem 1: Trie Implementation

Implement a Trie (prefix tree) with insert, search, and delete functionality.

### Problem 2: LRU Cache

Build an LRU Cache using `OrderedDict` or a custom doubly-linked list.

## 9. OOP and Design Patterns

### Problem 1: Strategy Pattern

Implement the strategy design pattern to switch between sorting algorithms.

### Problem 2: Observer Pattern

Simulate an event-notification system using the observer pattern.

## 10. Testing and Debugging

### Problem 1: Unit Test Generator

Create a utility that generates basic unit tests for given functions using `unittest`.

### Problem 2: Debug Decorator

Create a decorator that logs function arguments, return value, and exceptions if any.
