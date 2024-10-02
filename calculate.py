def plus(a: float, b: float) -> float:
    return a + b

def minus(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        print("0으로 못 나눠요! 이 부분입니다.") #충돌부분
    return a / b

num1 = float(input("첫 번째 수: "))
num2 = float(input("두 번째 수: "))

print(f"덧셈: {plus(num1, num2)}")
print(f"뺄셈: {minus(num1, num2)}")
print(f"곱셈: {multiplication(num1, num2)}")
print(f"나눗셈: {division(num1, num2)}")