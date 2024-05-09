import matplotlib.pyplot as plt
import pandas as pd

# Sample DataFrame (replace with your actual data)
data = {'col1': [1, 2, 3, 50], 
        'col2': [5, 3, 5, 10], 
        'col3': [10, 20, 15, 4], 
        'col4': [1, 2, 3, 4],
        'col5': [1, 2, 3, 4],
        'SalePrice': [100000, 120000, 90000, 250000]} 
df = pd.DataFrame(data)

# Determine the number of subplots needed
n_cols = len(df.columns) - 1  # Excluding the target
rows, cols = ((n_cols+1) // 2), 2  # Adjust for desired layout

# Create subplots
fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(5, 4))  # Adjust figsize
# # Flatten axes if rows and cols are not equal
# if n_cols % 2 != 0:
#     axes = axes.flatten()

# Plot scatter plots for each feature against SalePrice
# print(rows, cols)
for i, col in enumerate(df.columns):
    if col != 'SalePrice':
        print(i)
        print(i//rows,i%cols)
        ax = axes[i//cols][i%cols]
        ax.plot(df[col], df['SalePrice'])
        ax.set_xlabel(col)
        ax.set_ylabel('SalePrice')

# Hide unused subplots
for i in range(n_cols, len(axes)):
    axes[i].axis('off')

fig.tight_layout()  # Improve spacing
plt.show()
