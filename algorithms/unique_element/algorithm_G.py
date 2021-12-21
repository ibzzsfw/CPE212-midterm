# Algorithm G (Presort Unique algorithm)

def algorithmG(G):
    G.sort()  # Sort
    for i in range(0, len(G) - 2):  # Check
        if G[i] == G[i + 1]:  # Decision
            return False
    return True
