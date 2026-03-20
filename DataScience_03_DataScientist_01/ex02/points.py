import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('DataScience_03_DataScientist_01/Train_knight.csv')
# 1. Define the top features to avoid a messy plot
# (30+ features would make the image unreadable)
features = ["Sensitivity","Hability","Strength","Power","Agility","Dexterity","Awareness","Prescience","Reactivity","Midi-chlorien","Slash","Push","Pull","Lightsaber","Survival","Repulse","Friendship","Blocking","Deflection","Mass","Recovery","Evade","Stims","Sprint","Combo","Delay","Attunement","Empowered","Burst","Grasping","knight"]

# 2. Create the Pair Plot
plot = sns.pairplot(df[features], 
                    hue='knight', 
                    palette={'Jedi': 'blue', 'Sith': 'red'}, 
                    diag_kind='kde')

# 3. Add a title (optional)
plot.fig.suptitle("Jedi vs Sith: Top Feature Correlations", y=1.02)

# 4. SAVE THE IMAGE
# 'bbox_inches' ensures the labels don't get cut off
plt.savefig("knight_correlation_matrix.png", dpi=300, bbox_inches='tight')

# 5. Display the result
plt.show()