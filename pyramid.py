import numpy as np
import matplotlib.pyplot as plt
points = np.array([[-1, -1, -1],
                   [1, -1, -1 ],
                    [1, 1, -1],
                   [-1, 1, -1],
                   [0, 0 , 1]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
r = [-1,1]

X, Y = np.meshgrid(r, r)

ax.plot_surface(X,Y,-1, alpha=0.5)
ax.plot_surface(X,Y,0.5, alpha=0.5,  facecolors='r')


ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
