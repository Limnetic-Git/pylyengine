import raylib

class Inventory:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inventory = []
        for _ in range(width):
            self.inventory.append([{'item': None, 'count': 0}] * height)

    def __find_empty_slot(self):
        for y in range(self.width):
            for x in range(self.height):
                if not self.inventory[x][y]['item']:
                    return x, y
        return None, None


    def give(self, item, count=1):
        items_to_give_left = count
        for x in range(self.width):
            for y in range(self.height):
                item_in_slot = self.inventory[x][y]['item']
                item_count_in_slot = self.inventory[x][y]['count']
                if item_in_slot:
                    if item_in_slot.name == item.name and item_count_in_slot < item.stack:
                        for i in range(item.stack - item_count_in_slot):
                            item_count_in_slot += 1
                            items_to_give_left -= 1
        if items_to_give_left <= item.stack:
            empty_slot_x, empty_slot_y = self.__find_empty_slot()
            self.inventory[empty_slot_x][empty_slot_y] = {'item': item, 'count': items_to_give_left}
            items_to_give_left = 0
        elif items_to_give_left > item.stack:
            while items_to_give_left > 0:
                empty_slot_x, empty_slot_y = self.__find_empty_slot()
                if empty_slot_x == None: return False
                items_to_slot = (item.stack if items_to_give_left >= item.stack else items_to_give_left)
                self.inventory[empty_slot_x][empty_slot_y] = {'item': item, 'count': items_to_slot}
                items_to_give_left -= items_to_slot
        return True

