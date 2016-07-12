r"""
This module should handle the transition counting and transition matrix estimation.
"""

import utilities as util



def normalize(M):
    """
    Subfunction for T. It normalizes the matrix given as input.

    INPUT:
        - M = A matrix M.

    OUTPUT:
        - M0 = The matrix M normalized, with rows that add to 1.
    """

    M0 = np.array(M)
    if M0.ndim == 1:
        s = M0.sum()
        return np.divide(M0, s)

    elif M0.ndim == 2:
        s = M0.sum(axis=1)
        return np.divide(M0, s[:, np.newaxis])
    else:
        return "Normalize. Wrong input"



def T_non_reversible(C):
    """
    Function to get the transition matrix from the count matrix. It simply normalizes the count matrix.
    Is easy, and useful for very large amount of data.

    INPUT:
        - C = Count matrix.

    OUTPUT:
        - P = The probability transition matrix of the markov model.
    """

    return normalize(C)



def T_reversible(C, max_iterations=100, error=0.1):
    """
    Function to get the transition matrix from the count matrix. It gives a matrix that is reversible.
    That is, the markov model obtained is reversible (it satisfies the detailed balance equations).
    Detailed balance implies that, around any closed cycle of states, there is no net flow of probability.
    For example, it implies that, for all a, b and c,
    T( a , b ) T( b , c ) T( c , a ) = T( a , c ) T( c , b ) T( b , a ).

    INPUT:
        - C = Count matrix constructed with lag tau.
        - max_iterations = maximum number of iterations we allow.
        - error = error that we consider to understand that the iteration has converged.

    OUTPUT:
        - P = The probability transition matrix of the markov model.
    """

    C_i = C.sum(axis=1)  # array of the sums of the rows of C
    C_j = C.sum(axis=0)  # array of the sums of the columns of C

    P = T_non_reversible(C)
    P = (obtain_active_set(P))[0]
    pi = stationary_sol(P)

    P = np.multiply(P, pi)
    X_0 = P  # initial state

    it = 0
    Er = 0.2  # TO BE CHANGED

    while (Er > error) and (it < max_iterations):
        Xi_0 = X_0.sum(axis=1)  # array of the sums of the rows of X_0
        Xj_0 = X_0.sum(axis=0)  # array of the sums of the rows of X_0

        X_1 = C + np.matrix.transpose(C)
        X_1 = np.divide(X_1, ((C_i) / (Xi_0) + (C_j) / (Xj_0)))

        X_0 = X_1
        it += 1

    P = normalize(X_1)
    return P