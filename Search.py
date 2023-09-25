from abc import ABC, abstractmethod
import time
import random

"""Module with the base implementation of a Search class."""

class Search(ABC):
    """Abstract base class for searching."""

    def _init_(self, items):
        self._items = items

    @abstractmethod
    def _search(self):
        """Returns the index of the `item` contained
        in the `_items` property.
        Returns:
            int: Index of item
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        return self.time




import matplotlib.pyplot as plt



class BinarySearch:
    def __init__(self, data):
        self.data = data

    def _search(self, x):
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.data[mid] == x:
                return mid
            elif self.data[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def _time(self, x):
        import time
        start_time = time.time()
        self._search(x)
        return time.time() - start_time

if __name__ == '__main__':
    bin_t = []  # List to store the different amounts of time it took to do BinarySearch search (for different sizes)
    sizes = [10, 100, 500, 1000, 5000, 7500, 10000, 15000]  # Sizes for lists, up to 5000

    while True:  # Make sure the user gives the right input
        try:
            x = int(input('Enter a number to search for in the lists. If it is present, we will tell you the index at which it is found (starts at 0), else we will return -1.'))
            break
        except ValueError:
            print('Enter an integer input only!')

    for i in range(len(sizes)):
        # Creating random lists of the pre-defined sizes
        random_list = [random.randint(-1000, 1000) for _ in range(sizes[i])]
        


        bin = BinarySearch(sorted(random_list))
        search_bin = bin._search(x)
        time_bin = bin._time(x)
        bin_t.append(time_bin)

    plt.plot(sizes, bin_t, color='blue', label='BinarySearch timings')
    plt.xlabel('Sizes')
    plt.ylabel('Time')
    plt.title('Scatter Plot of Time taken to search vs. Size of list')
    plt.legend()
    plt.savefig('search_time.png')
    plt.show()
