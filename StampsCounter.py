Value = [ 5, 10, 20, 30, 40, 50, 200, 350]
Price = [ 5, 10, 20, 30, 40, 50, 180, 320]
Count = [20, 10, 10, 10, 10, 10,   4,   5]


def sort_by_first(*list):
    return zip(*sorted(zip(*list)))


def generate(Value, Price=None, Count=None, max_price=None):
    if Price == None:
        if Count == None:
            Value.sort()
        else:  #sort two lists by value
            Value, Count = sort_by_first(Value, Count)
        Price = Value

    max_price = max(Price+[max_price]) + 1
    len_price = len(Price)

    BestValue = [0] * max_price
    #list:  index = price
    ######  element = the best value for a given price

    AddedItems = [[0,[]]] * max_price
    #list:  index = price
    ######  element = [price paid, [list of added items by value]]

    for cp in range(max_price):  #cp = current_price
        for ip in range(len_price):  #ip = index_price
            pp = cp-Price[ip]  #pp = previous_price
            if Price[ip] <= cp  and  ( Count == None or #limit by count:
               AddedItems[pp][1].count(Value[ip]) < Count[ip] ):
                value2 = BestValue[pp] + Value[ip]
                if BestValue[cp] <= value2:  #BestValue updated
                    BestValue[cp] = value2
                    AddedItems[cp] = [
                        AddedItems[pp][0] + Price[ip],
                        AddedItems[pp][1] + [Value[ip]] ]

    return BestValue, AddedItems


#example
items_value = 1000
BestValue, AddedItems = generate(Value, Price, Count, max_price=items_value)

for i in range(items_value+1):
    if BestValue[i] >= items_value:
        print 'value:', BestValue[i]
        print 'price:', AddedItems[i][0]
        print 'diff: ', items_value-AddedItems[i][0]
        print 'items:', AddedItems[i][1]
        break
