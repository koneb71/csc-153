def remove_emptys(in_list):
    return filter(len, filter(None, in_list))