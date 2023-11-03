import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pk

with open("ctrl_vari.pkl", "rb") as fcv:
    ctrl_vari: dict[str, list[int]] = pk.load(fcv)
with open("heur_ctrl.pkl", "rb") as fcv:
    heur_cnt: dict[str, int] = pk.load(fcv)
with open("ndcnt_ctrl.pkl", "rb") as fcv:
    ndcnt: dict[str, int] = pk.load(fcv)

num_subplots = len(ctrl_vari)
fig, axes = plt.subplots(1, num_subplots, figsize=(12, 4))
# Loop through the dictionary and plot histograms on each subplot
for i, (label, data) in enumerate(ctrl_vari.items()):
    ax = axes[i]
    sns.boxplot(ctrl_vari[label], ax=ax)
    ax.scatter(0, heur_cnt[label], color='green',
               marker='X', label='Heuristic solution')
    ax.scatter(0, ndcnt[label], color='red',
               marker='o', label='Both polarities')
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histo {label}')

plt.tight_layout()
plt.show()
