def AddListsUnique(list_1, list_2):
    for a in list_2:
        if a not in list_1:
            list_1.append(a)
    return list_1