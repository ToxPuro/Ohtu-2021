from matchers import And, PlaysIn, HasAtLeast, Not, HasFewerThan, Or, All
class QueryBuilder():
    def __init__(self, query=All()):
        self.query=query

    def playsIn(self,team):
        return QueryBuilder(And(self.query,PlaysIn(team)))

    def hasAtLeast(self,value, attr):
        return QueryBuilder(And(self.query,HasAtLeast(value, attr)))

    def hasFewerThan(self,value,attr):
        return QueryBuilder(And(self.query,HasFewerThan(value,attr)))

    def build(self):
        return self.query
