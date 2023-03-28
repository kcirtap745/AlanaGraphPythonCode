import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 8), facecolor='white')

# Dataset
PHQ_Pre = [8, 4, 1, 8, 6, 12, 14, 1, 9, 16, 11, 9, 7, 7, 10, 3, 5, 3, 11, 1, 11, 8, 8, 11, 14, 3, 9, 21, 4, 7, 9, 3]
PHQ_Post = [3, 2, 4, 5, 10, 13, 7, 0, 14, 10, 4, 14, 3, 2, 11, 2, 6, 6, 3, 1, 9, 9, 6, 6, 17, 1, 13, 19, 5, 10, 9, 4]

Zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Ones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

Filled1 = False
Filled2 = False
Filled3 = False

for i in range(len(PHQ_Pre)):
    x_val = [0, 1]
    y_val = [PHQ_Pre[i], PHQ_Post[i]]
    if PHQ_Post[i] - PHQ_Pre[i] > 3.7:
        if Filled1 is True:
            plt.plot(x_val, y_val, color="green", linestyle='dashed', marker='o', markersize=3.5)
        else:
            plt.plot(x_val, y_val, color="green", linestyle='dashed', label="Yes (> 3.7)", marker='o', markersize=3.5)
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
plt.ylabel('Symptoms')
plt.title('PHQ')
plt.xticks([])
plt.yticks([0, 5, 10, 15, 20])
plt.ylim(0, 22)

# add legend to the graph
fig.legend(loc='upper right')
ax.text(-0.06, -1.1, "Pre-Intervention")
ax.text(0.9, -1.1, "Post-Intervention")

# display the graph
plt.show()
