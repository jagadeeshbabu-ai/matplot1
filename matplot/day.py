# import pandas as pd
# print(pd.__version__)

import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 15, 30]

# plt.plot(x, y)
# plt.show()

# ax.plot([1, 2, 3], [10, 20, 15])

# plt.figure(figsize=(8, 5))

# plt.plot([1, 2, 3, 4], [10, 20, 15, 30])

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 140, 180, 210]

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Slaes ($Doller)")

# plt.plot(months, sales)
# plt.plot(months, sales)

# plt.xticks(rotation=45)
plt.plot(
    months,
    sales,
    linewidth=2,
    alpha=0.7
)

plt.show()

# plt.show()


# plt.show()

