import random
def get_random_verification_code():
    r = ""
    for _ in range(6): r += str(random.randrange(0, 10))
    return r