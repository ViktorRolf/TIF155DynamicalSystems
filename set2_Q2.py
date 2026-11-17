import numpy as np
import matplotlib.pyplot as plt
import sympy as smp

#symbolic expressions
A, x, t, S, eJt, sigma= smp.symbols('A x t P eJt sigma')
u, v = smp.symbols('u v')


A = smp.Matrix([[(sigma+1),3],[-2,(sigma-1)]])
eigenvalue, _, eigenvectors = A.eigenvects()[0]

print(eigenvalue)
print(eigenvectors)

S = smp.Matrix([[smp.Rational(-1/2),smp.Rational(1/2)*smp.sqrt(5)],[1,0]])

ejt = smp.exp(sigma*t) * smp.Matrix([
    [smp.cos(smp.sqrt(5)*t), -smp.sin(smp.sqrt(5)*t)],
    [smp.sin(smp.sqrt(5)*t), smp.cos(smp.sqrt(5)*t)]
])

y0 = S.inv() * smp.Matrix([[u],[v]])

x = smp.simplify(smp.simplify((S*ejt)*y0))
print(x)




# c)
numeric_sigma = (-1/10, 0, 1/10)[1] #Change this for each plot
T = 30
N = T*10
tx = np.linspace(0,T,N)
ICs          = ([1,0], [1.5,-1], [0,2.5])
colors       = ("red","blue","green")

numeric_x = x.subs({sigma: numeric_sigma}) 
for j in range(3):
    trajectories = ([],[])
    for i in range(N):
        numeric_x_txi = numeric_x.subs({t: tx[i], u: ICs[j][0], v: ICs[j][1]})   
        trajectories[0].append(smp.N(numeric_x_txi[0]))
        trajectories[1].append(smp.N(numeric_x_txi[1]))
    
    plt.plot(trajectories[0],trajectories[1],label=f"ICs u,v={ICs[j][0]}, {ICs[j][1]}", color=colors[j])
    plt.scatter(ICs[j][0], ICs[j][1], marker='x', color=colors[j], s=100)

xlim_lower = -5
xlim_upper =  5
ylim_lower = -5
ylim_upper =  5

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((xlim_lower, xlim_upper))
plt.ylim((ylim_lower, ylim_upper))
plt.title(f"Trajectories for sigma={numeric_sigma}, with ICs marked with crosses")
plt.legend()
plt.show()


# e)


ellipse = smp.Matrix([[smp.cos(smp.sqrt(5)*t)], [smp.sin(smp.sqrt(5)*t)]])
rotated_ellipse = smp.simplify(S*ellipse)
print(rotated_ellipse)

'''
trajectories = ([],[])
tx = np.linspace(0,2*np.pi,100)
for i in range(100):
    numeric_rotated_ellipse = rotated_ellipse.subs({t: tx[i]})   
    trajectories[0].append(smp.N(numeric_rotated_ellipse[0]))
    trajectories[1].append(smp.N(numeric_rotated_ellipse[1]))
plt.scatter(trajectories[0][0],trajectories[1][0], marker='x', s=100)
plt.plot(trajectories[0],trajectories[1],label=f"ellipse")
plt.show()
'''

