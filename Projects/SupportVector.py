import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, roc_curve
from sklearn.model_selection import StratifiedKFold
plt.style.use('bmh')
##################################################
banknote = pd.read_csv(
    "http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt", header=None)
banknote.columns = ["first feature", "second feature",
                    "third feature", "fourth feature", "OUTPUT"]
banknote = pd.DataFrame(banknote)
banknote_normalized = pd.DataFrame(
    (banknote - banknote.mean()) / banknote.std())
banknote_normalized["OUTPUT"] = banknote["OUTPUT"]
##################################################
##################################################
# HARD MARGIN Support Vector Machine implementation
##################################################
##################################################
y = np.array(banknote_normalized.OUTPUT)
X = (banknote_normalized.drop(["OUTPUT"], axis="columns")).values
folds = StratifiedKFold(n_splits=5)
accuracies = []
sensitivities = []
false_alarm_rates = []
specifities = []
precisions = []
print("*"*25)
print("***HARD MARGIN RESULTS***")
print("*"*25)
for train_index, test_index in folds.split(X, y):
    x_train, x_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
    model = SVC()
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)
    hard_margin_matrix = confusion_matrix(y_test, y_predict)
    print("*"*25)
    print(hard_margin_matrix)
    true_positive = hard_margin_matrix[0, 0]
    false_negative = hard_margin_matrix[0, 1]
    false_positive = hard_margin_matrix[1, 0]
    true_negative = hard_margin_matrix[1, 1]
    print("accuracy equals " + str((true_positive + true_negative) / len(y_predict)))
    accuracies.append((true_positive + true_negative) / len(y_predict))
    print("sensitivity equals " +
          str(true_positive / (true_positive + false_negative)))
    sensitivities.append(true_positive / (true_positive + false_negative))
    print("false alarm rate equals " +
          str(false_positive / (false_positive + true_negative)))
    false_alarm_rates.append(false_positive / (false_positive + true_negative))
    print("specifity equals " + str(true_negative /
          (true_negative + false_positive)))
    specifities.append(true_negative /
                       (true_negative + false_positive))
    print("precision equals " + str(true_positive /
          (true_positive + false_positive)))
    precisions.append(true_positive / (true_positive + false_positive))
print("*"*25)
print("AFTER 5 CROSS FOLD VALIDATIONS")
print("average accuracy is " + str(np.mean(accuracies)))
print("average sensitivity is " + str(np.mean(sensitivities)))
print("average false alarm rate is " + str(np.mean(false_alarm_rates)))
print("average specifity is " + str(np.mean(specifities)))
print("average precision is " + str(np.mean(precisions)))

fpr, tpr, thresholds = roc_curve(y_test, y_predict, pos_label=0)
plt.plot(1-fpr, 1-tpr, label="HARD MARGIN")
##################################################
##################################################
# SOFT MARGIN Support Vector Machine implementation
##################################################
##################################################
y = np.array(banknote_normalized.OUTPUT)
X = (banknote_normalized.drop(["OUTPUT"], axis="columns")).values
folds = StratifiedKFold(n_splits=5)
accuracies = []
sensitivities = []
false_alarm_rates = []
specifities = []
precisions = []
print("*"*25)
print("***SOFT MARGIN RESULTS***")
print("*"*25)
for train_index, test_index in folds.split(X, y):
    x_train, x_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
    model = SVC(C=0.01)
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)
    soft_margin_matrix = confusion_matrix(y_test, y_predict)
    print("*"*25)
    print(soft_margin_matrix)
    true_positive = soft_margin_matrix[0, 0]
    false_negative = soft_margin_matrix[0, 1]
    false_positive = soft_margin_matrix[1, 0]
    true_negative = soft_margin_matrix[1, 1]
    print("accuracy equals " + str((true_positive + true_negative) / len(y_predict)))
    accuracies.append((true_positive + true_negative) / len(y_predict))
    print("sensitivity equals " +
          str(true_positive / (true_positive + false_negative)))
    sensitivities.append(true_positive / (true_positive + false_negative))
    print("false alarm rate equals " +
          str(false_positive / (false_positive + true_negative)))
    false_alarm_rates.append(false_positive / (false_positive + true_negative))
    print("specifity equals " + str(true_negative /
          (true_negative + false_positive)))
    specifities.append(true_negative /
                       (true_negative + false_positive))
    print("precision equals " + str(true_positive /
          (true_positive + false_positive)))
    precisions.append(true_positive / (true_positive + false_positive))
print("*"*25)
print("AFTER 5 CROSS FOLD VALIDATIONS")
print("average accuracy is " + str(np.mean(accuracies)))
print("average sensitivity is " + str(np.mean(sensitivities)))
print("average false alarm rate is " + str(np.mean(false_alarm_rates)))
print("average specifity is " + str(np.mean(specifities)))
print("average precision is " + str(np.mean(precisions)))

fpr, tpr, thresholds = roc_curve(y_test, y_predict, pos_label=0)
plt.plot(1-fpr, 1-tpr, label="SOFT MARGIN")
##################################################
plt.xlabel("False Positive Rate", fontweight="bold")
plt.ylabel("True Positive Rate", fontweight="bold")
plt.title("ROC Curve to compare between Hard and Soft Margin SVM",
          fontweight="bold")
plt.legend(fontsize="large")
plt.show()
##################################################
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(banknote_normalized[banknote_normalized["OUTPUT"] == 0]["first feature"],
             banknote_normalized[banknote_normalized["OUTPUT"]
                                 == 0]["second feature"],
             banknote_normalized[banknote_normalized["OUTPUT"]
                                 == 0]["third feature"],
             color="pink", alpha=0.8, label="0 Classification")
ax.scatter3D(banknote_normalized[banknote_normalized["OUTPUT"] == 1]["first feature"],
             banknote_normalized[banknote_normalized["OUTPUT"]
                                 == 1]["second feature"],
             banknote_normalized[banknote_normalized["OUTPUT"]
                                 == 1]["third feature"],
             color="lightsteelblue", alpha=0.8, label="1 Classification")
plt.legend(fontsize="large")
plt.show()
