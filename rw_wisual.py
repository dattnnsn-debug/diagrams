import matplotlib.pyplot as plt

from random_walk import RandomWalk
'''Створювати нові блукання, доки програма активна'''
while True:
    '''Створити випадкове блукання'''
    rw = RandomWalk()
    rw.fill_walk()
    '''Нанести на графік точки блукання'''
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Згенерувати випадкове блукання, y/n: ")
    if keep_running == 'n':
        break