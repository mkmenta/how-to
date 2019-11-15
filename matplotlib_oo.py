import matplotlib.pyplot as plt  # We use pyplot to create the figure and let it manage the backend
import numpy as np

# Learnt from https://realpython.com/python-matplotlib-guide/

# Following the hierarchy:
# Let's create a figure
fig = plt.figure()
print(type(fig))

# Let's create one axes on it
ax = fig.subplots(nrows=1, ncols=1)
print(type(ax))

# Let's plot stuff in that axes
plot_a = 'scatter'
if plot_a == 'line':
    x = np.linspace(0, 100)
    lines = ax.plot(x, 2 * x)
    print(type(lines[0]))
    lines[0].set_color('red')
    ax.set_title('line')
elif plot_a == 'scatter':
    N = 100
    x = 0.9 * np.random.rand(N)
    y = 0.9 * np.random.rand(N)
    elements = ax.scatter(x, y)
    print(type(elements))
    elements.set_edgecolor('b')
else:
    raise Exception

# Let's show the figure
plt.show()  # Blocking by default and shows all the figures
