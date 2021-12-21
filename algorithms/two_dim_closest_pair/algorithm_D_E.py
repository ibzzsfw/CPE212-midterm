import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(p1, p2):
        return math.sqrt(((p1.x - p2.x)*(p1.x - p2.x)) + ((p1.y - p2.y)*(p1.y - p2.y)))

    # Algorithm D (Brute-force 2D-Closest pair)

    def algorithmD(P):

        dist = float('inf')  # Initialize

        for i in range(0, len(P) - 1):  # Initialize, Increment
            for j in range(i + 1, len(P)):  # Compare

                if (Point.distance(P[i], P[j]) <= dist):  # Compare
                    dist = Point.distance(P[i], P[j])

        return dist

    # Algorithm E (Devide-and-Conquer 2D-Closest pair)

    def algorithmE(P):

        # Initialize
        X = sorted(P, key=lambda P: P.x)
        Y = sorted(P, key=lambda P: P.y)

        # Base case
        if (len(P) <= 3):
            return Point.algorithmD(P)

        # Compute
        Pl = X[:math.ceil(len(P) / 2)]
        Pr = X[math.floor(len(P) / 2):]

        # Determine
        dl = Point.algorithmE(Pl)
        dr = Point.algorithmE(Pr)
        d = min(dl, dr)

        # Delete
        Yp = []
        for p in Y:
            if (abs(p.x) <= 2 * d):
                Yp.append(p)
        # Scan
        dp = float('inf')
        for i in range(len(Yp)):
            for j in range(i + 1, min(i + 7, len(Yp))):
                if (dp < Point.distance(Yp[i], Yp[j])):
                    dp = Point.distance(Yp[i], Yp[j])

        return min(d, dp)
