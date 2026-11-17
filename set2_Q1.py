import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp




def numerical_dx(x,y,sigma):
    return (sigma+3)*x+4*y

def numerical_dy(x,y,sigma):
    return -(9/4)*x + (sigma-3)*y

def system(t, z, sigma):
    x, y = z
    dx = numerical_dx(x,y,sigma)
    dy = numerical_dy(x,y,sigma)
    return [dx, dy]

# Create phase plane plot
sigma = 1

xlim_lower = -4
xlim_upper =  4
ylim_lower = -4
ylim_upper =  4

x = np.linspace(xlim_lower, xlim_upper, 20)
y = np.linspace(ylim_lower, ylim_upper, 20)
X, Y = np.meshgrid(x, y)

U = numerical_dx(X, Y,sigma)
V = numerical_dy(X, Y,sigma)
plt.figure(figsize=(8, 8))
plt.streamplot(X, Y, U, V, density=0.8, color='gray')


# Calculate trajectories from different ICs
initial_conditions = [
    [1, 1],
    [-1, -1],
    [2, -2],
    [-2, 2]
]

for z0 in initial_conditions:
    sol = solve_ivp(
        system,
        [0, 10],
        z0,
        max_step=0.05,
        args = (sigma,)
        )
    plt.plot(sol.y[0], sol.y[1], 'b')
    plt.annotate(f"z0=({z0[0]},{z0[1]})",(sol.y[0][0], sol.y[1][0]), fontweight='bold', color='red')

# Cases for sigma
match sigma:
    case -1:
        plt.plot(0, 0, 'ro', label='FP stable degenerate')
    case 0:
        
        plt.plot([-4,4], [3,-3], 'r', label='Line of FPs unstable degenerate')
    case 1:
        plt.plot(0, 0, 'ro', label='FP unstable degenerate')


plt.xlabel('x')
plt.ylabel('y')
plt.xlim((xlim_lower, xlim_upper))
plt.ylim((ylim_lower, ylim_upper))
plt.title(f"Phase Plane for sigma={sigma}")
plt.legend()
plt.show()
