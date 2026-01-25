from UI.UI_Elements.Texture import *
from UI.UI_Elements.Text import *
import raylib

class Slotlist:
    def __init__(self, ui_layer, array, rel_x, rel_y, slot_size, distance_between=5):
        self.array = array
        self.ui_layer = ui_layer
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = slot_size / 1920
        self.rel_height = slot_size / 1080
        self.distance_between = distance_between
        self.item_buffer = {'item': None, 'count': 0, 'parent_slot': [-1, -1]}  # Используем -1 для обозначения отсутствия
        self.selected_slot = [0, 0]

    def update_position(self):
        window = self.ui_layer.parent_scene.window
        self.x = int(window.width * self.rel_x)
        self.y = int(window.height * self.rel_y)
        self.width = int(window.width * self.rel_width)
        self.height = int(window.height * self.rel_height)

    def delete_items_from_slot(self, slot, count):
        self.array[slot[0]][slot[1]]['count'] -= count
        if self.array[slot[0]][slot[1]]['count'] <= 0:
            self.array[slot[0]][slot[1]] = {'item': None, 'count': 0}

    def transfer(self, target_slot_coor):
        target_slot = self.array[target_slot_coor[0]][target_slot_coor[1]]

        # Если целевой слот - исходный слот буфера (возвращаем обратно)
        if target_slot_coor == self.item_buffer['parent_slot']:
            # Просто очищаем буфер, предметы уже в слоте
            self.item_buffer = {'item': None, 'count': 0, 'parent_slot': [-1, -1]}
            return

        # Если целевой слот пустой
        if not target_slot['item']:
            # Перемещаем весь буфер в целевой слот
            self.array[target_slot_coor[0]][target_slot_coor[1]] = {
                'item': self.item_buffer['item'],
                'count': self.item_buffer['count']
            }

            # Удаляем предметы из исходного слота
            if self.item_buffer['parent_slot'] != [-1, -1]:
                self.delete_items_from_slot(self.item_buffer['parent_slot'], self.item_buffer['count'])

            self.item_buffer = {'item': None, 'count': 0, 'parent_slot': [-1, -1]}

        # Если в целевом слоте тот же предмет
        elif target_slot['item'] == self.item_buffer['item']:
            # Вычисляем сколько можно переложить
            available_space = target_slot['item'].stack - target_slot['count']

            if available_space > 0:
                # Перекладываем сколько возможно
                amount_to_transfer = min(self.item_buffer['count'], available_space)

                # Добавляем в целевой слот
                target_slot['count'] += amount_to_transfer

                # Удаляем из исходного слота
                if self.item_buffer['parent_slot'] != [-1, -1]:
                    self.delete_items_from_slot(self.item_buffer['parent_slot'], amount_to_transfer)

                # Обновляем буфер
                self.item_buffer['count'] -= amount_to_transfer

                # Если буфер пуст
                if self.item_buffer['count'] <= 0:
                    self.item_buffer = {'item': None, 'count': 0, 'parent_slot': [-1, -1]}

    def update(self):
        window = self.ui_layer.parent_scene.window
        self.update_position()

        for x in range(len(self.array)):
            for y in range(len(self.array[x])):
                render_mode = 'default'
                slot_x = self.x + x * (self.width + self.distance_between)
                slot_y = self.y + y * (self.height + self.distance_between)

                # Проверка наведения мыши
                mouse_over = (window.mouse_x >= slot_x and window.mouse_x <= slot_x + self.width and
                             window.mouse_y >= slot_y and window.mouse_y <= slot_y + self.height)

                if mouse_over:
                    render_mode = "hover"

                    # ЛКМ - взять/переложить предмет
                    if raylib.IsMouseButtonReleased(0):
                        self.selected_slot = [x, y]

                        # Если буфер пустой и в слоте есть предмет - берем 1 предмет
                        if not self.item_buffer['item'] and self.array[x][y]['item']:
                            if self.array[x][y]['count'] > 0:
                                self.item_buffer = {
                                    'item': self.array[x][y]['item'],
                                    'count': 1,
                                    'parent_slot': [x, y],
                                }
                        # Если в буфере есть предмет - перекладываем
                        elif self.item_buffer['item']:
                            self.transfer(self.selected_slot)

                    # ПКМ - взять весь стек
                    elif raylib.IsMouseButtonReleased(1) and self.array[x][y]['item']:
                        self.selected_slot = [x, y]

                        # Если буфер пустой - берем весь стек
                        if not self.item_buffer['item']:
                            self.item_buffer = {
                                'item': self.array[x][y]['item'],
                                'count': self.array[x][y]['count'],
                                'parent_slot': [x, y],
                            }
                        # Если в буфере есть предмет - пробуем объединить
                        elif self.item_buffer['item']:
                            self.transfer(self.selected_slot)

                    # Средняя кнопка - взять половину
                    elif raylib.IsMouseButtonReleased(2) and self.array[x][y]['item']:
                        self.selected_slot = [x, y]

                        if not self.item_buffer['item'] and self.array[x][y]['count'] > 1:
                            half_count = self.array[x][y]['count'] // 2
                            if half_count > 0:
                                self.item_buffer = {
                                    'item': self.array[x][y]['item'],
                                    'count': half_count,
                                    'parent_slot': [x, y],
                                }

                if [x, y] == self.selected_slot:
                    render_mode = "selected"

                # Отрисовка слота
                raylib.DrawRectangleRounded(
                    [slot_x, slot_y, self.width, self.height],
                    self.ui_layer.ui_theme['Slotlist']['roundness'],
                    self.ui_layer.ui_theme['Slotlist']['segments'],
                    self.ui_layer.ui_theme['Slotlist'][render_mode]['main_color'],
                )

                raylib.DrawRectangleRoundedLinesEx(
                    [slot_x, slot_y, self.width, self.height],
                    self.ui_layer.ui_theme['Slotlist']['roundness'],
                    self.ui_layer.ui_theme['Slotlist']['segments'],
                    self.ui_layer.ui_theme['Slotlist'][render_mode]['outline_width'],
                    self.ui_layer.ui_theme['Slotlist'][render_mode]['outline_color'],
                )

                # Отрисовка предмета в слоте
                slot_item = self.array[x][y]
                if slot_item['item'] and slot_item['count'] > 0:
                    # Проверяем, взяты ли предметы из этого слота
                    items_in_slot = slot_item['count']

                    # Если это родительский слот буфера и предмет тот же
                    if (self.item_buffer['parent_slot'] == [x, y] and
                        self.item_buffer['item'] == slot_item['item']):
                        items_in_slot -= self.item_buffer['count']

                    # Если в слоте еще остались предметы
                    if items_in_slot > 0:
                        texture_element_x = slot_x / window.width + (3 / 1920)
                        texture_element_y = slot_y / window.height + (3 / 1080)
                        texture_element_width = self.rel_width - (6 / 1920)
                        texture_element_height = self.rel_height - (6 / 1080)

                        texture_element = Texture(
                            self.ui_layer,
                            texture_element_x,
                            texture_element_y,
                            texture_element_width,
                            texture_element_height,
                            slot_item['item'].texture_name,
                            raylib.WHITE,
                        )

                        text_element = Text(
                            self.ui_layer,
                            texture_element_x - texture_element_width + 0.015,
                            texture_element_y + 0.01,
                            0.075,
                            0.075,
                            str(items_in_slot),
                            raylib.RAYWHITE,
                        )

                        texture_element.update()
                        text_element.update()

        # Отрисовка предмета в буфере (на курсоре)
        if self.item_buffer['item'] and self.item_buffer['count'] > 0:
            item_texture_x = window.mouse_x / window.width
            item_texture_y = window.mouse_y / window.height

            item_texture = Texture(
                self.ui_layer,
                item_texture_x,
                item_texture_y,
                self.rel_width,
                self.rel_height,
                self.item_buffer['item'].texture_name,
                raylib.WHITE,
            )
            item_texture.update()

            item_text = Text(
                self.ui_layer,
                item_texture_x - self.rel_width + 0.0165,
                item_texture_y + 0.0127,
                0.075,
                0.075,
                str(self.item_buffer['count']),
                raylib.RAYWHITE,
            )
            item_text.update()
