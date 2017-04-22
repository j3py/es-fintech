#!/usr/bin/env python3
# updates postgresql db with portfolio data

import portfolio_consts
import psycopg2

# add SQLAlchemy!!!
# test all the postgres things
# this will have to be changed completely!

try:
    connect_str = portfolio_consts.connect_str
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
    cursor.execute("CREATE TABLE portfolio (id serial PRIMARY KEY, name char(40));")
    # run an INSERT statement
    cursor.execute("""INSERT INTO portfolio () VALUES ()""")
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
    
	
class PortfolioEntry(Base):
    __tablename__ = 'portfolio'
    
    id bigserial PRIMARY KEY, 
    timestamp timestamp, 
    symbol varchar(16), 
    AverageDailyVolume bigint, 
    BookValue double precision, 
    Change_PercentChange varchar(32), 
    Change double precision, 
    Currency varchar(16), 
    DividendShare double precision, 
    LastTradeDate date, 
    EarningsShare double precision, 
    EPSEstimateCurrentYear double precision, 
    EPSEstimateNextYear double precision, 
    EPSEstimateNextQuarter double precision, 
    DaysLow double precision, 
    DaysHigh double precision, 
    YearLow double precision, 
    YearHigh double precision, 
    MarketCapitalization varchar(32), 
    EBITDA varchar(32), 
    ChangeFromYearLow double precision, 
    PercentChangeFromYearLow varchar(32), 
    ChangeFromYearHigh double precision, 
    PercebtChangeFromYearHigh varchar(32), 
    LastTradeWithTime varchar(48), 
    LastTradePriceOnly double precision, 
    DaysRange varchar(32), 
    FiftydayMovingAverage double precision, 
    TwoHundreddayMovingAverage double precision, 
    ChangeFromTwoHundreddayMovingAverage double precision, 
    PercentChangeFromTwoHundreddayMovingAverage varchar(32), 
    ChangeFromFiftydayMovingAverage double precision, 
    PercentChangeFromFiftydayMovingAverage varchar(32), 
    Name varchar(256), 
    Open double precision, 
    PreviousClose double precision, 
    ChangeinPercent varchar(32), 
    PriceSales double precision, 
    PriceBook double precision, 
    ExDividendDate date, 
    PERatio double precision, 
    DividendPayDate date, 
    PEGRatio double precision, 
    PriceEPSEstimateCurrentYear double precision, 
    PriceEPSEstimateNextYear double precision, 
    ShortRatio double precision, 
    LastTradeTime time, 
    OneyrTargetPrice double precision, 
    Volume bigint, 
    YearRange varchar(32), 
    StockExchange varchar(32), 
    DividendYield double precision, 
    PercentChange varchar(32), 
    RiskModelScoreInit integer, 
    RiskModelScoreCurrent integer, 
    PEGScoreInit integer, 
    PEGScoreCurrent integer, 
    DivScoreInit integer, 
    DivScoreCurrent integer, 
    ShortScoreInit integer, 
    ShortScoreCurrent integer, 
    PriceScoreInit integer, 
    PriceScoreCurrent integer, 
    OverseasScoreInit integer, 
    OverseasScoreCurrent integer, 
    DivYieldInit double precision, 
    NumOfSharesInit double precision, 
    NumOfSharesCurrent double precision,
    PriceInit double precision, 
    TotalValueInit double precision, 
    TotalValueCurrent double precision, 
    PercentOfTotalPortfolioValue double precision, 
    PercentGainSinceInception double precision, 
    TotalPortfolioValueInit double precision, 
    TotalPortfolioValueCurrent double precision, 
    TotalPortfolioGainSinceInception double precision
    
    def save(self, ** kwargs):
        self.RiskModelScoreCurrent = self.PEGScoreCurrent + self.DivScoreCurrent + self.ShortScoreCurrent + self.PriceScoreCurrent + self.OverseasScoreCurrent
        
        self.TotalValueCurrent = self.NumOfSharesCurrent * self.LastTradePriceOnly
        
        self.PercentOfTotalPortfolioValue = self.TotalValueCurrent / self.TotalPortfolioValueCurrent
        
        self.PercentGainSinceInception = (self.TotalValueCurrent - self.TotalValueInit) / self.TotalValueInit
        
        self.TotalPortfolioGainSinceInception = (self.TotalPortfolioValueCurrent - self.TotalPortfolioValueInit) / self.TotalPortfolioValueInit
        
        self.stored_at = datetime.datetime.now()
        return super(TestEntry, self).save(** kwargs)
    
    def __repr__(self):
        return "<PortfolioEntry(symbol='%s', created_at='%s')>" % (self.symbol, self.created_at)