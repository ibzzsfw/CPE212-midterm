# Algorithm B (Quick Linear search)
def algorithmB(R, K):

    R.append(K)
    i = 0  # Initialize
    N = len(R)

    for i in range(0, N):  # Increment

        if (R[i] == K):  # Compare
            if(i < N - 1):  # End?
                print("B terminate successfully.")
                break
            else:
                print("B terminate unsuccessfully.")
                break
