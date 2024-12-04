import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import MaxNLocator
# Array of results
violation_rates = [9,15,11,10,12,9,2,3]

# Names of the LLMs
models = ['CodeGen','VeriGen','DeepSeek','RTLCoder','CodeV','OriGen','Llama', 'FreeV']

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(4.5, 2.2))

# Set the width of each bar
bar_width = 0.5
BLUE='#FFFACD'
GREEN='#BDFCC9'
PURPLE='#D4A4F4'
YELLOW='#FFDAB9'
color_list = [BLUE,BLUE,YELLOW,YELLOW,YELLOW,YELLOW,GREEN,GREEN]
patterns = ["///", "", "///", "", "", "", "///", ""]

x = np.arange(len(models))

for i, (rate, color, pattern) in enumerate(zip(violation_rates, color_list, patterns)):
    ax.bar(
        x[i],
        rate,
        color=color,
        edgecolor="black",
        hatch=pattern,
        label="Base model" if pattern and "Base model" not in ax.get_legend_handles_labels()[1] else "",
    )

# Add legend
handles, labels = ax.get_legend_handles_labels()
custom_handles = []
for handle, label in zip(handles, labels):
    if label == "Base model":
        custom_handles.append(
            mpatches.Patch(facecolor="none", edgecolor="black", hatch="///", label=label)
        )
    else:
        custom_handles.append(handle)
ax.legend(custom_handles, labels, loc="upper right")


# Customize the plot
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=45, ha="right",fontsize=9)
ax.set_ylabel("Violation Rate (%)")
# ax.set_title("Violation Rates Across Models")
plt.xlabel('Model')
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6))  # 15 ticks
plt.tight_layout()
plt.savefig("copyright_fig.png", dpi=600, bbox_inches="tight")
plt.show()



# # Plot the bar chart
# plt.bar(models, results, color=color_list, width=bar_width, edgecolor='grey')
# plt.xticks(rotation=45,fontsize=9)
# # Add labels and title
# plt.ylabel('Violation Rate (%)')
# # plt.title('Copyrighted of Different LLMs')

# # Add legend
# # plt.legend(['Performance'])
# plt.tight_layout()

# # Show the plot
# plt.savefig("copyright_fig.png", dpi=600, bbox_inches="tight")
# plt.show()