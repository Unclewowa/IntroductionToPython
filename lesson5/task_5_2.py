import numpy as np
import os

if __name__ == '__main__':
    a1_1 = np.ones(10)
    b1_1 = np.ones(55)
    #print(a1_1)
    #print(b1_1)

    a1_3x4 = np.ones((3,4))
    #print(a1_3x4)

    a1_2x4x5 = np.ones((2,4,5))
    #print(a1_2x4x5)

    filename = "task_5_2.txt"

    try:
        os.remove(filename)
    except OSError:
        pass

    with open(filename,'wb') as f:
        np.save(f, a1_1)
        np.save(f, b1_1)
        np.save(f, a1_3x4)
        np.save(f, a1_2x4x5)
