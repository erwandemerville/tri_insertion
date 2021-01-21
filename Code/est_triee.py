def est_triee(T):
    v = -1
    for i in range(len(T)):
        if T[i] >= v:
            v = T[i]
        else:
            return False
    return True