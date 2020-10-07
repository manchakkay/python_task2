import matplotlib.pyplot as plt
import numpy as np

def mark(arr, i, j, index):
    arr[i, j] = index
    for s in range(-1, 2, 2): 
        if(arr[i + s, j] == -1):
            mark(arr, i + s, j, index)
        if(arr[i, j + s] == -1):
            mark(arr, i, j + s, index)

def mark_array(arr):
    new_arr = np.copy(arr)

    index = 1
    new_arr[new_arr != 0] = -1
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if new_arr[i, j] == -1:
                mark(new_arr, i, j, index)
                index += 1
    return new_arr


if __name__ == "__main__":
    arr = np.zeros((20, 20), dtype='int8')

    arr[1:-1, -2] = 1

    arr[1, 1:5] = 1
    arr[1, 7:12] = 1
    arr[2, 1:3] = 1
    arr[2, 6:8] = 1
    arr[3:4, 1:7] = 1

    arr[7:11, 11] = 1
    arr[7:11, 14] = 1
    arr[10:15, 10:15] = 1

    arr[5:10, 5] = 1
    arr[5:10, 6] = 1

    new_arr = mark_array(arr)

    print("Labels - ", list(set(new_arr.ravel()))[1:])

    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.imshow(arr, cmap="Greys")
    plt.colorbar(ticks=arr.ravel())
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(new_arr, cmap="Greys")
    plt.colorbar(ticks=new_arr.ravel())
    plt.axis("off")
    plt.tight_layout()
    plt.show()