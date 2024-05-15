def oxford_comma(items):
    # If there's only one item, return it
    if len(items) == 1:
        return items[0]
    # If there are two items, join them with "and"
    elif len(items) == 2:
        return " and ".join(items)
    # If there are more than two items, join all but the last with commas, and append "and" before the last
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]


print(oxford_comma(["kiwi"]))
print(oxford_comma(["kiwi", "durian", "starfruit"]))

