from functions.polish_object import polish_object

def center_obiect(x1, x2, frame):
    x_center = (x1 + x2) / 2

    right = frame.shape[1] * 44/64
    left = frame.shape[1] * 20/64
    print(right)
    if x_center < left:
        side = "po lewej stronie"
    elif x_center > right:
        side = "po prawej stronie"
    else:
        side = "na środku"
    return side

def ivona(confidence, x1, x2, frame, object_name, engine):
    if confidence > 0.8:
        side = center_obiect(x1, x2, frame)
        object_name_pl = polish_object(object_name)
        object_name_with_side = f"{object_name_pl} {side}"

    elif confidence > 0.7:
        side = center_obiect(x1, x2, frame)
        object_name_pl = polish_object(object_name)
        object_name_with_side = f"Prawdopodobnie {object_name_pl} {side}"

    if confidence > 0.75:
        engine.say(object_name_with_side)
        engine.runAndWait()

def ivona_color(confidence, x1, x2, frame, object_name, engine, traffic_light_color):
    if confidence > 0.8:
        side = center_obiect(x1, x2, frame)
        object_name_pl = polish_object(object_name)
        object_name_with_side = f"{object_name_pl} {side}. Kolor światła {traffic_light_color}"

    elif confidence > 0.7:
        side = center_obiect(x1, x2, frame)
        object_name_pl = polish_object(object_name)
        object_name_with_side = f"Prawdopodobnie {object_name_pl} {side}. Kolor światła {traffic_light_color}"

    if confidence > 0.75:
        engine.say(object_name_with_side)
        engine.runAndWait()