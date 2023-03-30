import matplotlib.pyplot as plt
import numpy as np

# Dataset
PHQ_Pre = [9.1, 6.8, 6.7, 11.3, 7, 10, 7.3, 5.7, 11, 6.3, 7.3, 7, 7.5, 6.7, 8, 6, 5.3, 8.2, 6.5, 8.8, 5.3, 10, 7.2, 6.7, 7.9, 6, 8.5, 7.3,
           15, 8.8]

PHQ_Post = [16.5, 8.3, 10, 12.2, 10, 12.2, 9.5, 6, 11.6, 6, 8.6, 7.3, 8.7, 6.8, 9.2, 10, 8.2, 10.2, 7.5, 8.5, 6.5, 11.1, 13.8, 6.6, 7.4,
            7.3, 8.6, 9.2, 12.5, 10.1]

fig, ax = plt.subplots(figsize=(8.1, 9), facecolor='white')

Filled1 = False
Filled2 = False
Filled3 = False

for i in range(len(PHQ_Pre)):
    x_val = [0, 1]
    y_val = [PHQ_Pre[i], PHQ_Post[i]]
    if PHQ_Post[i] - PHQ_Pre[i] > 1.9:
        if Filled1 is True:
            plt.plot(x_val, y_val, color="green", linestyle='dashed', marker='o', markersize=3.5)
        else:
            plt.plot(x_val, y_val, color="green", linestyle='dashed', label="Yes (>1.9) (*)", marker='o', markersize=3.5)
            Filled1 = True
    elif PHQ_Post[i] - PHQ_Pre[i] > 0:
        if Filled2 is True:
            plt.plot(x_val, y_val, color="blue", linestyle='dashed', marker='o', markersize=3.5)
        else:
            plt.plot(x_val, y_val, color="blue", linestyle='dashed', label="Yes", marker='o', markersize=3.5)
            Filled2 = True
    else:
        if Filled3 is True:
            plt.plot(x_val, y_val, color="red", linestyle='dashed', marker='o', markersize=3.5)
        else:
            plt.plot(x_val, y_val, color="red", linestyle='dashed', label="No", marker='o', markersize=3.5)
            Filled3 = True

plt.plot([0, 0], [0, 200], color="gray", linestyle='solid', linewidth=0.5)
plt.plot([1, 1], [0, 200], color="gray", linestyle='solid', linewidth=0.5)

# add axis labels and a title to the graph
plt.grid("on")
plt.xlabel(' ')
plt.ylabel('METs', fontweight="bold", fontsize=11)
plt.title('Estimated MET Level', fontweight="bold", fontsize=16, x=0.46, y=1.015)
plt.xticks([])
plt.yticks(np.arange(1, 18, 2))
plt.ylim(4.75, 17)
plt.xlim(-0.1, 1.19)

# add legend to the graph
fig.legend(title="Improvement Grades", loc='right', bbox_to_anchor=(1, 0.38))
ax.text(-0.1, 4.5, "Pre-Invervention", fontweight="bold")
ax.text(0.85, 4.5, "Post-Intervention", fontweight="bold")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_label_coords(-0.06, 0.52)

# display the graph
plt.show()
