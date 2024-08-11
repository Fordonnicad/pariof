def my_generator():
    yield [12, 25, 0.0016136538582380293]

# Create an instance of the generator
generator = my_generator()

# Iterate over the values yielded by the generator
for value in generator:
    print(value)
