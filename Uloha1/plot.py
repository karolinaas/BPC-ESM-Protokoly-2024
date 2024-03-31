import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Input data
propust_1n4148 = np.array([[0,0.527,0.561,0.582,0.592,0.599,0.634,0.656,0.673,0.686,0.697,0.707,0.716,0.723,0.730],[0,0.25,0.5,0.75,0.9,1,2,3,4,5,6,7,8,9,10]])
zaver_1n4148 = np.array([[0,0.1,0.25,0.5,1,2,3,4,5,6,7,8,9,10],[0,0.011,0.027,0.053,0.106,0.205,0.303,0.403,0.505,0.603,0.703,0.804,0.903,1.004]])

propust_bat42 = np.array([[0,0.239,0.259,0.271,0.279,0.286,0.292,0.297,0.301,0.305,0.309,0.222,0.233,0.202,0.179],[0,1,2,3,4,5,6,7,8,9,10,0.5,0.75,0.25,0.1]])
zaver_bat42 = np.array([[0,1,2,3,4,5,6,7,8,9,10,0.5,1.5,0.25,0.1],[0,0.238,0.359,0.473,0.589,0.7,0.814,0.924,1.035,1.148,1.257,0.173,0.297,0.141,0.118]])

propust_LED = np.array([[0,1.709,1.737,1.754,1.768,1.777,1.786,1.794,1.802,1.808,1.814,1.686,1.66,1.625],[0,1,2,3,4,5,6,7,8,9,10,0.5,0.25,0.1]])
zaver_LED = np.array([[0,1,2,3,4,5,6,7,8,9,10,0.5],[0,0.103,0.202,0.308,0.407,0.508,0.607,0.708,0.805,0.904,1.001,0.053]])

fig = plt.figure()
grid = gridspec.GridSpec(nrows=2, ncols=2, hspace=0, wspace=0, figure=fig)

# Plot drawing
i_quadrant = fig.add_subplot(grid[0, 1], zorder=3)
i_quadrant.axline((np.max(propust_1n4148[0]), np.max(propust_1n4148[1])), (np.partition(propust_1n4148[0], -2)[-2], np.partition(propust_1n4148[1], -2)[-2]), color='darkviolet', linestyle='--')
i_quadrant.axline((np.max(propust_bat42[0]), np.max(propust_bat42[1])), (np.partition(propust_bat42[0], -2)[-2], np.partition(propust_bat42[1], -2)[-2]), color='darkviolet', linestyle='--')
i_quadrant.axline((np.max(propust_LED[0]), np.max(propust_LED[1])), (np.partition(propust_LED[0], -2)[-2], np.partition(propust_LED[1], -2)[-2]), color='darkviolet', linestyle='--')
i_quadrant.plot(np.sort(propust_1n4148[0]), np.sort(propust_1n4148[1]), color='red', marker='x', markersize='5', markeredgecolor='darkred')
i_quadrant.plot(np.sort(propust_bat42[0]), np.sort(propust_bat42[1]), color='limegreen', marker='x', markersize='5', markeredgecolor='darkgreen')
i_quadrant.plot(np.sort(propust_LED[0]), np.sort(propust_LED[1]), color='blue', marker='x', markersize='5', markeredgecolor='midnightblue')
i_quadrant.margins(0)

ii_quadrant = fig.add_subplot(grid[0, 0], zorder=2, sharey=i_quadrant)
ii_quadrant.plot(0, 0, color='red', marker='x', markersize='5', markeredgecolor='darkred', label="1N4148")
ii_quadrant.plot(0, 0, color='limegreen', marker='x', markersize='5', markeredgecolor='darkgreen', label="BAT42")
ii_quadrant.plot(0, 0, color='blue', marker='x', markersize='5', markeredgecolor='midnightblue', label="LED")
ii_quadrant.margins(0)

iii_quadrant = fig.add_subplot(grid[1, 0], zorder=0, sharex=ii_quadrant)
iii_quadrant.plot(np.sort(zaver_1n4148[0]), np.sort(zaver_1n4148[1]), color='red', marker='x', markersize='5', markeredgecolor='darkred', label="1N4148")
iii_quadrant.plot(np.sort(zaver_bat42[0]), np.sort(zaver_bat42[1]), color='limegreen', marker='x', markersize='5', markeredgecolor='darkgreen', label="BAT42")
iii_quadrant.plot(np.sort(zaver_LED[0]), np.sort(zaver_LED[1]), color='blue', marker='x', markersize='5', markeredgecolor='midnightblue', label="LED")
iii_quadrant.margins(0)

iv_quadrant = fig.add_subplot(grid[1, 1], zorder=1, sharex=i_quadrant, sharey=iii_quadrant)
#iv_quadrant.plot(x, y)
iv_quadrant.margins(0)

# Axes box settings
i_quadrant.spines['top'].set_visible(False)
i_quadrant.spines['right'].set_visible(False)
ii_quadrant.spines['top'].set_visible(False)
ii_quadrant.spines['left'].set_visible(False)
iii_quadrant.spines['left'].set_visible(False)
iii_quadrant.spines['bottom'].set_visible(False)
iv_quadrant.spines['right'].set_visible(False)
iv_quadrant.spines['bottom'].set_visible(False)

# Tick settings
ii_quadrant.tick_params(axis='both', labelleft=False)
ii_quadrant.tick_params(axis='y', left=False)
ii_quadrant.tick_params(axis='x', direction='in', pad=-15)

iii_quadrant.tick_params(axis='both', labelleft=False, labelbottom=False, left=False, bottom=False)

iv_quadrant.tick_params(axis='both', labelbottom=False, bottom=False)
iv_quadrant.tick_params(axis='y', direction='in', pad=-22)

i_quadrant.set_xticks(np.arange(0, 2, 0.2))
# i_quadrant.set_yticks(np.arange(0, np.max(data_propust[1]) + 1, 1))
# ii_quadrant.set_xticks(np.arange(0, np.max(data_zaver[0]) + 1, 1))
# iv_quadrant.set_yticks(np.arange(0, np.max(data_zaver[1]) + 0.1, 0.2))

plt.setp(i_quadrant.get_xticklabels()[0], visible=False)
plt.setp(i_quadrant.get_yticklabels()[0], visible=False)
plt.setp(ii_quadrant.get_xticklabels()[0], visible=False)
plt.setp(iv_quadrant.get_yticklabels()[0], visible=False)

# Axis settings
i_quadrant.set_xlabel("$U_F\ (V)$", loc='right')
i_quadrant.set_ylabel("$I_F\ (mA)$", loc='top')
ii_quadrant.set_xlabel("$U_R\ (V)$", loc='left')
iv_quadrant.set_ylabel("$I_R\ (\mu A)$", loc='bottom')

i_quadrant.set_ylim([0,11])
i_quadrant.set_xlim([0, 1.914])
ii_quadrant.set_xlim([0,11])
iv_quadrant.set_ylim([0,1.1])

iii_quadrant.invert_xaxis()
iii_quadrant.invert_yaxis()

ii_quadrant.legend(loc="center")

plt.show()