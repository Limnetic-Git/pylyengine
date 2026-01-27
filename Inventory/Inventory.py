import raylib

class Inventory:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inventory = []
        self.null_slot = {'item': None, 'count': 0}
        for x in range(width):
            column = []
            for y in range(height):
                column.append(self.null_slot)
            self.inventory.append(column)

    def add_slotsline(self, index=0):
        self.height += 1
        for y in range(self.width):
            self.inventory[y].insert(index, self.null_slot)

    def del_slotsline(self, index=0):
        self.height -= 1
        for y in range(self.width):
            self.inventory[y].pop(index)


    def __find_empty_slot(self):
        for x in range(self.width):
            for y in range(self.height):
                if not self.inventory[x][y]['item']:
                    return x, y
        return None, None

    def give(self, item, count=1):
        items_to_give_left = count
        for x in range(self.width):
            for y in range(self.height):
                slot = self.inventory[x][y]
                if (slot['item'] and
                    slot['item'].name == item.name and
                    slot['count'] < item.stack):

                    available_space = item.stack - slot['count']
                    to_add = min(available_space, items_to_give_left)

                    if to_add > 0:
                        slot['count'] += to_add
                        items_to_give_left -= to_add

                        if items_to_give_left == 0:
                            return True
        while items_to_give_left > 0:
            empty_slot_x, empty_slot_y = self.__find_empty_slot()
            if empty_slot_x is None:
                return False
            to_add = min(item.stack, items_to_give_left)
            self.inventory[empty_slot_x][empty_slot_y] = {
                'item': item,
                'count': to_add
            }
            items_to_give_left -= to_add

        return True
