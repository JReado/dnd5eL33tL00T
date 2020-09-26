def yes_or_no():
        YesNo = input(""" \n Yes or No? \n """)
        YesNo = YesNo.lower()
        if(YesNo == "yes" or YesNo == 'y'):
            return True
        elif(YesNo == "no" or YesNo == 'n'):
            return False
        else:
            print(""" \n Invalid. Yes or No only. \n """)
            return yes_or_no()


class wallet:
    _wallets = []
    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls, *args, **kwargs)
        cls._wallets.append(instance)
        return instance
        
    def __init__(self):
        self.name = input("""\nName?\n""")
        print(""" \nWould you like to add current money to the wallet?\n """)
        onboardYN = yes_or_no()
        if onboardYN == True:
            cp = int(input(""" \n Number of copper pieces? \n """))
            sp = int(input(""" \n Number of silver pieces? \n """))
            ep = int(input(""" \n Number of electrum pieces? \n """))
            gp = int(input(""" \n Number of gold pieces? \n """))
            pp = int(input(""" \n Number of platinum pieces? \n """))
            currency = (pp * 1000) + (gp * 100) + (ep * 50) + (sp * 10) + cp
            self.platinum = pp
            self.gold = gp
            self.electrum = ep
            self.silver = sp
            self.copper = cp
            print("""\n{}'s wallet:\n\nPlatinum: {} \nGold: {} \nElectrum: {} \nSilver: {} \nCopper: {} \n""".format(self.name,pp, gp, ep, sp, cp))
        elif onboardYN == False:
            currency = 0
            print("""\n{}'s wallet is empty\n""".format(self.name))
        self.balance = currency
        
    
    def __str__(self):
        total = self.balance
        cp = 0
        sp = 0
        ep = 0
        gp = 0
        pp = 0
        pp = total // 1000
        total = total % 1000
        gp = total // 100
        total = total % 100
        ep = total // 50
        total = total % 50
        sp = total // 10
        total = total % 10
        cp = total
        if gp < 100 and pp >= 10:
            gp = gp + 100
            pp = pp - 10
        if sp < 50 and gp > 5:
            gp = gp - 5
            sp = sp + 50
        self.platinum = pp
        self.gold = gp
        self.electrum = ep
        self.silver = sp
        self.copper = cp
        return("""{}'s wallet:\n\nPlatinum: {} \nGold: {} \nElectrum: {} \nSilver: {} \nCopper: {} \n""".format(self.name,pp, gp, ep, sp, cp))
    
    
    def add(self):
        cp = int(input(""" \n Number of copper pieces? \n """))
        sp = int(input(""" \n Number of silver pieces? \n """))
        ep = int(input(""" \n Number of electrum pieces? \n """))
        gp = int(input(""" \n Number of gold pieces? \n """))
        pp = int(input(""" \n Number of platinum pieces? \n """))
        currency = (pp * 1000) + (gp * 100) + (ep * 50) + (sp * 10) + cp
        self.balance += currency
        print(self)
        
    def buy(self):
        cp = int(input(""" \n Number of copper pieces? \n """))
        sp = int(input(""" \n Number of silver pieces? \n """))
        ep = int(input(""" \n Number of electrum pieces? \n """))
        gp = int(input(""" \n Number of gold pieces? \n """))
        pp = int(input(""" \n Number of platinum pieces? \n """))
        currency = (pp * 1000) + (gp * 100) + (ep * 50) + (sp * 10) + cp
        if self.balance < currency:
            print("""\nYou're broke. Not enough cash. Get gud.\n""")
        else:
            self.balance -= currency
        print(self)
            
