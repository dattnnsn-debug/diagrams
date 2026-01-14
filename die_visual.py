from die import Die

'''Створити D6'''
die = Die()

'''Зробити декілька кидів і зберегти результати у список.'''
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

'''Проаналізувати результати'''
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)