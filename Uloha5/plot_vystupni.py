from excel_data_import import import_data_column
import numpy as np
import matplotlib.pyplot as plt

cols = [3, 5, 7, 9, 11]
line_colors = ["red", "blue", "limegreen", "mediumorchid", "darkorange"]
marker_colors = ["darkred", "midnightblue", "darkgreen", "indigo", "chocolate"]
line_labels = ["$U_{GS} = 0V$", "$U_{GS} = 2V$", "$U_{GS} = 2,5V$", "$U_{GS} = 2,8V$", "$U_{GS} = 3V$"]

#plt.figure(figsize=(11.69, 8.27))

for col, line_color, marker_color, line_label in zip(cols, line_colors, marker_colors, line_labels):
    U_DS = import_data_column("uloha5.xlsx", "vystupni", 4, col, 30)
    I_D = import_data_column("uloha5.xlsx", "vystupni", 4, col+1, 30) * 1e-3

    plt.plot(np.sort(U_DS), np.sort(I_D), color=line_color, marker='x', markersize='6', markeredgecolor=marker_color, label=line_label)

plt.legend()
plt.ylabel("$I_D\ (mA)$")
plt.xlabel("$U_{DS}\ (V)$")
plt.title("Výstupní charakteristiky tranzistoru BS170")

plt.savefig("vystupni.png")
plt.show()