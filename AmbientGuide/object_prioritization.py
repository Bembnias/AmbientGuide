from priority import Priority

def object_prioritization(distance):
    main_priority = []
    for object in distance:
        for i in range(0, len(object), 4):
            row = []
            p = Priority(object[i])
            P = p / (object[1+i] * object[1+i])
            row.append(object[i])
            row.append(P)
            row.append(object[i+2])
            row.append(object[i+3])
            main_priority.append(row)
    main_priority = sorted(main_priority, key=lambda x: x[1], reverse=True)
    return main_priority