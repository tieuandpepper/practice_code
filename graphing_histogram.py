import matplotlib.pyplot as plt
import seaborn as sns
import json
import math
GREEN='#BDFCC9'
BLUE='#C6DEF1'
YELLOW = '#FAEDCB'
original_file = "outputs_original_1204.jsonl"
watermark_file = "outputs_watermark_1204.jsonl"

def read_json(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            record = json.loads(line.strip())  # Parse each line as JSON
            data.append(record)
    return data

uwm_test_results = read_json(original_file)

uwm_mean_score_list = []
uwm_weighted_score_list = []
for test_case in uwm_test_results:
    uwm_mean_score_list.append(test_case["mean_score"])
    uwm_weighted_score_list.append(test_case["weighted_mean_score"])

wm_test_results = read_json(watermark_file)

wm_mean_score_list = []
wm_weighted_score_list = []
for test_case in wm_test_results:
    wm_mean_score_list.append(test_case["mean_score"])
    wm_weighted_score_list.append(test_case["weighted_mean_score"])


# num_bins = math.ceil(math.sqrt(len(mean_score_list)))  # Calculate number of bins
# Example scores
# mean_score_list = [0.1, 0.2, 0.35, 0.4, 0.5, 0.6, 0.65, 0.7, 0.8, 0.9]

max_val = max(max(wm_mean_score_list), max(uwm_mean_score_list))
min_val = min(min(wm_mean_score_list),min(uwm_mean_score_list))

num_bins = 20
# Create histogram
plt.hist(wm_mean_score_list, label="Without Watermark", bins=num_bins, color=YELLOW, edgecolor="black", alpha=0.6,align='mid',rwidth=0.8,range=[min_val,max_val])
plt.hist(uwm_mean_score_list, label="With Watermark", bins=num_bins, color=BLUE, edgecolor="black", alpha=0.8,align='mid',rwidth=0.4,range=[min_val,max_val])
plt.legend()
# Add labels and title
# plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
# plt.savefig("watermark.png", dpi=600, bbox_inches="tight")
# Show the plot
plt.show()

# # importing libraries
# import matplotlib.pyplot as plt
 
# # giving two age groups data
# age_g1 = [1, 3, 5, 10, 15, 17, 18, 16, 19, 21,
#           23, 28, 30, 31, 33, 38, 32, 40, 45, 
#           43, 49, 55, 53, 63, 66, 85, 80, 57, 
#           75, 93, 95]
 
# age_g2 = [6, 4, 15, 17, 19, 21, 28, 23, 31, 36,
#           39, 32, 50, 56, 59, 74, 79, 34, 98, 97,
#           95, 67, 69, 92, 45, 55, 77, 76, 85]
 
# # plotting first histogram
# plt.hist(age_g1, label='Age group1', alpha=.7, edgecolor='black',color=YELLOW, align='mid', bins=20,rwidth=0.7,range=[0,100])
 
# # plotting second histogram
# plt.hist(age_g2, label="Age group2", alpha=.5, bins = 10, range=[0,100],
#          edgecolor='black', color=BLUE, rwidth=0.5, align='mid')
# plt.legend()
 
# # Showing the plot using plt.show()
# plt.show()

