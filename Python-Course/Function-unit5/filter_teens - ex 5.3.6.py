def fix_age(age):
    return 0

def filter_teens(a, b, c):

    a = float(input("Please enter a age: "))
    b = float ( input ( "Please enter b age: " ) )
    c = float ( input ( "Please enter c age: " ) )

    if a >= 13 and a < 15 or a > 16 and a <= 19:
        a = fix_age(a)
    if b >= 13 and b < 15 or b > 16 and b <= 19:
        b = fix_age(b)
    if c >= 13 and c < 15 or c > 16 and c <= 19:
        c = fix_age(c)
    return a + b + c

print(filter_teens(0, 0, 0))