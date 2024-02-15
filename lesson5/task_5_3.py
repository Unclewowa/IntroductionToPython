import numpy as np

if __name__ == '__main__':
    a_1_5x5 = np.eye(5)

    #print(a_1_5x5)

    with open("task_5_3.txt", "wb") as f:
        np.save( f, a_1_5x5)
