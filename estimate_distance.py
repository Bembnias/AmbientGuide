from actual_dimensions import dimension

def estimate_distances(f, class_id, x0, y0):
    if class_id in (0, 9, 13, 39, 45):
        d = dimension(class_id, f, x0)
    else:
        d = dimension(class_id, f, y0)

    print(d)