class loot(object):
    _loot_lst = []
    limit = 1
    
    def __new__(cls,*args, **kwargs):
        if not len(cls._loot_lst) <= cls.limit:
            raise RuntimeError("Could not create. Loot already exists. Check status with print(loot)")
        else:
            instance = object.__new__(cls,*args, **kwargs)
            cls._loot_lst.append(instance)
            return instance
        
    def __init__(self):
       self.name = 'loot'
       self.balance = 0
       self.platinum = 0
       self.gold = 0
       self.electrum = 0
       self.silver = 0
       self.copper = 0
        
    def __str__(self):
        total = self.balance
        cp = 0
        sp = 0
        ep = 0
        gp = 0
        pp = 0
        pp = total // 1000
        total = total % 1000
        gp = total // 100
        total = total % 100
        ep = total // 50
        total = total % 50
        sp = total // 10
        total = total % 10
        cp = total
        if gp < 100 and pp >= 10:
            gp = gp + 100
            pp = pp - 10
        if sp < 50 and gp > 5:
            gp = gp - 5
            sp = sp + 50
        self.platinum = pp
        self.gold = gp
        self.electrum = ep
        self.silver = sp
        self.copper = cp
        return("""\nLoot status: \n \nPlatinum: {} \nGold: {} \nElectrum: {} \nSilver: {} \nCopper: {} \n""".format(pp, gp, ep, sp, cp))
    
    def add(self):
        cp = int(input(""" \n Number of copper pieces? \n """))
        sp = int(input(""" \n Number of silver pieces? \n """))
        ep = int(input(""" \n Number of electrum pieces? \n """))
        gp = int(input(""" \n Number of gold pieces? \n """))
        pp = int(input(""" \n Number of platinum pieces? \n """))
        currency = (pp * 1000) + (gp * 100) + (ep * 50) + (sp * 10) + cp
        self.balance += currency
        print(self)
        
    def buy(self):
        cp = int(input(""" \n Number of copper pieces? \n """))
        sp = int(input(""" \n Number of silver pieces? \n """))
        ep = int(input(""" \n Number of electrum pieces? \n """))
        gp = int(input(""" \n Number of gold pieces? \n """))
        pp = int(input(""" \n Number of platinum pieces? \n """))
        currency = (pp * 1000) + (gp * 100) + (ep * 50) + (sp * 10) + cp
        if self.balance < currency:
            print("""\nYou're broke. Not enough cash. Get gud.\n""")
        else:
            self.balance -= currency
        print(self)
            
    def cashout(self):
        print(""" \nCashing out the loot. Are you sure? \n """)
        YesNo = yes_or_no()
        if YesNo == True:
            num_players = int(input("""\nHow many players are splitting the pot?  """))
            share = self.balance // num_players
            kitty = self.balance % num_players
            total = share
            cp = 0
            sp = 0
            ep = 0
            gp = 0
            pp = 0
            pp = total // 1000
            total = total % 1000
            gp = total // 100
            total = total % 100
            ep = total // 50
            total = total % 50
            sp = total // 10
            total = total % 10
            cp = total
            print("""\n{} remains in the kiity\n""".format(kitty))
            print("""\nShare value:\nPlatinum: {} \nGold: {} \nElectrum: {} \nSilver: {} \nCopper: {} \n""".format(pp, gp, ep, sp, cp))
            print("""\nAdd share to tracked wallets?\n""")
            add_share_YN = yes_or_no()
            if add_share_YN == True:
                for people in wallet._wallets:
                    people.balance += share
                    print(people)
            self.balance = kitty
            print(self)
def help():
    print("""\nThe running total of the loot is set to the variable 'loot'\n
          To track money for a player, type '(player name) = wallet()'\n
          To add to loot, type 'loot.add()'\n
          To add to a player type '(player name).add()'\n
          If a player spends money, type '(player name).buy()'\n
          If the group wants to buy something from the loot, type 'loot.buy()'\n
          To see the status of either loot or player wallet, type 'print(name)'\n
          To divy out the loot, type 'loot.cashout()'. This will clear the loot's balance\n
          Forget what variable you used for a player? List the wallets using 'players()'\n""")

def players():
    player_lst = []
    var = globals()
    for x in var:
        if type(var[x]) == wallet:
            player_lst.append(x)
            print("""\n{} is the variable for:""".format(x))
            print(var[x])

            
Epstein_Didnt_Kill_Himself = True                
loot = loot()
print("""Welcome to DNDL00T! For an overview of things you can do, call "help()" but more than likely you're on your own.\n""")