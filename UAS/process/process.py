class Process:
    def __init__(self, data, view):
        self.data = data
        self.view = view

    def add_item(self):
        name = self.view.get_input("Enter item name: ")
        quantity = self.view.get_input("Enter quantity: ", is_float=True)
        price = self.view.get_input("Enter price: ", is_float=True)
        self.data.add_item(name, quantity, price)
        print(f"Item '{name}' added successfully!")

    def view_items(self):
        items = self.data.get_items()
        self.view.display_items(items)
