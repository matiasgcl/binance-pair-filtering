# requires: python-binance
# To retrieve data from Binance we need an API key (read only enough)
# public and secret key should be placed in API.data (first and second line, just the keys)
## Corrections-commentaries-new ideas : matiasgcl@protonmail.com
## Was this script useful?
## spread the love: Ethereum erc20: 0xDc3d1a7566a536CFbcaAeb0CD2a179d78062B4b6

from binance.client import Client

client = Client()

isUp = client.get_system_status()
assert isUp['status'] == 0 # Lets check we can actually retrieve information
print('System status ok\n')

info = client.get_all_tickers()
print('Insert the ticker for the pair you want to filter from (i.e. you dont want to see coins with this pair), e.g. USDT')
subs1 = input()
subs = subs1
aux = -1*len(subs)
res = [i['symbol'] for i in info if subs in i['symbol']]
res = [i[:aux] for i in res if i[aux:]=='USDT']

print('Insert the ticker for the pair you want to see, e.g. BTC')
subs2 = input()
subs = subs2
aux = -1*len(subs)
resbtc = [i['symbol'] for i in info if subs in i['symbol']]
resbtc = [i[:aux] for i in resbtc if i[aux:]==subs]

print('Insert the ticker for the pair you want to filter again (i.e. for the pairs which have the second one ticker you gave AND does not have the first pair, you want to exclude this new pair) e.g. BUSD')
subs3 = input()
subs = subs3
resbusd = [i['symbol'] for i in info if subs in i['symbol']]
resbusd = [i[:aux] for i in resbusd if i[aux:]==subs]

result1 = [x for x in resbtc if x not in res]
result2 = [x for x in resbusd if x not in res]
result = [x for x in result1 if x not in result2]
filtered = []
print('Tokens with '+subs2+' pair which does not have a '+subs1+' neither a '+subs3+' pair are:')
print('\nFrom the previous list, excluding non traded ones, we have (this may take a while):')
for i in range(len(result)):
    auxcheck = client.get_symbol_info(result[i]+subs2)
    if(auxcheck['status'] == 'TRADING'):
        filtered.append(result[i])

print(filtered)
print('\nCorrections-commentaries-new ideas : matiasgcl@protonmail.com')
print('\nWas this script useful? spread the love: \nEthereum erc20: 0xDc3d1a7566a536CFbcaAeb0CD2a179d78062B4b6')
