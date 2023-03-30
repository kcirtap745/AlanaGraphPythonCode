import matplotlib.pyplot as plt
import numpy as np

# Dataset
PHQ_Pre = [5, 5.1, 8.6, 4.8, 7.6, 5.5, 4, 8.3, 4.7, 5.2, 5.3, 4.5, 5, 5.9, 3.6, 3.9, 6.2, 4.8, 6.6, 3.9, 7.5, 5.4, 5, 3.9, 6.4, 4.6, 6.4,
           5.5, 9.1, 6.7]

PHQ_Post = [7.5, 6.35, 9.1, 7.6, 9.1, 7.2, 3.6, 8.7, 4.5, 6.4, 5.5, 6.5, 5.1, 6.9, 4.4, 4.5, 7.6, 5.5, 6.3, 4.8, 8.7, 5.5, 4.9, 4.4, 8.2,
            5.5, 6.4, 6.9, 8.7, 7.6]

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
plt.title('MET Level', fontweight="bold", fontsize=16, x=0.46, y=0.99)
plt.xticks([])
plt.yticks(np.arange(0, 10, 1))
plt.ylim(2.9, 10)
plt.xlim(-0.1, 1.19)

# add legend to the graph
fig.legend(title="Improvement Grades", loc='right', bbox_to_anchor=(1, 0.392))
ax.text(-0.1, 2.65, "Pre-Intervention", fontweight="bold")
ax.text(0.87, 2.65, "Post-Intervention", fontweight="bold")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_label_coords(-0.06, 0.52)

# display the graph
plt.show()
