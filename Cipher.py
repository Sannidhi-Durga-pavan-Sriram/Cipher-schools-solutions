# Question 1
print("Hello, World!")

# Question 2
print("Hello, Python!\nLet's start coding.")

# Question 3
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hi {name}, you are {age} years old.")

# Question 4
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Question 5
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

# Question 6
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0 and num % 10 != 0:
    print("Yes, condition satisfied.")
else:
    print("No, condition not satisfied.")

# Question 7
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Question 8
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)

# Question 9
for i in range(1, 11):
    print(i)

# Question 10
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# Question 11
i = 5
while i >= 1:
    print(i)
    i -= 1

# Question 12
i = 5
while i >= 1:
    print(i)
    i -= 1

# Question 13
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# Question 14
for i in range(1, 31):
    if i % 4 == 0 and i % 7 == 0:
        break
    print(i)

# Collections Set Difference
s1 = set([(1, 2), (3, 4), (5, 6)])
s2 = set([(3, 4), (7, 8)])
result = s1 - s2
print(result)

# List Comprehension - Matrix Transformation
matrix = [[1, 2], [3, 4], [5, 6]]
result = [[x**2 if x % 2 == 0 else x for x in row] for row in matrix]
print(result)

# Logger System Class
from collections import deque, defaultdict
import re

class LoggerSystem:
    def __init__(self, capacity):
        self.capacity = capacity
        self.logs = deque(maxlen=capacity)
        self.user_logs = defaultdict(list)
        self.level_count = defaultdict(int)

    def add_log(self, line: str) -> None:
        match = re.match(r"\[(.*?)\] (\w+) (\w+): (.*)", line)
        if not match:
            return
        timestamp, level, user_id, message = match.groups()
        log_entry = {
            "timestamp": timestamp,
            "level": level,
            "user_id": user_id,
            "message": message
        }
        self.logs.append(log_entry)
        self.user_logs[user_id].append(log_entry)
        self.level_count[level] += 1

    def get_user_logs(self, user_id: str):
        return self.user_logs.get(user_id, [])

    def count_levels(self):
        return dict(self.level_count)

    def filter_logs(self, keyword: str):
        keyword = keyword.lower()
        return [log for log in self.logs if keyword in log['message'].lower()]

    def get_recent_logs(self):
        return list(self.logs)

# Driver Code
logger = LoggerSystem(capacity=5)
logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]
for line in logs:
    logger.add_log(line)

# Vector3D Class
import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        return self.magnitude() <= other.magnitude()

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()

    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    def __getitem__(self, index):
        return (self.x, self.y, self.z)[index]

    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    @staticmethod
    def zero():
        return Vector3D(0, 0, 0)

