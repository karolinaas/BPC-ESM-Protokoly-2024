from excel_data_import import import_data_column
import numpy as np
import matplotlib.pyplot as plt


# Aplitudová kmitočtová charakteristika
akch_f = import_data_column("uloha4.xlsx", "List1", 4, 2, 19)
akch_Audb = import_data_column("uloha4.xlsx", "List1", 4, 5, 19)

plt.figure(1)
plt.axhline(np.max(akch_Audb), color='lightblue', linestyle='--')
plt.axhline(np.max(akch_Audb) - 3, color='lightblue', linestyle='--')
plt.axvline(1.6e+06, ymax=0.8, color='lightblue', linestyle='--')
plt.text(1.6e+06, 31.1, "1,6MHz", horizontalalignment="center", verticalalignment="center", color="darkblue")
plt.text(1.5e+5, np.max(akch_Audb), "$A_{UdB_{MAX}}$", horizontalalignment="left", verticalalignment="top", color="darkblue")
plt.text(1.5e+5, np.max(akch_Audb) - 3, "$A_{UdB_{MAX}} - 3dB$", horizontalalignment="left", verticalalignment="top", color="darkblue")
plt.plot(akch_f, akch_Audb, color='blue', marker='x', markersize='6', markeredgecolor='midnightblue')
plt.xscale("log")
plt.grid(True, which="both")
plt.ylabel("$A_{UdB}\ (dB)$")
plt.xlabel("$f\ (Hz)$")
plt.title("Aplitudová kmitočtová charakteristika tranzistoru BC546B")

# Převodní charakteristika
pch_Uvst = import_data_column("uloha4.xlsx", "List2", 4, 3, 19)
pch_Uvyst = import_data_column("uloha4.xlsx", "List2", 4, 4, 19)

plt.figure(2)
xlim = np.array([pch_Uvst[0], pch_Uvst[-5]])
k, q = np.polyfit(pch_Uvst[:-5], pch_Uvyst[:-5], 1)
plt.plot(xlim, k * xlim + q, color='lightblue', linestyle='--')
plt.plot(pch_Uvst, pch_Uvyst, color='blue', marker='x', markersize='6', markeredgecolor='midnightblue')
plt.grid(True)
plt.ylabel("$U_{výst}\ (mV)$")
plt.xlabel("$U_{vst}\ (V)$")
plt.title("Převodní charakteristika tranzistoru BC546B")

plt.show()
