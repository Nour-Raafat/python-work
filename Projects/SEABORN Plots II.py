import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url_3 = "https://drive.google.com/file/d/1FjfqZP3_Nuv5iGBv4LpCt8NgRtd6vCjq/view?usp=sharing"
url_3 = 'https://drive.google.com/uc?id=' + url_3.split('/')[-2]
mpg = pd.read_csv(url_3)
mpg = pd.DataFrame(mpg)

decade = ["70s" if i < 80 else "80s" for i in mpg["model_year"]]
mpg["decade"] = decade
print(mpg.head(10))
# countplots
sns.catplot(x="origin", data=mpg, kind="count")
plt.show()

sns.catplot(x="origin", data=mpg, kind="count",
            col="decade", palette=['slategrey', 'steelblue', 'lightsteelblue'])
plt.show()
# barplots
sns.catplot(x="decade", y="horsepower", data=mpg, kind="bar")
plt.show()

sns.catplot(x="decade", y="horsepower", data=mpg,
            kind="bar", order=["80s", "70s"], ci=None)
plt.show()
# boxplots
sns.catplot(x="decade", y="horsepower", data=mpg,
            kind="box", order=["80s", "70s"])
plt.show()

sns.catplot(x="decade", y="horsepower", data=mpg,
            kind="box", sym="", hue="origin")
plt.show()
# box extends to 2IQR
sns.catplot(x="decade", y="horsepower", data=mpg,
            kind="box", sym="", whis=2)
plt.show()
# box extends from 5th percentile to 95th percentile
sns.catplot(x="decade", y="horsepower", data=mpg,
            kind="box", sym="", whis=[5, 95])
plt.show()
# pointplots
sns.catplot(x="decade", y="horsepower", data=mpg, kind="point")
plt.show()

sns.catplot(x="decade", y="horsepower", data=mpg, kind="point", hue="origin",
            join=False, estimator=np.median, capsize=0.2)
plt.show()

sns.catplot(x="decade", y="horsepower", data=mpg, kind="point", hue="origin",
            join=False, estimator=np.median, ci=None)
plt.show()
# style
sns.set_style("whitegrid")
sns.set_palette("Reds")
sns.catplot(x="origin", data=mpg, kind="count")
plt.show()
# context can be paper, notebook, talk, poster
sns.set_context("poster")
sns.catplot(x="origin", data=mpg, kind="count")
plt.show()

sns.set_style("darkgrid")
sns.set_context("talk")
sns.set_palette(["indigo", "violet", "lightsteelblue"])
sns.catplot(x="origin", data=mpg, kind="count")
plt.show()

sns.set_style(None)
sns.set_context("notebook")
sns.set_palette("Blues")
sns.catplot(x="origin", data=mpg, kind="count")
plt.xticks(rotation=90)
plt.title("origin of cars".title(), fontsize="large", c="lightsteelblue")
plt.show()
