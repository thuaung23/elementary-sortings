# This program uses elementary sorts, such as selection, insertion and bubble.
# This program is written in object oriented programming.
# Written by: Thu Aung
# Written on: Oct 11,2020

"""
These elementary sorting algorithms are good for only smaller input sizes
because the time complexity of them is quadratic, O(N^2).
"""

class Sorting:
    def __init__(self, item):
        self.item = item

    def select_sort(self):
        for i in range(len(self.item)):
            # Create minimum for comparison.
            i_min = i
            for j in range(i+1, len(self.item)):
                if self.item[j] < self.item[i_min]:
                    # If condition is met, minimum is assigned to lesser item.
                    i_min = j
            # Swap positions.
            self.item[i], self.item[i_min] = self.item[i_min], self.item[i]
        return self.item

    def insert_sort(self):
        # Item at index[0] is considered as sorted.
        for i in range(1, len(self.item)):
            # Hold the value of item at index[i] in a variable, key.
            key = self.item[i]
            # To compare value of item/items (located before index[i]) with key.
            j = i-1
            while j>=0 and key < self.item[j]:
                # If conditions met, move item to the right.
                self.item[j+1] = self.item[j]
                # This is to continue moving until one of conditions is false.
                j-=1
            # After breaking out of loop, the next item after sorted items becomes key.
            self.item[j+1] = key
        return self.item

    def bubble_sort(self):
        # Scan the whole list.
        for i in range(len(self.item)-1):
            # A counter to break out of loop if already sorted.
            no_swap = 0
            # After first pass, last item reached to last index. Thus, for second pass, scan up to n-2 and so on.
            for j in range(len(self.item)-i-1):
                if self.item[j] > self.item[j+1]:
                    # Swap items if condition is true.
                    self.item[j], self.item[j+1] = self.item[j+1], self.item[j]
                    no_swap += 1
            if no_swap == 0:
                break
        return self.item

# Example Usage
arr_1 = [2,6,8,4,9,2,1,4,3,6,9,7,5,1,2,3]
sorted_arr1 = Sorting(arr_1)
print("Unsorted: ", arr_1)
print("Selection Sort: ", sorted_arr1.select_sort())
print("Bubble Sort: ", sorted_arr1.bubble_sort())
print("Insertion Sort: ", sorted_arr1.insert_sort())