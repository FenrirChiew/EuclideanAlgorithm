# gcd = Greatest Common Divisor
# lcm = Least Common Multiple

# The Euclidean Algorithm can be described as follows:
# 1. Let A and B be integers with A > B >= 0.
# 2. First check whether B = 0.
#      If yes, gcd (A, B) = A.
#      If it isn’t, then B > 0 and the quotient-remainder theorem can be used to obtain A = B·q + r, 0 <= r < B
#      Thus, gcd (A, B) = gcd (B, r).
#      Since 0 <= r < B < A, the largest number of the pair (B, r) is smaller than the largest number of the pair (A,B).
# 3. Repeat the process in (2), but use B instead of A and r instead of B.
# 4. The repetitions will be terminated when r = 0.

# lcm(A, B) = the product of A and B divides the gcd(A and B).

def gcd(a, b):
    print(f"gcb({a}, {b})")
    c = a % b
    print(f"{a} = {b}({a // b}) + {c}\n")
    if c != 0:
        return gcd(b, c)
    else:
        print(f"gcb({b}, {c})")
        print(f"= {b}\n")
        return b


def lcm(a, b):
    c = a * b / int(gcd(a, b))
    print(f"lcm({a}, {b})")
    print(f"    {a} x {b}")
    print(f"= --------------------")
    print(f"    gcd({a}, {b})")
    print(f"= {c}\n")


if __name__ == '__main__':
    a = 20220
    b = 238
    print(lcm(a, b))
