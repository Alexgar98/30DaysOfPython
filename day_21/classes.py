import statistics #Using this instead of numpy per subject

#Would normally put the classes in another file, but it's gonna be fine for now
class Statistics:
    def __init__(self, datalist):
        self.datalist = datalist
    def count(self):
            return len(self.datalist)
    def sum(self):
        return sum(self.datalist)
    def min(self):
        return min(self.datalist)
    def max(self):
        return max(self.datalist)
    def range(self):
        return (max(self.datalist) - min(self.datalist))
    def mean(self):
        return statistics.mean(self.datalist)
    def median(self):
        return statistics.median(self.datalist)
    def mode(self):
        mode = statistics.mode(self.datalist)
        return {'mode' : mode, 'count' : self.datalist.count(mode)}
    def std(self):
        return statistics.stdev(self.datalist)
    def var(self):
        return statistics.variance(self.datalist)
    def freq_dist(self):
        dist = []
        unique_ages = []
        for age in self.datalist:
            if not age in unique_ages:
                unique_ages.append(age)
        for age in unique_ages:
            dist.append((self.datalist.count(age) / len(self.datalist) * 100, age))
        dist.sort(reverse=True, key=lambda x : x[1])
        dist.sort(reverse=True, key=lambda x : x[0])
        return dist
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())

class PersonAcount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()
        self.properties = []
    def total_income(self):
        sum = 0
        for income in self.incomes:
            sum += income[0]
        return sum
    def total_expense(self):
        sum = 0
        for expense in self.expenses:
            sum += expense[0]
        return sum
    def account_info(self):
        return f'{self.firstname} {self.lastname}:\nIncome: {self.total_income()}\nExpenses: {self.total_expense()}\nProperties: {self.properties}'
    def add_income(self, income):
        self.incomes.add(income)
    def add_expenses(self, expense):
        self.expenses.add(expense)
    def account_balance(self):
        return self.total_income() - self.total_expense()

person = PersonAcount("Alex", "Garcia")
person.add_income((200, 'English lessons'))
person.add_expenses((200, 'A huge dragon'))
person.add_expenses((50, 'Petrol'))
print(person.total_income())
print(person.total_expense())
print(person.account_info())
print(person.account_balance())