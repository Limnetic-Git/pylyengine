import raylib

def DrawTexture(texture, position, rotation, scale, tint=raylib.WHITE, 
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