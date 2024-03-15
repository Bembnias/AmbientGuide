from actual_dimensions import dimension

def estimate_distances(f, class_id, x0, y0):
    if class_id in (0, 9, 13, 39, 45):
        d = float(dimension(class_id, f, x0))
    else:
        d = float(dimension(class_id, f, y0))

    return d




