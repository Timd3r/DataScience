import seaborn as sns
import matplotlib.pyplot as plt
import math
import pandas as pd
# 1. Prepare your feature list (everything except 'Survival' and 'knight')
df = pd.read_csv('DataScience_03_DataScientist_01/Train_knight.csv')
target_feature = 'Survival'
other_features = [col for col in df.columns if col not in [target_feature, 'knight']]

# 2. Calculate grid size (e.g., if you have 30 features, a 6x5 grid)
cols_count = 5
rows_count = math.ceil(len(other_features) / cols_count)

# 3. Create the figure
fig, axes = plt.subplots(rows_count, cols_count, figsize=(20, rows_count * 4))
axes = axes.flatten() # Flatten to loop easily

for i, feature in enumerate(other_features):
    sns.scatterplot(ax=axes[i], data=df, x=feature, y=target_feature, 
                    hue='knight', palette={'Jedi': 'blue', 'Sith': 'red'}, alpha=0.6)
    axes[i].set_title(f'{target_feature} vs {feature}')
    axes[i].legend(title='Knight', loc='upper right')

# 4. Remove any empty subplots at the end
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()

# 5. Save the result
print(df.describe().loc[['min', 'max']])