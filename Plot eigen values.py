import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create plots
fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# Eigenvalue 1
ax1.plot_surface(X, Y, np.abs(eigenvalues[0]), cmap='viridis')
ax1.set_title('Absolute Value of First Eigenvalue')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# Eigenvalue 2
ax2.plot_surface(X, Y, np.abs(eigenvalues[1]), cmap='viridis')
ax2.set_title('Absolute Value of Second Eigenvalue')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.show()
