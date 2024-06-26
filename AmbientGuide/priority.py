def Priority(class_id):
    priority = {
        0: 4,
        1: 101,
        2: 101,
        3: 101,
        4: 1,
        5: 101,
        6: 101,
        7: 101,
        8: 1,
        9: 600,
        10: 17,
        11: 17,
        12: 17,
        13: 17,
        14: 1,
        15: 2,
        16: 2,
        17: 2,
        18: 2,
        19: 2,
        20: 2,
        21: 4,
        22: 2,
        23: 2,
        24: 13,
        25: 5,
        26: 13,
        27: 1,
        28: 1,
        29: 1,
        30: 13,
        31: 13,
        32: 13,
        33: 1,
        34: 13,
        35: 1,
        36: 13,
        37: 13,
        38: 13,
        39: 2,
        40: 2,
        41: 2,
        42: 2,
        43: 2,
        44: 2,
        45: 2,
        46: 1,
        47: 1,
        48: 1,
        49: 1,
        50: 1,
        51: 1,
        52: 1,
        53: 1,
        54: 1,
        55: 1,
        56: 17,
        57: 21,
        58: 2,
        59: 21,
        60: 21,
        61: 17,
        62: 17,
        63: 13,
        64: 1,
        65: 1,
        66: 1,
        67: 1,
        68: 13,
        69: 13,
        70: 5,
        71: 2,
        72: 21,
        73: 1,
        74: 1,
        75: 1,
        76: 2,
        77: 1,
        78: 1,
        79: 1
    }
    if class_id in priority:
        p = priority[class_id]
    else:
        p = 0
    return p