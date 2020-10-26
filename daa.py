import pandas as pd
import numpy as np


from dateutil.relativedelta import relativedelta
import math
df = pd.read_csv("apple.csv")


df = df.drop(index=0,axis=0)
df["1year"] = df["netinvest"].values


year = 1
year3 = 3
year5 = 5
year10 = 10

for i in range(len([1])):
    # database = df[df.F_key==df.F_key.unique()[i]]
    database = df
    database["Date"] = pd.to_datetime(database['date'], utc=False).dt.date
    database_new = database.drop("date",axis=1)
    database_new = database_new.sort_values('Date',ascending=False)
    database_new = database_new.reset_index()
    database_new = database_new.drop("index",axis=1)

    for j in range(len(database["netinvest"].values)):
        currentprice = database_new["Date"][j]
        datepastdate = currentprice - relativedelta(years=int(year))
        datepastdate3 = currentprice - relativedelta(years=int(year3))
        datepastdate5 = currentprice - relativedelta(years=int(year5))
        datepastdate10 = currentprice - relativedelta(years=int(year10))

        if datepastdate in database_new['Date'].values:
            print(datepastdate)
            currentyearbackprice = database_new[database_new['Date'] == currentprice]['netinvest']
            oneyearbackprice = database_new[database_new['Date'] == datepastdate]['netinvest']
            yr_value = float(currentyearbackprice) / float(oneyearbackprice)
            roll = (math.pow(yr_value, 1 / year) - 1) * 100
            database_new.loc[oneyearbackprice.index,"1year"] = roll
            print(roll)
        else:
            pass

        if datepastdate3 in database_new['Date'].values:
            print(datepastdate3)
            currentyearbackprice = database_new[database_new['Date'] == currentprice]['netinvest']
            oneyearbackprice3 = database_new[database_new['Date'] == datepastdate3]['netinvest']
            yr_value = float(currentyearbackprice) / float(oneyearbackprice3)
            roll = (math.pow(yr_value, 1 / year3) - 1) * 100
            database_new.loc[oneyearbackprice3.index, "3years"] = roll
            print(roll)
        else:
            pass

        if datepastdate5 in database_new['Date'].values:
            print(datepastdate5)
            currentyearbackprice = database_new[database_new['Date'] == currentprice]['netinvest']
            oneyearbackprice5 = database_new[database_new['Date'] == datepastdate5]['netinvest']
            yr_value = float(currentyearbackprice) / float(oneyearbackprice5)
            roll = (math.pow(yr_value, 1 / year5) - 1) * 100
            database_new.loc[oneyearbackprice5.index, "5years"] = roll
            print(roll)

        else:
            pass

        if datepastdate10 in database_new['Date'].values:
            print(datepastdate10)
            currentyearbackprice = database_new[database_new['Date'] == currentprice]['netinvest']
            oneyearbackprice10 = database_new[database_new['Date'] == datepastdate10]['netinvest']
            yr_value = float(currentyearbackprice) / float(oneyearbackprice10)
            roll = (math.pow(yr_value, 1 / year10) - 1) * 100
            database_new.loc[oneyearbackprice10.index, "10years"] = roll
            print(roll)

        else:
            pass

    print(database_new.tail())



year = 1
year3 = 3
year5 = 5
year10 = 10

for i in range(len([ramteja])):
    # database = df[df.F_key==df.F_key.unique()[i]]
    database = df1[df1.F_key==df1.F_key.unique()[i]]
    database["Date"] = pd.to_datetime(database['date'], utc=False).dt.date
    database_new = database.drop("date",axis=1)
    database_new = database_new.sort_values('Date',ascending=False)
    database_new = database_new.reset_index()
    database_new = database_new.drop("index",axis=1)

    for j in range(len(database["netinvest"].values)):
        currentprice = database_new["Date"][j]
        datepastdate = currentprice - relativedelta(years=int(year))
        datepastdate3 = currentprice - relativedelta(years=int(year3))
        datepastdate5 = currentprice - relativedelta(years=int(year5))
        datepastdate10 = currentprice - relativedelta(years=int(year10))

        if datepastdate in database_new['Date'].values:
            print(datepastdate)
            currentyearbackprice = database_new[database_new['Date'] == currentprice]['netinvest']
            oneyearbackprice = database_new[database_new['Date'] == datepastdate]['netinvest']
            yr_value = float(currentyearbackprice) / float(oneyearbackprice)
            roll = (math.pow(yr_value, 1 / year) - 1) * 100
            database_new.loc[oneyearbackprice.index,"1year"] = roll
            print(roll)
        else:
            pass

        if datepastdate3 in database_new['Date'].values:
            print(datepastdate3)
            currentyearbackprice = database_new[database_new['Date'] == currentprice]['netinvest']
            oneyearbackprice3 = database_new[database_new['Date'] == datepastdate3]['netinvest']
            yr_value = float(currentyearbackprice) / float(oneyearbackprice3)
            roll = (math.pow(yr_value, 1 / year3) - 1) * 100
            database_new.loc[oneyearbackprice3.index, "3years"] = roll
            print(roll)
        else:
            pass

        if datepastdate5 in database_new['Date'].values:
            print(datepastdate5)
            currentyearbackprice = database_new[database_new['Date'] == currentprice]['netinvest']
            oneyearbackprice5 = database_new[database_new['Date'] == datepastdate5]['netinvest']
            yr_value = float(currentyearbackprice) / float(oneyearbackprice5)
            roll = (math.pow(yr_value, 1 / year5) - 1) * 100
            database_new.loc[oneyearbackprice5.index, "5years"] = roll
            print(roll)

        else:
            pass

        if datepastdate10 in database_new['Date'].values:
            print(datepastdate10)
            currentyearbackprice = database_new[database_new['Date'] == currentprice]['netinvest']
            oneyearbackprice10 = database_new[database_new['Date'] == datepastdate10]['netinvest']
            yr_value = float(currentyearbackprice) / float(oneyearbackprice10)
            roll = (math.pow(yr_value, 1 / year10) - 1) * 100
            database_new.loc[oneyearbackprice10.index, "10years"] = roll
            print(roll)

        else:
            pass

    print(database_new.tail())
