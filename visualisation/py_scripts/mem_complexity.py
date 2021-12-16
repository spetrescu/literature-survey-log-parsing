# importing the library
import numpy as np
import matplotlib.pyplot as plt

# data to be plotted
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([9.019624, 9.019372, 9.01975, 9.019561, 9.019435, 9.019494, 9.019624, 9.019624, 9.019494, 9.019377])

# Drain,Android,2,0:00:00.886391,,1
# Drain,Android,2,0:00:01.164008,,2
# Drain,Android,2,0:00:01.147693,,3
# Drain,Android,2,0:00:00.964603,,4
# Drain,Android,2,0:00:00.911045,,5
# Drain,Android,2,0:00:00.962243,,6
# Drain,Android,2,0:00:00.847813,,7
# Drain,Android,2,0:00:00.845960,,8
# Drain,Android,2,0:00:00.930364,,9
# Drain,Android,2,0:00:01.448028,,10
#
# Drain,Android,4,0:00:01.566823,11.914965,1
# Drain,Android,4,0:00:01.425408,11.915024,2
# Drain,Android,4,0:00:01.572490,11.915154,3
# Drain,Android,4,0:00:01.639290,11.915154,4
# Drain,Android,4,0:00:01.428661,11.914786,5
# Drain,Android,4,0:00:01.515014,11.914912,6
# Drain,Android,4,0:00:01.343486,11.915091,7
# Drain,Android,4,0:00:01.344757,11.915033,8
# Drain,Android,4,0:00:01.343820,11.915038,9
# Drain,Android,4,0:00:01.376518,11.914975,10
#
# Drain,Android,10,0:00:03.620079,21.129919,1
# Drain,Android,10,0:00:04.078159,21.191433,2
# Drain,Android,10,0:00:03.757513,21.264846,3
# Drain,Android,10,0:00:03.517918,21.165002,4
# Drain,Android,10,0:00:03.500902,21.359857,5
# Drain,Android,10,0:00:03.363779,21.124527,6
# Drain,Android,10,0:00:03.353268,21.156568,7
# Drain,Android,10,0:00:04.648784,21.122311,8
# Drain,Android,10,0:00:07.275912,21.196535,9
# Drain,Android,10,0:00:05.846326,21.213345,10
#
# Drain,Android,20,0:00:09.011728,35.100346,1
# Drain,Android,20,0:00:09.231832,35.521916,2
# Drain,Android,20,0:00:09.278660,34.969319,3
# Drain,Android,20,0:00:10.639585,35.479137,4
# Drain,Android,20,0:00:10.276458,35.091841,5
# Drain,Android,20,0:00:11.000893,34.861615,6
# Drain,Android,20,0:00:10.768982,35.232782,7
# Drain,Android,20,0:00:11.982541,35.248409,8
# Drain,Android,20,0:00:10.573528,34.835419,9
# Drain,Android,20,0:00:09.904550,35.16703,10

# plotting
plt.title("Memory consumption for 2k logs")
plt.xlabel("Run no")
plt.ylabel("Memory in MB")
plt.plot(x, y, color="green")
plt.show()