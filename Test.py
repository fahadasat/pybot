
import numpy as np

def sample_size(x):
    # Calculate the sample size
    n_x = np.size(x)
    # n_y = np.size(y)
    return (n_x)


def calc_mean(x):
    # Calculate the mean
    x_m = np.mean(x)
    # y_m = np.mean(y)
    return (x_m)


def main():
    # Main
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 5, 8, 13, 15, 18, 20, 21, 23])
    # Print the array
    print('x array: ', x)
    print('x array: ', y)

    # Print size of array
    n_x = sample_size(x)
    n_y = sample_size(y)
    print('x size ', n_x)
    print('y size ', n_y)

    # Print the mean
    x_m = calc_mean(x)
    y_m = calc_mean(y)
    print('x mean: ', x_m)
    print('y mean: ', y_m)


if __name__ == "__main__":
    main()