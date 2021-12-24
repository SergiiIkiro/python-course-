import numpy_financial as npf
import numpy as np
import matplotlib.pyplot as plt

rev = [3869.47, 7188.46, 22203.31, 29391.78, 33269.24, 49976.65, 59218.56, 40734.22]

cf1 = [-500000, 38694, 71884, 222033, 293917, 332692, 499766, 592185, 407342] * 10

print("Option 1: ", npf.irr(cf1))

plt.plot(rev)
plt.savefig(plt.plot.png)

res = np.std(rev)
print(res)
