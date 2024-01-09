def find_two_occurences(list):
    counts = {}

    for elem in list:
        counts[elem] = counts.get(elem, 0) + 1    # Get the current count, default = 0]

    for elem, count in counts:
        if count == 2:
            