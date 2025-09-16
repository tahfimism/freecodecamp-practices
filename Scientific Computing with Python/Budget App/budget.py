class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
    
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True


    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

    

def create_spend_chart(categories):
    # 1. Calculate total spent per category and overall
    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        spent.append(total)
    total_spent = sum(spent)

    # 2. Calculate percentage spent per category (rounded down to nearest 10)
    percents = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    # 3. Build the chart lines
    lines = ["Percentage spent by category"]
    for i in range(100, -1, -10):
        line = f"{i:>3}|"
        for p in percents:
            if p >= i:
                line += " o "
            else:
                line += "   "
        line += " "
        lines.append(line)

    # 4. Add the horizontal line
    lines.append("    " + "-" * (len(categories) * 3 + 1))

    # 5. Prepare category names vertically
    names = [cat.name for cat in categories]
    maxlen = max(len(name) for name in names)
    for i in range(maxlen):
        line = "     "
        for name in names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        lines.append(line)

    return "\n".join(lines)



