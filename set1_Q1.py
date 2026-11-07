import matplotlib.pyplot as plt
import numpy as np
import sympy as smp

#setting up symbolics (rf is f solved for r)
f, x, r, rf = smp.symbols('f x r rf')

f = smp.Rational(1,5) + smp.Rational(7,10)/(1 + smp.exp(80*(1-x))) - r*x**4
fp = smp.diff(f, x)

rf = ( smp.Rational(1,5) + smp.Rational(7,10)/(1 + smp.exp(80*(1-x))) )/x**4
r_eval = smp.symbols('f_eval')


# calculating r for each fp
N = 150
xvals = np.linspace(0.70, 1.4, N)
rvals = []
r_stability = dict()

for xv in xvals:
    r_eval = rf.subs(x, xv).evalf()
    rvals.append(r_eval)

    if fp.subs([(x,xv), (r,r_eval)]) < 0:
        r_stability[r_eval] = True  # 'stable'
    else:
        r_stability[r_eval] = False # 'unstable'
        
# plot step by step and checking when to use dahsed or solid line
fig, ax = plt.subplots()
for i in range(N-1):
    if r_stability[rvals[i]]: # 'stable'
        plt.plot(rvals[i:i+2],xvals[i:i+2],color='orange',)
    else:                     # 'unstable'
        plt.plot(rvals[i:i+2],xvals[i:i+2],linestyle="--", color='red')

#annotating fixed points, (exact positions added by using the solver below)
ax.annotate("Saddle node bif\nSnowball",
            xy=(0.749, 1.03),
            xytext=(0.7, 1.2),
            textcoords='data',
            arrowprops=dict(arrowstyle='->'))

ax.annotate("Saddle node bif\nWarm",
            xy=(0.261, 0.949),
            xytext=(0.22, 1.1),
            textcoords='data',
            arrowprops=dict(arrowstyle='->'))

# finalizing plot
ax.set_title("FPs against parameter r, stable/unstable denoted solid/dashed")
ax.set_xlabel("r")
ax.set_ylabel("Fixed point")
ax.grid()
plt.show()


#Find numerical FP
snowball_pair = smp.nsolve((f, fp), (r, x), (0.749, 1.03))
print(f'r critical ={float(snowball_pair[0]):.3g} with FP= {float(snowball_pair[1]):.3g}')
