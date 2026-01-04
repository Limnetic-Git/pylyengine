import raylib

def DrawTextureRaw(texture, position, rotation, scale, tint=raylib.WHITE,
                            flip_x=False, flip_y=False, origin=None):
    """
    Рисует текстуру с поддержкой отражения.
    Args:
        texture: Текстура для отрисовки
        position: Позиция (x, y)
        rotation: Угол вращения в градусах
        scale: Масштаб (может быть числом или (scale_x, scale_y))
        tint: Цвет оттенка
        flip_x: Отражение по горизонтали
        flip_y: Отражение по вертикали
        origin: Точка вращения (если None - центр)
    """
    if isinstance(scale, (tuple, list)):
        scale_x, scale_y = scale
    else:
        scale_x = scale_y = scale
    
    src_rect = [
        0,
        0,
        -texture.width if flip_x else texture.width,
        -texture.height if flip_y else texture.height
    ]

    dest_width = texture.width * scale_x
    dest_height = texture.height * scale_y
    x, y = position
    
    dest_rect = [x, y, dest_width, dest_height]
    if origin is None:
        origin = (dest_width / 2, dest_height / 2)

    raylib.DrawTexturePro(texture, src_rect, dest_rect, origin, rotation, tint)

def DrawTexture(texture, position, rotation, scale, window, camera, tint=raylib.WHITE,
                            flip_x=False, flip_y=False, origin=None):


    screen_width = window.width
    screen_height = window.height

    x, y = position
    scale_x, scale_y = scale

    texture_width = texture.width * abs(scale_x) * camera.zoom_x
    texture_height = texture.height * abs(scale_y) * camera.zoom_y

    world_x = x * camera.zoom_x + camera.x
    world_y = y * camera.zoom_y + camera.y

    if origin:
        origin_x = origin[0] * scale_x * camera.zoom_x
        origin_y = origin[1] * scale_y * camera.zoom_y
    else:
        origin_x = texture_width / 2
        origin_y = texture_height / 2

    obj_left = world_x - origin_x
    obj_top = world_y - origin_y
    obj_right = obj_left + texture_width
    obj_bottom = obj_top + texture_height

    screen_left = 0
    screen_top = 0
    screen_right = screen_width
    screen_bottom = screen_height

    if (obj_right < screen_left or
        obj_left > screen_right or
        obj_bottom < screen_top or
        obj_top > screen_bottom):
        return

    DrawTextureRaw(
        texture=texture,
        position=(world_x, world_y),
        rotation=rotation,
        scale=(scale_x * camera.zoom_x,
            scale_y * camera.zoom_y),
        origin=origin,
        tint=tint,
        flip_x=flip_x,
        flip_y=flip_y,
    )
    window.debug_monitor.drawing_objects_count += 1
