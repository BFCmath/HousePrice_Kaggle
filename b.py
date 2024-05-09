from matplotlib import pyplot as plt
import pandas as pd
def plot_num(df: pd.DataFrame):
    n_cols = len(df.columns) - 1  # Excluding the target
    rows, cols = ((n_cols+1) // 2) , 2  # Adjust for desired layout
    print(n_cols)
    print(rows,cols)
    # 1. Scatter Plots as Subplots
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(10, 8))  

    for i, col in enumerate(df.columns):
        if col != 'SalePrice':
            print(i)
            print(i//rows,i%cols)
            ax = axes[i//cols][i%cols]
            ax.plot(df[col], df['SalePrice'])
            ax.set_xlabel(col)
            ax.set_ylabel('SalePrice')

    fig.tight_layout()  
    plt.show()

    # # 2. Box Plots as Subplots
    # fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(10, 8)) 

    # for i, col in enumerate(added_num_train_data.columns):
    #     row, col = i // cols, i % cols
    #     axes[row, col].boxplot(added_num_train_data[col], vert=False)
    #     axes[row, col].set_title(col)  

    # fig.tight_layout()
    # plt.show() 
data123 = {'col1': [1, 2, 3, 50], 
        'col2': [5, 3, 5, 10], 
        'col3': [10, 20, 15, 4], 
        'col4': [1, 2, 3, 4],
        'col5': [1, 2, 3, 4],
        'SalePrice': [100000, 120000, 90000, 250000]} 
df123 = pd.DataFrame(data123)

plot_num(df123)