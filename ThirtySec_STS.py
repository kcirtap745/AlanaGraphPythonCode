import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8.1, 9), facecolor='white')

# Dataset
PHQ_Pre = [13, 9, 19, 10, 12, 13, 7, 16, 10, 12, 10, 10, 7, 7, 10, 12, 13, 14, 11, 10, 10, 8, 14, 10, 9, 8, 13, 6, 12, 12, 15]
PHQ_Post = [16, 11, 20, 12, 15, 15, 11, 20, 6, 12, 14, 6, 8, 10, 11, 16, 11, 15, 12, 12, 14, 10, 16, 13, 10, 10, 25, 10, 15, 13, 18]

Filled1 = False
Filled2 = False
Filled3 = False

for i in range(len(PHQ_Pre)):
    x_val = [0, 1]
    y_val = [PHQ_Pre[i], PHQ_Post[i]]
    if PHQ_Post[i] - PHQ_Pre[i] > 1:
        if Filled1 is True:
            plt.plot(x_val, y_val, color="green", linestyle='dashed', marker='o', markersize=3.5)
        else:
            plt.plot(x_val, y_val, color="green", linestyle='dashed', label="Yes (>1) (MCID)", marker='o',
                     markersize=3.5)
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

plt.plot([0, 0], [0, 50], color="gray", linestyle='solid', linewidth=0.5)
plt.plot([1, 1], [0, 50], color="gray", linestyle='solid', linewidth=0.5)

# add axis labels and a title to the graph
plt.grid("on")
plt.xlabel(' ')
plt.ylabel('Number of Stands', fontweight="bold", fontsize=11)
plt.title('30 Seconds STS', fontweight="bold", fontsize=16, x=0.44, y=0.99)
plt.xticks([])
plt.yticks([0, 5, 10, 15, 20, 25])
plt.ylim(3, 26)
plt.xlim(-0.1, 1.22)

# add legend to the graph
fig.legend(title="Improvement Grades", loc='right', bbox_to_anchor=(1, 0.42))
ax.text(-0.12, 2.25, "Pre-Intervention", fontweight="bold")
ax.text(0.85, 2.22, "Post-Intervention", fontweight="bold")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_label_coords(-0.06, 0.585)

# display the graph
plt.show()
