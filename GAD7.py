import matplotlib.pyplot as plt

# Dataset
PHQ_Pre = [16, 5, 2, 3, 2, 3, 4, 2, 4, 6, 14, 6, 2, 0, 9, 1, 9, 2, 3, 4, 8, 12, 0, 7, 19, 6, 4, 15, 13, 4, 9, 5, 2]
PHQ_Post = [10, 4, 2, 4, 1, 4, 7, 5, 3, 8, 5, 8, 2, 2, 8, 1, 6, 2, 6, 3, 11, 10, 0, 6, 20, 4, 4, 12, 15, 4, 17, 10, 1]

fig, ax = plt.subplots(figsize=(8.1, 9), facecolor='white')

Filled1 = False
Filled2 = False
Filled3 = False

for i in range(len(PHQ_Pre)):
    x_val = [0, 1]
    y_val = [PHQ_Pre[i], PHQ_Post[i]]
    if PHQ_Pre[i] - PHQ_Post[i] > 4:
        if Filled1 is True:
            plt.plot(x_val, y_val, color="green", linestyle='dashed', marker='o', markersize=3.5)
        else:
            plt.plot(x_val, y_val, color="green", linestyle='dashed', label="Yes (>4) (MCID)", marker='o',
                     markersize=3.5)
            Filled1 = True
    elif PHQ_Pre[i] - PHQ_Post[i] > 0:
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
plt.ylabel('Points', fontweight="bold", fontsize=11)
plt.title('GAD 7', fontweight="bold", fontsize=16, x=0.44, y=0.99)
plt.xticks([])
plt.yticks([0, 5, 10, 15, 20, 25])
plt.ylim(-1.5, 21)
plt.xlim(-0.1, 1.2)

# add legend to the graph
fig.legend(title="Improvement Grades", loc='right', bbox_to_anchor=(1, 0.42))
ax.text(-0.12, -0.8, "Pre-Intervention", fontweight="bold")
ax.text(0.85, -0.8, "Post-Intervention", fontweight="bold")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_label_coords(-0.06, 0.585)

# display the graph
plt.show()
