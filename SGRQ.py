import matplotlib.pyplot as plt
import numpy as np

# Dataset
PHQ_Pre = [48.7, 65.4, 17.9, 54.1, 39.7, 56, 56.1, 14.6, 65.7, 52.8, 42.8, 65.7, 30.1, 67, 65.8, 46.1, 46.6, 37.8, 16.5, 9.5, 50.7, 31.5,
           48.6, 23, 44.5, 51.6, 57.9, 57.8, 92.5, 22.3, 22.7, 12, 37.8]
PHQ_Post = [5.8, 44.8, 10.6, 22.2, 31.4, 43, 40.6, 7, 62.2, 43.9, 16.7, 62.2, 28.8, 56.7, 59.2, 32.6, 55.7, 24.7, 0, 3.2, 41.8, 35, 53.2,
            12.3, 50.54, 52.8, 58.9, 32.37, 64.12, 19.1, 16.3, 19.86, 15.79]

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

plt.plot([0, 0], [0, 200], color="gray", linestyle='solid', linewidth=0.5)
plt.plot([1, 1], [0, 200], color="gray", linestyle='solid', linewidth=0.5)

# add axis labels and a title to the graph
plt.grid("on")
plt.xlabel(' ')
plt.ylabel('Points', fontweight="bold", fontsize=11)
plt.title('SGRQ', fontweight="bold", fontsize=16, x=0.46, y=0.99)
plt.xticks([])
plt.yticks(np.arange(*(0, 100, 5)))
plt.ylim(-1.5, 99)
plt.xlim(-0.1, 1.2)

# add legend to the graph
fig.legend(title="Improvement Grades", loc='right', bbox_to_anchor=(1, 0.41))
ax.text(-0.12, -3.8, "Pre-Intervention", fontweight="bold")
ax.text(0.85, -3.8, "Post-Intervention", fontweight="bold")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_label_coords(-0.06, 0.52)

# display the graph
plt.show()
