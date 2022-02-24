import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

###############################################################################################


def update_weights(weights: list, learning_rate: float, dataset: DataFrame):
    new_weights = []
    for i in range(6):
        weight_batch = []
        for j in range(len(dataset)):
            weight_batch.append(
                learning_rate * dataset.iloc[j, i] * (dataset.iloc[j, 6] - dataset.iloc[j, 7]))
        new_weights.append(weights[i] + np.mean(weight_batch))
    return new_weights


def update_bias(bias: float, learning_rate: float, dataset: DataFrame):
    bias_batch = []
    for i in range(len(dataset)):
        bias_batch.append(
            learning_rate * (dataset.iloc[i, 6] - dataset.iloc[i, 7]))
    bias = bias + np.mean(bias_batch)
    return bias


def predict(weights: list, bias: float, dataset: DataFrame):
    predictions = []
    for i in range(len(dataset)):
        summation = 0
        for j in range(6):
            summation += (weights[j] * dataset.iloc[i, j])
        summation += bias
        predictions.append(summation)
    return predictions
###############################################################################################


url = 'https://drive.google.com/uc?id=' + \
    "https://drive.google.com/file/d/1piOi9sTVWseRvRaSBymmPto0kRp1jRC7/view?usp=sharing".split(
        '/')[-2]
weathers = pd.read_csv(url)
weathers = weathers.drop(["Formatted Date", "Summary",
                          "Precip Type", "Loud Cover", "Daily Summary"], axis=1)
weathers_70_percent = weathers[:(len(weathers) * 70 // 100)]
weathers_30_percent = weathers[(len(weathers) * 70 // 100):]
weathers_30_percent = pd.DataFrame(weathers_30_percent.reset_index(drop=True))
weathers_70_percent = pd.DataFrame(weathers_70_percent.reset_index(drop=True))
weathers_70_percent["TARGET Humidity"] = weathers_70_percent["Humidity"]
weathers_70_percent = weathers_70_percent.drop("Humidity", axis=1)
weathers_30_percent["TARGET Humidity"] = weathers_30_percent["Humidity"]
weathers_30_percent = weathers_30_percent.drop("Humidity", axis=1)
###############################################################################################
weights_list = [np.random.random() for i in range(6)]
bias = 0.5
mean_squared_error = []
###############################################################################################
training_data = pd.DataFrame(
    (weathers_70_percent - weathers_70_percent.mean()) / weathers_70_percent.std())
training_data["TARGET Humidity"] = weathers_70_percent["TARGET Humidity"]
testing_data = pd.DataFrame(
    (weathers_30_percent - weathers_30_percent.mean()) / weathers_30_percent.std())
testing_data["TARGET Humidity"] = weathers_30_percent["TARGET Humidity"]
###############################################################################################

training_data["PREDICTION Humidity"] = predict(
    weights_list, bias, training_data)
for epoch in range(1, 51):
    print("THIS IS EPOCH NUMBER " + str(epoch))
    weights_list = update_weights(weights_list, 0.0108, training_data)
    bias = update_bias(bias, 0.0108, training_data)
    testing_data["PREDICTION Humidity"] = predict(
        weights_list, bias, testing_data)
    testing_data["Squared Error"] = (testing_data["TARGET Humidity"] -
                                     testing_data["PREDICTION Humidity"])**2
    mean_squared_error.append(np.mean(testing_data["Squared Error"]))
print(mean_squared_error)
fig, ax = plt.subplots()
epochs = [i for i in range(1, 51)]
ax.plot(epochs, mean_squared_error)
ax.set_xlabel("Epoch Number", fontweight="bold")
ax.set_ylabel("MSE", fontweight="bold")
ax.set_title("Change in MSE over a number of Epochs", fontweight="bold")
plt.show()
