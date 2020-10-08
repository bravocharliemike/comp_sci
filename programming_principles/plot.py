from random_walk import RandomWalk
import matplotlib.pyplot as plt

# Make a random walk
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=15)
    plt.show()  # run the plot

    # keep running?
    keep_going = input('Make another walk? (y/n): ')
    if keep_going == 'n':
        break   # get out of loop
