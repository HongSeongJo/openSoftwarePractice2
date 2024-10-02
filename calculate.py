def plus(a: float, b: float) -> float:
    return a + b

def minus(a: float, b: float) -> float:
    return a - b


num1 = float(input("첫 번째 수: "))
num2 = float(input("두 번째 수: "))

print(f"덧셈: {plus(num1, num2)}")
print(f"뺄셈: {minus(num1, num2)}")