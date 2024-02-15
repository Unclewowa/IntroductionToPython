import numpy as np

if __name__ == '__main__':

    a_05_5x5 = np.eye(5)*0.5
    #print(a_05_5x5)

    with open("task_5_4.txt", "wb") as f:
        np.save( f, a_05_5x5)

    #with open("task_5_4.txt","rb") as f:
    #    print(np.load(f))
