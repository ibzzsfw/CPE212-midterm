# Algorithm C (Presort Linear search)
def algorithmC(R, K):

    R.sort()
    R.append(float("inf"))
    i = 1  # Initialize
    N = len(R)

    for i in range(0, N):  # Increment

        if (K <= R[i]):  # Compare
            if(K == R[i]):  # End?
                print("C terminate successfully.")
                break
            else:
                print("C terminate unsuccessfully.")
                break
