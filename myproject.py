import pandas as pd
import matplotlib.pyplot as plt
import os

filename = input("Enter your data source:")
f = pd.read_csv(filename,  sep="\\s+",header=0)

f = pd.read_csv(filename,  sep="\\s+",header=0)
print('Data info',f.info())
print('Statistical information',f.describe())

df = pd.DataFrame(f)
print(df)

# Determine correlation matrix

print(df.corr())



# plotting graphs

os.makedirs('plots', exist_ok=True)

plt.plot(df['CRIM'], color='red')
plt.title('Per capita Crime by Population status')
plt.xlabel('Population Status')
plt.ylabel('Crime per capita')
plt.savefig(f'plots/Crime_per_capita.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(df['RM'], bins=3, color='g')
plt.title('Average number of rooms per dwelling ')
plt.xlabel('Rooms')
plt.ylabel('Count')
plt.savefig(f'plots/rooms_dwelling.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(df['B'], df['MEDV'], color='b')
plt.title('Relation between black population and housing price')
plt.xlabel('Black population')
plt.ylabel('Median housing price')
plt.savefig(f'plots/black_housing.png', format='png')

plt.close()