import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://drive.google.com/file/d/1Zr0L15ebq8m2bnYuxaUZSXBaViK7ojjR/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
diamonds = pd.read_csv(url)
diamonds = pd.DataFrame(diamonds)
print(diamonds.head())
d_diamonds = diamonds[diamonds["Color"] == "D"]
d_diamonds = d_diamonds.reset_index(drop=True)
print(d_diamonds.head())

# Scatter Plots
sns.scatterplot(x=d_diamonds["Carat(Weight of Daimond)"],
                y=d_diamonds["Price(in US dollars)"], color="pink")
plt.show()

special = np.logical_and(
    d_diamonds["Cut(Quality)"] == "Ideal", d_diamonds["Clarity"] == "VS2")
sns.scatterplot(x=d_diamonds[special]["Carat(Weight of Daimond)"],
                y=d_diamonds[special]["Price(in US dollars)"], color="indianred", alpha=0.7)
plt.show()

# Count Plots
sns.countplot(x=diamonds["Cut(Quality)"])
plt.show()

sns.countplot(x="Cut(Quality)", data=diamonds)
plt.title("Another way(x=\"colname\", data=\"df\")")
plt.show()

sns.countplot(y=diamonds["Cut(Quality)"])
plt.show()

# using Hue Parameter
sns.countplot(x="Color", data=diamonds, hue="Cut(Quality)")
plt.show()

sns.countplot(x="Color", data=diamonds.sort_values("Color"), hue="Cut(Quality)",
                hue_order=["Ideal", "Premium", "Very Good", "Good", "Fair"],
              palette={"Ideal": "#aebfce", "Premium": "#aecec2",
                       "Very Good": "#ccceae", "Good": "#ceb7ae", "Fair": "#d19882"},
              saturation=1)
plt.show()

# Relational Plots ahead!
better_than_fair = diamonds[diamonds["Cut(Quality)"] != "Fair"]
special = np.logical_and(
    better_than_fair["Color"] == "D", better_than_fair["Clarity"] == "VS2")
sns.relplot(x="Carat(Weight of Daimond)", y="Price(in US dollars)",
            data=better_than_fair[special],
            row="Cut(Quality)", kind="scatter")
plt.show()

sns.relplot(x="Carat(Weight of Daimond)", y="Price(in US dollars)",
            data=better_than_fair[special],
            col="Cut(Quality)", kind="scatter")
plt.show()
#############################################
#############################################
d_e_ideal_premium = diamonds[np.logical_and(diamonds["Color"].isin(["D", "E"]),
                                            diamonds["Cut(Quality)"].isin(["Ideal", "Premium"]))]
print(set(d_e_ideal_premium["Color"]))
print(set(d_e_ideal_premium["Cut(Quality)"]))
# it is optional to determine the row and col order(not mandatory)
# relplot by deafult is a scatter plot
sns.relplot(x="Carat(Weight of Daimond)", y="Price(in US dollars)",
            data=d_e_ideal_premium, row="Color", row_order=["D", "E"],
            col="Cut(Quality)", col_order=["Ideal", "Premium"])
plt.show()


sns.relplot(x="Carat(Weight of Daimond)", y="Price(in US dollars)",
            data=d_e_ideal_premium, size="Depth", hue="Depth")
plt.title("Size in the Scatter", color="lightsteelblue")
plt.show()

# using style parameter

sns.relplot(x="Carat(Weight of Daimond)", y="Price(in US dollars)",
            data=d_e_ideal_premium[np.logical_and(d_e_ideal_premium["Clarity"].isin(
                ["VS1", "VS2", "VVS1", "VVS2", "IF"]),
                d_e_ideal_premium["Price(in US dollars)"] >= 10000)],
            style="Clarity", hue="Clarity", alpha=0.6)
plt.show()
# line plots
url_2 = "https://drive.google.com/file/d/17bHLeBl7cPFmuYwvwrgCaomglyFlAKae/view?usp=sharing"
url_2 = 'https://drive.google.com/uc?id=' + url_2.split('/')[-2]
climates = pd.read_csv(url_2)
climates = pd.DataFrame(climates)
# with confidece interval
sns.relplot(x="Month", y="Temp", data=climates, kind="line")
plt.show()
# with standard deviation
sns.relplot(x="Month", y="Temp", data=climates,
            kind="line", ci="sd", color="pink")
plt.show()
# normal line plot
url_3 = "https://drive.google.com/file/d/1FjfqZP3_Nuv5iGBv4LpCt8NgRtd6vCjq/view?usp=sharing"
url_3 = 'https://drive.google.com/uc?id=' + url_3.split('/')[-2]
mpg = pd.read_csv(url_3)
mpg = pd.DataFrame(mpg)
sns.relplot(x="model_year", y="horsepower", data=mpg, kind="line",
            ci=None, style="origin",
            hue="origin", dashes=False, markers=True)
plt.show()
corr_matrix = diamonds.corr()
print(corr_matrix)
sns.heatmap(corr_matrix, annot=True)
plt.show()
