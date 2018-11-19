import json
from pprint import pprint
from prettytable import PrettyTable
t = PrettyTable(['Rule Name(Localized)', 'Rule Impact', 'Priority', 'Color'])
with open('result.json') as f:
    data=json.load(f)
i=0    
while(i<=22):
    rule_impact=data['results']['rule_results'][i]['rule_impact']
    rule_name=data['results']['rule_results'][i]['rule_name']
    if rule_impact>=0 and rule_impact>=1:
        t.add_row([rule_impact,rule_name, "low" ,"green"])
    elif rule_impact>=10:
        t.add_row([rule_impact,rule_name, "high" ,"red"])
    else:
        t.add_row([rule_impact,rule_name, "normal" ,"amber"])
    i=i+1
print(t)





























