items = {
 'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
 'cheese':{'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
 'sausage':{'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}

def CountLess20(items : dict, key : str):
 if(items[key]['count'] < 20):
  return True
 else:
  return False

resultList = {}

for key in items:
 resultList[key] = CountLess20(items, key)

print(resultList)