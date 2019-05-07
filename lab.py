import tushare as ts

def initiate(file='test'):

    with open ('token/%s'%file, 'r') as t:
        token = t.read()

    return ts.pro_api(token)


df = initiate().daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')

print(df)