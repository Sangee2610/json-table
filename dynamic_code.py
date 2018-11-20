#code to print a json file as table - Pragatheeswaran R

from prettytable import PrettyTable
import json

table = PrettyTable()
table.field_names = ["Rule Name(Localized)", "Rule impact", "Priority", "color"]
with open("result.json", "r") as read_file:
    data = json.load(read_file)
    for key in data.items():
        trace_1=data.get("results")
        for key in trace_1.items():
            dictonary_list=trace_1.get("rule_results")
            index = 0
            while index < len(dictonary_list):
                for key in dictonary_list[index]:
                    impact=dictonary_list[index].get("rule_impact")
                    name=dictonary_list[index].get("localized_rule_name")
                    if impact <=1:
                        priority="low"
                        color="Green"
                    elif impact > 10:
                        priority="High"
                        color="Red"
                    else:
                        priority="Normal"
                        color="Amber"
                    result=table.add_row([name, impact, priority, color])
                    index += 1
                    break
            break
        break
print(table)
                    



