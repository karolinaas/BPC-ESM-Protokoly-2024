from excel_data_import import import_data_column
import numpy as np
import matplotlib.pyplot as plt

cols = [2, 4]
line_colors = ["red", "blue"]
marker_colors = ["darkred", "midnightblue"]
line_labels = ["$U_{DS} = 5V$", "$U_{DS} = 3V$"]

for col, line_color, marker_color, line_label in zip(cols, line_colors, marker_colors, line_labels):
    U_GS = import_data_column("uloha5.xlsx", "prevodni", 4, col, 11)
    I_D = import_data_column("uloha5.xlsx", "prevodni", 4, col+1, 11) * 1e-3

    plt.plot(np.sort(U_GS), np.sort(I_D), color=line_color, marker='x', markersize='6', markeredgecolor=marker_color, label=line_label)

plt.legend()
plt.ylabel("$I_D\ (mA)$")
plt.xlabel("$U_{GS}\ (V)$")
plt.title("Převodní charakteristiky tranzistoru BS170")

plt.savefig("prevodni.png")
plt.show()