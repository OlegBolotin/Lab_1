def is_int(value):
    return str.isdigit(value)

pin = int(input())
pin_str = str(pin)
a = is_int(pin_str)
print(a)
if (len(str(pin)) == 4 or len(str(pin)) == 6):
    print("Hello world")
