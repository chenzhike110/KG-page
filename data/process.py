import json

f = open('data/dishes.json')
data = json.load(f)

result = [
    {'工艺':'切', '菜名':[]},
    {'工艺':'焯', '菜名':[]},
    {'工艺':'拌', '菜名':[]},
    {'工艺':'煮', '菜名':[]}
]

for dish in data:
    for action in result:
        for step in dish["步骤"]:
            if action['工艺'] in step:
                action['菜名'].append(dish["菜名"])
                break


with open('data/process.json', 'w') as outfile:
    outfile.write(json.dumps(result, ensure_ascii=False, indent=4))

