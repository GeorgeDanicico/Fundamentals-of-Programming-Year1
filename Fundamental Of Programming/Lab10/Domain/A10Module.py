

class IterableDataStructure:
    def __init__(self):
        self._object_list = []

    def add(self, obj):
        self._object_list.append(obj)

    def __len__(self):
        return len(self._object_list)

    def __setitem__(self, item, value):
        self._object_list[item] = value

    def __getitem__(self, index):
        """
        we will get the item with the specified key
        :param index: the key we want to delete
        """
        return self._object_list[index]

    def __delitem__(self, item):
        """
        we delete a certain term in the dict using the unique key
        """
        self._object_list.remove(item)

    def __next__(self):
        if len(self._object_list) - 1 == self._position:
            raise StopIteration()

        self._position += 1
        return self._object_list[self._position]

    def __iter__(self):
        """
        we will keep in mind that the iterator starts at 0
        """
        self._position = -1
        return self


def FilterMethod(objects_list, filter_type):
    """
    we will filter the given object list accord to the filter_type function which is at the beginning considered an object
    :param objects_list: the list we want to filter
    :param filter_type: the filter function connection we will use to filter the list
    """

    return [item for item in objects_list if filter_type(item)]

    # filtered_list = IterableDataStructure()
    # for obj in objects_list:
    #     if filter_type(obj):
    #         filtered_list.add(obj)
    #
    # return filtered_list


def SortingMethod(objects_list, sort_type):
    """
    The sorting method I have chosen is the Comb Sort. Comb Sort is a modified bubble sort. In bubble sort the gap
    between the elements we compare will ways be 1. So here is the "optimisation of the comb sort. We take a "shrink
    factor" k which is generally 1.3 and we divide the actual length of the list by that k, and so the gap will be the
    integer obtained from the division, and we will do the same for loop as for the bubble sort, but the gap won't be
    1, but i + gap, where i is the current index of the for loop and gap is that number. After this step we will
    continue to divide the length by 1.3 until the gap is 1 or there hasn't been any modifications in the previous
    step.
    """
    length_of_object_list = len(objects_list)
    gap = length_of_object_list
    shrink_factor = 1.3
    sorted_done = False
    while not sorted_done:
        gap = gap / shrink_factor
        gap = int(gap)
        if gap <= 1:
            sorted_done = True
            gap = 1

        for index in range(length_of_object_list - gap):
            index_with_gap = gap + index
            if sort_type(objects_list[index], objects_list[index_with_gap]):
                objects_list[index], objects_list[index_with_gap] = objects_list[index_with_gap], objects_list[index]
                sorted_done = False

    return objects_list
