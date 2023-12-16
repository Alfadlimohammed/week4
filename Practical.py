import math
result = math.sqrt(2401)
print(result)
if __name__ == '__main__':
    from math import sqrt

    result = sqrt(2401)
    print(result)
if __name__ == '__main__':
    import math

    result = math.log2(1024)
    print(result)
if __name__ == '__main__':
    def displayTwice(msg):
        print(msg)
        print(msg)


    displayTwice("Hello, World!")
    displayTwice("Testing the function")
    displayTwice(42)
    displayTwice((4, 5, 6))
if __name__ == '__main__':
    def displayTwice(msg):
        """
        Display the given message twice.

        Parameters:
        - msg: The message to be displayed.
        """
        print(msg)
        print(msg)
    help(displayTwice)
if __name__ == '__main__':
    import math
    hypot = lambda x, y: math.hypot(x, y)
    result = hypot(3, 4)
    print(result)
    print(type(result))
if __name__ == '__main__':
    to_seconds = lambda hours, minutes: hours * 3600 + minutes * 60
    print(to_seconds(0, 2))
    print(to_seconds(2, 0))
    print(to_seconds(1, 30))
if __name__ == '__main__':
    to_seconds = lambda hours, minutes=0: hours * 3600 + minutes * 60
    print(to_seconds(1))
    print(to_seconds(2))