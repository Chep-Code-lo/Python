def filter_speeds(speeds, min_value):
    values = []
    indices = []
    for i, v in enumerate(speeds):
        if v < min_value:
            values.append(v)
            indices.append(i)
    return values, indices

    