import pandas as pd

# 1. Calculate the correlation matrix
df = pd.read_csv('DataScience_03_DataScientist_01/Train_knight.csv')

# Initialize the encoder
mapping = {'Jedi': 1, 'Sith': 0}
df['knight'] = df['knight'].map(mapping)
print(df.head())

# 3. Calculate the correlation matrix
# We only want the correlation between 'knight' and the other features
correlations = df.corr()['knight']

# 4. Clean up the output
# We take the absolute value if you want magnitude, 
# but usually, we just sort them to see the strongest relationships.
result = correlations.sort_values(ascending=False)

# 5. Format to match your subject (removing the temporary 'knight_num' if needed)
print(result)