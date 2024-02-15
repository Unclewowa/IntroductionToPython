import numpy as np
import os

if __name__ == '__main__':
    a0_1 = np.zeros(10)
    b0_1 = np.zeros(55)
    #print(a0_1)
    #print(b0_1)

    a0_3x4 = np.zeros((3,4))
    #print(a0_3x4)

    a0_2x4x5 = np.zeros((2,4,5))
    #print(a0_2x4x5)

    filename = "task_5_1.txt"

    try:
        os.remove(filename)
    except OSError:
        pass

    with open(filename,'wb') as f:
        np.save(f, a0_1)
        np.save(f, b0_1)
        np.save(f, a0_3x4)
        np.save(f, a0_2x4x5)



