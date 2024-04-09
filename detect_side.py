def detect_side(x1, x2, frame):
    x_center = (x1 + x2) / 2

    right = frame.shape[1] * 44/64
    left = frame.shape[1] * 20/64
    print(right)
    if x_center < left:
        side = 1
    elif x_center > right:
        side = 2
    else:
        side = 0
    return side