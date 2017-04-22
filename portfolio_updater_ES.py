#!/usr/bin/env python3
# updates elastic search with portfolio data

import portfolio_consts
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, DocType, Date, Float, Keyword, Text, Double, Long, Short
import datetime

# test all the elastic search things:
# this will have to be changed completely

# create dat connection yo
con = connections.create_connection(hosts=portfolio_consts.hosts, timeout=20)

# create dat doc class yo
class TestEntry(DocType):
    timestamp = Date()
    symbol = Text(analyzer='standard', fields={'raw': Keyword()})
    AverageDailyVolume = Long()
    BookValue = Double()
    Change_PercentChange = Text(analyzer='standard')
    Change = Double()
    Currency = Text(analyzer='standard', fields={'raw': Keyword()})
    DividendShare = Double()
    LastTradeDate = Date()
    EarningsShare = Double()
    EPSEstimateCurrentYear = Double()
    EPSEstimateNextYear = Double()
    EPSEstimateNextQuarter = Double()
    DaysLow = Double()
    DaysHigh = Double()
    YearLow = Double()
    YearHigh = Double()
    MarketCapitalization = Text(analyzer='standard')
    EBITDA = Text(analyzer='standard')
    ChangeFromYearLow = Double()
    PercebtChangeFromYearLow = Text(analyzer='standard')
    LastTradeWithTime = Text(analyzer='standard')
    LastTradePriceOnly = Double()
    DaysRange = Text(analyzer='standard')
    FiftydayMovingAverage = Double()
    TwoHundreddayMovingAverage = Double()
    ChangeFromTwoHundreddayMovingAverage = Double()
    PercentChangeFromTwoHundreddayMovingAverage = Text(analyzer='standard')
    ChangeFromFiftydayMovingAverage = Double()
    PercentChangeFromFiftydayMovingAverage = Text(analyzer='standard')
    Name = Text(analyzer='standard', fields={'raw': Keyword()})
    Open = Double()
    PreviousClose = Double()
    ChangeinPercent = Text(analyzer='standard')
    PriceSales = Double()
    PriceBook = Double()
    ExDividendDate = Date()
    PERatio = Double()
    DividendPayDate = Date()
    PEGRatio = Double()
    PriceEPSEstimateCurrentYear = Double()
    PriceEPSEstimateNextYear = Double()
    ShortRatio = Double()
    LastTradeTime = Date()
    OneyrTargetPrice = Double()
    Volume = Long()
    YearRange = Text(analyzer='standard')
    StockExchange = Text(analyzer='standard', fields={'raw': Keyword()})
    DividendYield = Double()
    PercentChange = Text(analyzer='standard')
    RiskModelScoreInit = Short()
    RiskModelScoreCurrent = Short()
    PEGScoreInit = Short()
    PEGScoreCurrent = Short()
    DivScoreInit = Short()
    DivScoreCurrent = Short()
    ShortScoreInit = Short()
    ShortScoreCurrent = Short()
    PriceScoreInit = Short()
    PriceStoreCurrent = Short()
    OverseasScoreInit = Short()
    OverseasScoreCurrent = Short()
    DivYieldInit = Double()
    NumOfSharesInit = Double()
    NumOfSharesCurrent = Double()
    PriceInit = Double()
    TotalValueInit = Double()
    TotalValueCurrent = Double()
    PercentOfTotalPortfolioValue = Double()
    PercentGainSinceInception = Double()
    TotalPortfolioValueInit = Double()
    TotalPortfolioValueCurrent = Double()
    TotalPortfolioGainSinceInception = Double()
    stored_at = Date()

    class Meta:
        index = 'portfolio'

    def save(self, ** kwargs):
        self.RiskModelScoreCurrent = self.PEGScoreCurrent + self.DivScoreCurrent + self.ShortScoreCurrent + self.PriceScoreCurrent + self.OverseasScoreCurrent
        
        self.TotalValueCurrent = self.NumOfSharesCurrent * self.LastTradePriceOnly
        
        self.PercentOfTotalPortfolioValue = self.TotalValueCurrent / self.TotalPortfolioValueCurrent
        
        self.PercentGainSinceInception = (self.TotalValueCurrent - self.TotalValueInit) / self.TotalValueInit
        
        self.TotalPortfolioGainSinceInception = (self.TotalPortfolioValueCurrent - self.TotalPortfolioValueInit) / self.TotalPortfolioValueInit
        
        self.stored_at = datetime.datetime.now()
        return super(TestEntry, self).save(** kwargs)


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