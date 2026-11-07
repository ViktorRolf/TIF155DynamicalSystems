import matplotlib.pyplot as plt
import numpy as np
import sympy as smp

#symbolic expressions
f, fp, x, r, h, hc = smp.symbols('f fp, x r h hc')

f = h + x*(r-x)
fp = r-2*x
hc = -r**2/4

#print roots of f
roots = smp.solve(f,x)
print(roots)

#calculate h_c curve
r_vals = np.linspace(-2,2)
hc_vals = []
for rs in r_vals:
    hc_vals.append(float(hc.subs(r,rs)))

#Plot fig1, h,r plane
fig, ax = plt.subplots()

plt.plot(hc_vals,r_vals,color='orange',label="Bif curve, 1 half stable FP")
plt.text(-0.8,0,"No FPs\n4h+r**2<0")
plt.text(-0.1,-1.5,"1 stable FP and 1 unstable FP \n4h+r**2>0")

ax.set_title("(h,r)-space plot,\namount of fix points (FPs)\nand bifurcation curve [h_c(r),r]")
ax.set_xlabel("h")
ax.set_ylabel("r")
ax.set_xlim(-1,0.5)
ax.set_ylim(-2,2)
ax.legend()
ax.grid()
plt.show()


#setup for fig2 3d plot of (h,r,x*)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
H = np.arange(-1, 0.5, 0.01)
R = np.arange(-2, 2, 0.01)
H, R = np.meshgrid(H, R)

# f' = r - 2x
# so f'(Rm) = R - 2*(R/2 - sqrt(4*H + R**2)/2) = sqrt(4*H + R**2) > 0 (when 4*H + R**2 > 0)
# vice versa f'(Rp) = - sqrt(4*H + R**2) < 0 (when 4*H + R**2 > 0)

# => Rm unstable, Rp stable
Rm = R/2 - np.sqrt(4*H + R**2)/2
Rp = R/2 + np.sqrt(4*H + R**2)/2

#If arg < 0 then np.sqrt(arg) return None so Rm/Rp will have none value in the region wehre we have no FPs

surf = ax.plot_surface(H, R, Rm, cmap="Blues",
                       linewidth=0, antialiased=False,
                       label="Unstable FPs")
surf = ax.plot_surface(H, R, Rp, cmap="Reds",
                       linewidth=0, antialiased=False,
                       label="Stable FPs")

ax.set_xlabel("h")
ax.set_ylabel("r")
ax.set_zlabel("FPs (x*)")
ax.set_title("Surface plot for FPs\nas a function of r and h")
ax.legend()
plt.show()