#!/usr/bin/env python3
# updates elastic search with portfolio data

import portfolio_consts
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, DocType, Date, Float, Keyword, Text
import datetime

# test all the elastic search things:
# this will have to be changed completely

# create dat connection yo
con = connections.create_connection(hosts=portfolio_consts.hosts, timeout=20)

# create dat doc class yo
class TestEntry(DocType):
    symbol = Text(analyzer='snowball', fields={'raw': Keyword()})
    price = Float()
    fumoney = Keyword()
    timestamp = Date()
    num_shares = Float()
    total_value = Float()

    class Meta:
        index = 'testindex'

    def save(self, ** kwargs):
        self.total_value = self.num_shares * self.price
        return super(TestEntry, self).save(** kwargs)

    #def is_published(self):
        #return datetime.datetime.now() < self.timestamp

# 'create mappings in elasticsearch'
TestEntry.init()

# create and save an entry
doc = TestEntry(meta={'id':2}, symbol='BS', fumoney=['$1B'])
doc.price = 100000000.99
doc.num_shares = 5
doc.timestamp = datetime.datetime.now()
doc.save()

td = TestEntry.get(id=2)
s = Search(using=con)
t = s.query('match', RiskModelScoreInit=10)
res = t.execute()

dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-8)))

testfile = open('test.txt', 'w')
testfile.write(str(dt))
testfile.write('\n')
testfile.write(str(td))
testfile.write('\n')
testfile.write(str(res.to_dict()))
testfile.write('\n')
testfile.write(str(connections.get_connection().cluster.health()))
testfile.write('\n')
testfile.write('\n')
testfil.close()