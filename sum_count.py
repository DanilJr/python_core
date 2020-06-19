def count_positives_sum_negatives(arr):
    if arr==[]:
        return []
    else:
        return [len(list((filter(lambda x: x>0, arr)))), sum(filter(lambda x: x<0, arr))]