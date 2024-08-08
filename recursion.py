def countdown(i):
    print(f"{i}... ")
    if i <= 1:
        print("done")
        return
    countdown(i - 1)


countdown(10)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))
