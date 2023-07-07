def hcf_two(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b, c=None):
    if c is None:
        lcm_ab = (a * b) // hcf_two(a, b)
        return lcm_ab
    else:
        lcm_ab = (a * b) // hcf_two(a, b)
        lcm_abc = (lcm_ab * c) // hcf_two(lcm_ab, c)
        return lcm_abc

def hcf_three(a, b, c):
    hcf_ab = hcf_two(a, b)
    hcf_abc = hcf_two(hcf_ab, c)
    return hcf_abc


