#! usr/bin/python3
""" SIM COMPANIES PRICING ASSISTANT
    Developed by Dark, April-May 2020.

    Provide player details about the minimum 
    price at which he should sell his product 
    either on the Exchange or by contract in
    SimCompanies.

    No integrated UI; use with a REPL.

    Check out Sim Companies at
        https://www.simcompanies.com
"""


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

    xpt_cost = 0.342
    exc_pct = 0.03
   
    # STATIC METHODS

    @staticmethod
    def calc_price(
         src_cost, freight, tgt_mgn):
        ''' Return exchange & contract prices
            given source & freight costs and
           desired gross margin.
        '''

        # calc exchange price
        exch_price = (
            (src_cost + freight) /
            (1 - Product.exc_pct - tgt_mgn))

        # calc contract price
        contr_price = (
            (src_cost + freight / 2) /
            (1 - tgt_mgn))

        return exch_price, contr_price



    @staticmethod
    def calc_margin(
        exch_cogs, contr_cogs, price):
        """ Returns GPM, given cogs, price.
            See also CLI-friendly public 
            method 'cm'.
        """
        
        exch_mgn = (
            (price - exch_cogs) / price * 100)

        contr_mgn = (
            (price - contr_cogs) / price * 100)

        return exch_mgn, contr_mgn



    @staticmethod
    def fv(pv, i, n, t):
        ''' return future value of
            a given amount of money
            held presently
        '''
        # fv = pv * (1 + (i/n))**(n*t)
        return
       


    # DUNDERS

    def __init__(
        self, prod_type,
        src_cost, tgt_mgn=0.03):

        if prod_type.lower() in \
            Product.xpt_mult:

            self.prod_type = prod_type
            self.src_cost = src_cost
            self.tgt_mgn = tgt_mgn

            self.eval_attrs()

            self.list_options(0.5)

        else:
            print("Invalid product selection.")
            # return



    # REGULAR METHODS

    def eval_attrs(self):
        ''' calc freight as well as price and 
            cogs for both exchange and contract
        '''

        self.freight = (
            Product.xpt_cost * 
            Product.xpt_mult[self.prod_type])

        # calc exchange, contract prices
        self.exch_price, self.contr_price  = (
            Product.calc_price(
                self.src_cost,
                self.freight,
                self.tgt_mgn))

        # calc cost of goods sold (cogs)
        self.exch_cogs = (
            self.src_cost +
            self.freight +
            self.exch_price * 0.03)

        self.contr_cogs = (
            self. src_cost + 
            self.freight / 2)



    def tell_all(self):
        """ give user the full Monty """

        print(
            f"On the Exchange, sell your {self.prod_type} at $"
            f"{round(self.exch_price,2)}. Your sourcing cost was $"
            f"{self.src_cost}. Freight will cost ${round(self.freight,2)}. "
            f"The exchange fee will be ${round(self.exch_price*0.03,2)}. "
            f"Your total COGS is ${round(self.exch_cogs,2)}. "
            f"Your gross margin per unit sold will be $"
            f"{round(self.exch_price - self.exch_cogs,2)} "
            f"and your gross margin percentage will be "
            f"{round((self.exch_price - self.exch_cogs)/self.exch_price * 100,2)}%."
            "\n")

        print(
            f"By Contract, sell your {self.prod_type} at $"
            f"{round(self.contr_price,2)}. Your sourcing cost was $"
            f"{self.src_cost}. Freight will cost ${round(self.freight/2,2)}. "
            f"Your total COGS is ${round(self.contr_cogs,2)}. "
            f"Your gross margin per unit sold will be $"
            f"{round(self.contr_price - self.contr_cogs,2)} "
            f"and your gross margin percentage will be "
            f"{round((self.contr_price - self.contr_cogs)/self.contr_price * 100,2)}%."
            "\n")
        

    
    def list_options(self, mult, 
            lbound=1, ubound=11):
        ''' Provides a list of prices for both
            Exchange and contract by GPM.
        '''

        # print header rows
        print()
        print("Gross profit margins for",
                self.prod_type)
        print("-------------------------")
        print("Pct\t" "Exch\t" "Contr")
        print("-------------------------")


        # print data table
        for gpm in range(lbound, ubound):
            
            gpm *= mult

            exc, con = (
                Product.calc_price(
                    self.src_cost,
                    self.freight,
                    gpm/100))
            
            print(
                f"{gpm:,.2f}%".rjust(3),
                "\t"
                f"${exc:,.2f}\t"
                f"${con:,.2f}\t")

        print()



    def cm(self, price):
        ''' Calc margin on self. Easier to
            use on a CLI than the static
            method 'calc_margin' (WET).
        '''

        exch_price, contr_price = \
                Product.calc_margin(
                        self.exch_cogs,
                        self.contr_cogs,
                        price)

        return exch_price, contr_price



if __name__ == "__main__":

    print("ready for use in repl")



''' use later?
    print(
            f"Selling your product on the Exchange at ${price},"
            f"your gross margin will be ${round(price - self.exch_cogs,2)} "
            f"or {round((price - self.exch_cogs)/price * 100,2)}%."
        )
        
        print(
            f"Selling your product by contract at ${price},"
            f"your gross margin will be ${round(price - self.contr_cogs,2)} "
            f"or {round((price - self.contr_cogs)/price * 100,2)}%."

'''
