def f(*args, **kwargs):
    print("Positional: ", kwargs)


f(galleons=100, sickels=50, knuts=25, pennies=5)