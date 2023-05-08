import sklearn.datasets as dt
import random
random.seed(75)
import matplotlib.pyplot as plt
import pandas as pd

def prepare_data_problem_2():
    '''
        Fetch and downsample RCV1 dataset to only 500 points.
        https://scikit-learn.org/stable/datasets/real_world.html#rcv1-dataset 
    '''
    rcv1 = dt.fetch_rcv1()

    # Choose 500 samples randomly
    sample_size = 500
    row_indices = random.sample(list(range(rcv1.data.shape[0])),sample_size)
    data_sample = rcv1.data[row_indices,:]

    print(f'Shape of the input data: {data_sample.shape}') # Should be (500, 47236)
    return data_sample

def prepare_data_problem_1():    
    # Downloads from https://www.gapminder.org/data/
    cm_path = 'child_mortality_0_5_year_olds_dying_per_1000_born.csv'
    fe_path = 'children_per_woman_total_fertility.csv'
    cm = pd.read_csv(cm_path).set_index('country')['2017'].to_frame()/10
    fe = pd.read_csv(fe_path).set_index('country')['2017'].to_frame()
    child_data = cm.merge(fe, left_index=True, right_index=True).dropna()
    child_data.columns = ['mortality', 'fertility']
    child_data.head()
    print (child_data)

    return child_data

def joint_scatter_plot(data, approx_data): 
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(data['mortality'],data['fertility'], color='b')
    ax1.scatter(approx_data['mortality'],approx_data['fertility'], color='r')
    plt.show()

