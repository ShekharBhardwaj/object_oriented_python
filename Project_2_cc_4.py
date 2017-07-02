def combiner(list_str_n_num):
    whole_str=""
    new_num=0
    for item in list_str_n_num:
        if isinstance(item, str):
            whole_str += item
        else:
            new_num += float(item)
    return whole_str + str(new_num)

print(combiner(["apple", 5.2, "dog", 8]))