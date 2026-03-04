import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

experience = [1,2,3,4,5,6,7,8,9,10]

salary = [
    20000,25000,30000,35000,40000,
    45000,55000,60000,75000,80000
]

df = pd.DataFrame({
    "Experience": experience,
    "Salary": salary
})

print("Dataset:\n")
print(df)


x = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()


model.fit(x, y)

print("\nSlope:", model.coef_[0])
print("Intercept:", model.intercept_)

predicted_salary = model.predict(pd.DataFrame({"Experience":[5]}))

print("\nPredicted Salary for 5 Years Experience:", predicted_salary[0])

y_pred = model.predict(x)

plt.scatter(x, y)
plt.plot(x, y_pred)

plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Salary vs Experience (Linear Regression)")

plt.show()

counts, bins, patches = plt.hist(y_pred, bins=5, edgecolor="black")

colors = ["red","orange","green","purple","cyan"]

for patch, color in zip(patches, colors):
    patch.set_facecolor(color)

for i in range(len(counts)):
    plt.text(
        bins[i] + (bins[i+1]-bins[i])/2,
        counts[i],
        int(counts[i]),
        ha="center",
        va="bottom"
    )


plt.xlabel("Predicted Salary")
plt.ylabel("Number of Employees")
plt.title("Histogram of Predicted Salary Distribution")

plt.show()