def increasing_or_decreasing(seq):
    lst = seq[1:]
    
    is_increasing = all([lst[lst_index] > seq[lst_index] for lst_index in range(len(lst))])
    is_decreasing = all([lst[lst_index] < seq[lst_index] for lst_index in range(len(lst))])


    if is_increasing:
        return "Up"
    if is_decreasing:
        return "Down"
    return False