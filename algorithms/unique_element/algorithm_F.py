# Algorithm F (Ordinary Unique algorithm)

def algorithmF(F):
    for i in range(0, len(F) - 2):  # Initialize, Check
        for j in range(i + 1, len(F) - 1):  # List
            if F[i] == F[j]:  # Decision
                return False
    return True
