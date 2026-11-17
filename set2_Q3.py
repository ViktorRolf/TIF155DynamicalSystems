import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
from scipy.integrate import solve_ivp

# case alpha = 2, for x1star
A = smp.Matrix([[ 0,  1],
                [-1, -2]])
print(A.is_diagonalizable())

#symbolic expressions
x, y, alpha = smp.symbols('x y alpha')



# solve system
def numerical_dx(x,y,sigma):
    return y

def numerical_dy(x,y,alpha):
    return -np.sin(x) - alpha*y

def system(t, z, alpha):
    x, y = z
    dx = numerical_dx(x,y,alpha)
    dy = numerical_dy(x,y,alpha)
    return [dx, dy]

# Calculate trajectories from different ICs
alphas = (1,2,3)
initial_conditions = [
    [1, 1],
    [-1, -1],
    [2, -2],
    [-2, 2]
]
FP1_class = ["Stable spiral FP","Degenarate stable FP","Stable node FP"]

xlim_lower = -np.pi
xlim_upper =  np.pi
ylim_lower = -np.pi
ylim_upper =  np.pi

for alpha in alphas:
    for z0 in initial_conditions:
        sol = solve_ivp(
            system,
            [0, 10],
            z0,
            max_step=0.05,
            args = (alpha,)
            )
        plt.plot(sol.y[0], sol.y[1], 'b')
        plt.annotate(f"z0=({z0[0]},{z0[1]})",(sol.y[0][0], sol.y[1][0]), fontweight='bold', color='red')


    plt.scatter(0, 0, marker='o',
            color='red', s=100, label = FP1_class[alpha-1],zorder=10)
    plt.scatter(np.pi, 0, marker='o',
            facecolors='none', edgecolors='red', s=100, label ="Unstable FP",zorder=10)


    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim((xlim_lower, xlim_upper))
    plt.ylim((ylim_lower, ylim_upper))
    plt.grid()
    plt.title(f"Phase Plane for alpha={alpha}")
    plt.legend()
    plt.show()
