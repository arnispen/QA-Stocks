from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

SYM_500_NO_STRING = []

for i in range(0, len(trs)):
    SYM_500_NO_STRING.append(trs[i])

SYM_500_NO_STRING = SYM_500_NO_STRING[2:]

SYM_500_WITH_NUMBERS = []

for sym in SYM_500_NO_STRING:
    sym_a = sym.find('a')
    SYM_500_WITH_NUMBERS.append(sym_a)

SYM_500 = []

for i in range(0, len(SYM_500_WITH_NUMBERS)):
    if SYM_500_WITH_NUMBERS[i] != -1:
        SYM_500.append(SYM_500_WITH_NUMBERS[i].string)