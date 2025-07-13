def solution(n, m):
    g = gcd(n,m)
    return [g,lcm(n,m,g)]
def gcd(n,m):
    while m > 0:
        n,m = m, n % m
    return n
def lcm(n,m,gcd):
    return n*m / gcd