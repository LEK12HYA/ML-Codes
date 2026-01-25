import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

file_path = "Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name="IRCTC Stock Price")


def own_mean(values):
    if len(values) == 0:
        return np.nan
    return sum(values)/len(values)

def own_variance(values):
    if len(values) == 0:
        return np.nan
    mean_val = own_mean(values)
    return sum((v - mean_val)**2 for v in values)/len(values)

def avg_time(func, values, iterations=10):
    times = []
    for _ in range(iterations):
        start = time.time()
        func(values)
        end = time.time()
        times.append(end - start)
    return sum(times)/len(times)


price = df.iloc[:,3].values
day = df.iloc[:,2].values
month = df.iloc[:,1]
change = df.iloc[:,8].values


np_mean = np.mean(price)
man_mean = own_mean(price)

np_var = np.var(price)
man_var = own_variance(price)


numpy_time = avg_time(np.mean, price)
manual_time = avg_time(own_mean, price)


wed_price = price[day == "Wed"]
wed_mean = own_mean(wed_price)

april_price = price[month.astype(str).str.lower() == "april"]
april_mean = own_mean(april_price)



loss_prob = len([x for x in change if x < 0])/len(change)

wed_indices = [i for i, d in enumerate(day) if d == "Wed"]
profit_on_wed = len([i for i in wed_indices if change[i] > 0]) / len(wed_indices)
cond_prob = profit_on_wed  


print("Mean and Variance")
print("Population Mean (NumPy):", np_mean)
print("Custom Mean:", man_mean)
print("Population Variance (NumPy):", np_var)
print("Custom Variance:", man_var)

print("\nExecution Time")
print("NumPy Mean:", numpy_time)
print("Custom Mean:", manual_time)

print("\nCondition Means")
print("Wednesday Mean:", wed_mean)
print("April Mean:", april_mean)

print("\nProbabilities")
print("Probability of Loss:", loss_prob)
print("Probability of Profit on Wednesday:", profit_on_wed)
print("Conditional Probability of Profit on Wednesday:", cond_prob)


plt.scatter(day, change, color='blue', alpha=0.7)
plt.xlabel("Day of Week")
plt.ylabel("Change %")
plt.title("Stock Change % vs Day of Week")
plt.grid(True)
plt.show()
