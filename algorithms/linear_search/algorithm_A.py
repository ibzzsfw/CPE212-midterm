# Algorithm A (Linear search)
def algorithmA(R, K):

    i = 0  # Initialize
    N = len(R)
    for i in range(0, N):  # Increment

        if (R[i] == K):  # Compare
            print("A terminate successfully.")
            break

    if (i == N - 1 and R[i] != K):
        print("A terminate unsuccessfully.")
