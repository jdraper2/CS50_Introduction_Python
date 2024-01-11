class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * int(self.size)

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Not enough space.")
        self.size = self.size + n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("Not enough cookies.")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    #Setter - capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cant be negative")
        self._capacity = capacity


    @property
    def size(self):
        return self._size

    #Setter - capacity
    @size.setter
    def size(self, size):
        self._size = size


def main():

    my_jar = Jar()

    my_jar.deposit(4)
    my_jar.deposit(4)
    my_jar.withdraw(6)

    print(my_jar)


if __name__ == "__main__":
    main()
