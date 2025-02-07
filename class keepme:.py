class keepme:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, *args, **kwargs):        
        key = str(args) + str(kwargs)
        if key in self.cache:
            return self.cache[key]

        value = self.function(*args, **kwargs)
        self.cache[key] = value
        return value

@keepme
def fib(n):
    if n in (0, 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(0, 10):
    print(fib(i))

print(fib.cache)
print(fib.cache)
