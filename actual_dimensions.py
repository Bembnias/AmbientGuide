def dimension(class_id, f, P):
    dimension = {
        0: 0.55,
        1: 0.95,
        2: 1.6,
        3: 1,
        4: 19.4,
        5: 3.5,
        6: 3.5,
        7: 3.5,
        8: 2,
        9: 0.3,
        10: 0.7,
        11: 0.4,
        12: 1.80,
        13: 2.2,
        14: 0.25,
        15: 0.24,
        16: 0.6,
        17: 2,
        18: 0.7,
        19: 1.6,
        20: 3,
        21: 1.5,
        22: 1.8,
        23: 5.7,
        24: 0.5,
        25: 0.7,
        26: 0.3,
        27: 0.4,
        28: 0.8,
        29: 0.26,
        30: 1.8,
        31: 1.5,
        32: 0.25,
        33: 0.5,
        34: 1.06,
        35: 0.20,
        36: 0.6,
        37: 1.6,
        38: 0.65,
        39: 0.09,
        40: 0.15,
        41: 0.1,
        42: 0.16,
        43: 0.19,
        44: 0.19,
        45: 0.17,
        46: 0.2,
        47: 0.1,
        48: 0.08,
        49: 0.1,
        50: 0.15,
        51: 0.2,
        52: 0.2,
        53: 0.4,
        54: 0.1,
        55: 0.1,
        56: 0.95,
        57: 0.95,
        58: 0.5,
        59: 0.35,
        60: 0.75,
        61: 0.4,
        62: 1.12,
        63: 0.36,
        64: 0.13,
        65: 0.17,
        66: 0.17,
        67: 0.16,
        68: 0.6,
        69: 0.6,
        70: 0.3,
        71: 0.5,
        72: 1.9,
        73: 0.2,
        74: 0.25,
        75: 0.3,
        76: 0.15,
        77: 0.2,
        78: 0.3,
        79: 0.17
    }
    if class_id in dimension:
        D= dimension[class_id]
        d = (f * D) / P
        return f"{d}"
    else:
        return 9999999;