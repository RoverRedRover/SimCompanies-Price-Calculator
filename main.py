#! usr/bin/python3
""" Provide player details about the minimum price at which he should sell his product either on the Exchange or by contract in SimCompanies. """

__version__ = 2.0  # Prior code contained in "old.txt"


class Product:

    xpt_mult = {
        "seed": 0.1,
        "apples": 1,
        "oranges": 1,
        "grapes": 1,
        "grain": 0.1,
        "sugarcane": 0.1,
        "cotton": 0.5,
        "wood": 1
    }

    xpt_cost = 0.346
    exc_pct = 0.030
    tgt_mgn = 0.075

    def __init__(self, prod_type, src_cost):

        if prod_type.lower() in Product.xpt_mult:

            self.prod_type = prod_type
            self.src_cost = src_cost
            self.freight = Product.xpt_cost * Product.xpt_mult[self.prod_type]
            self.freight_contr = self.freight / 2
            self.exch_price = (self.src_cost + self.freight) / (
                1 - Product.exc_pct - Product.tgt_mgn)
            self.exch_fee = self.exch_price * 0.03
            self.exch_cogs = self.src_cost + self.freight + self.exch_fee
            self.contr_price = (self.src_cost + self.freight_contr) / (
                1 - Product.tgt_mgn)

            """TODO with open("history.txt", "w") as text_file:
                text_file.write()"""

        else:
            print("Invalid product selection.")
            return

    def tell_all(self):
        """ give user the full Monty """
        print(
            f"On the Exchange, sell your {self.prod_type} at $"
            f"{round(self.exch_price,2)}. Your sourcing cost was $"
            f"{self.src_cost}. Freight will cost ${round(self.freight,2)}. "
            f"The exchange fee will be ${round(self.exch_fee,2)}. "
            f"Your total COGS is ${round(self.exch_cogs,2)}. "
            f"Your gross margin per unit sold will be $"
            f"{round(self.exch_price - self.exch_cogs,2)} "
            f"and your gross margin percentage will be "
            f"{round((self.exch_price - self.exch_cogs)/self.exch_price * 100,2)}%."
        )

    def what_if(self, price):
        """ provide margin at prospective unit price """
        #TODO
        pass
