# sample of pagination
def pagination(items, quantity_items_on_page, number_page):
    current_items = items[(number_page - 1) * quantity_items_on_page :
                    number_page * quantity_items_on_page]
    return current_items


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list of items
print(pagination(items, 2, 1))
print(pagination(items, 2, 2))
print(pagination(items, 2, 3))
print(pagination(items, 2, 4))
print(pagination(items, 2, 5))