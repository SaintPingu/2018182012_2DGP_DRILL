objects = [[], [], []]

def add_object(obj, depth):
    objects[depth].append(obj)

def remove_object(obj):
    for layer in objects:
        if obj in layer:
            layer.remove(obj)
            del obj
            return

def all_objects():
    for layer in objects:
        for obj in layer:
            yield obj

def clear():
    for obj in all_objects():
        del obj
    
    for layer in objects:
        layer.clear()
    