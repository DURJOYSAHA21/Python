a=1
try:
    b=int(input('Input'))
    a=a/b
except ZeroDivisionError:
    print("Cannot divide")
except ValueError:
    print("not num")
except:
    print("wrong")
else:
    print(a)
finally:
    print("i will print")