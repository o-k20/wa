import numpy as np

# Define the function F(x, y)
def F(x, y):
    return np.exp(1j * y) + 2 * np.exp(-2j * y / 3) * np.cos(np.sqrt(3) / 2 * x)

# Define the matrix M(x, y)
def matrix_M(x, y):
    f = F(x, y)
    return np.array([[0, f], [np.conjugate(f), 0]])

# Grid setup
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)

# Prepare to store eigenvalues
eigenvalues = np.zeros((2, 100, 100), dtype=complex)

# Diagonalize M at each grid point
for i in range(100):
    for j in range(100):
        eigvals, _ = np.linalg.eig(matrix_M(X[i, j], Y[i, j]))
        eigenvalues[:, i, j] = eigvals
