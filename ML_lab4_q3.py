import numpy as np
import matplotlib.pyplot as plt

def assign_train_class():
    np.random.seed(42)
    X = np.random.randint(1, 11, 20)
    Y = np.random.randint(1, 11, 20)

    labels = np.array([1 if x + y >= 9 else 0 for x, y in zip(X, Y)])

    plt.figure(figsize=(6, 6))
    for i in range(20):
        color = 'blue' if labels[i] == 0 else 'red'
        plt.scatter(X[i], Y[i], color=color)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Training Data")
    plt.grid(True)
    plt.show()

    return X, Y, labels

if __name__ == "__main__":
    assign_train_class()
