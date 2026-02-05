numbers = [int(input()) for _ in range(10)]
mod = {x % 42 for x in numbers}
print(len(mod))