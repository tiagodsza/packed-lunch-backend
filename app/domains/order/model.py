from app.domains.food import Food


class Order:
    def __init__(self, order:[Food]):
        self.order = order
