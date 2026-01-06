'''Число, піднесене до степеня три - це його куб. Зробіть візуальне представлення для перших п'яти
кубів, а тоді для перших 5000 кубів.'''

import matplotlib.pyplot as plt

x_values = range(1, 6) #Створюємо діапазон
y_values = [x**3 for x in x_values] #Рахуємо куби діапазону

plt.style.use('seaborn-v0_8') #Додаємо стиль діаграми
fig, ax = plt.subplots() #Генеруємо функцією діаграму
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, s=100)

'''Задати назву для графіка та кожної з осей.'''
ax.set_title("Cube Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

'''Задати розмір шрифта для підписів на розмітці.'''
ax.tick_params(axis='both', which='major', labelsize=14)

'''Задати діапазон для кожної з осей.'''
ax.axis([0, 6, 0, 150])

'''Автоматичне збререження діаграми'''

plt.show()