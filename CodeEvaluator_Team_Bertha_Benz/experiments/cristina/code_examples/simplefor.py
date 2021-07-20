def a():
    for _ in range(10000000):  # do something CPU heavy
        pass

if __name__=="__main__":
    a()
    print("hello")
