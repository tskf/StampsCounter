# Stamps Counter

Calculate the best combination of items for a given value (knapsack problem). For example - helps choosing the cheepest stamps for a letter based on provided values, prices and limited by count. Specifically it can be useful for choosing non-denominated stamps.


## Usage - generate()

### Parameters
#### Lists: Value (required), Price, Count
- Index is the same for a given item across lists,
  - example for item 0: Value[0], Price[0], Count[0].
- Value: current value of a stamp.
- Price: for how much a non-denominated stamp was bought.
- Count: limit a stamp usage in a combination.
#### Integer: max_price
- Generate combinations up to a given price.
- By default: max price from Price list.

### Return Values
#### List: BestValue
- index = price
- element = the best value for a given price
#### List: AddedItems
- index = price
- element = [price paid, [list of added items by value]]

### Example
```python
Value = [ 5, 10, 20, 30, 40, 50, 200, 350]
Price = [ 5, 10, 20, 30, 40, 50, 180, 320]
Count = [20, 10, 10, 10, 10, 10,   4,   5]
```
#### Calculate lookup lists:
```python
BestValue, AddedItems = generate(Value, Price, Count, max_price=2000)
```
#### Use them to find the best combinations:
```python
items_value = 1000
for i in range(items_value+1):
    if BestValue[i] >= items_value:
        value = BestValue[i]
        price = AddedItems[i][0]
        diff  = items_value-AddedItems[i][0]
        items = AddedItems[i][1]
        break
```
```
value: 1000
price: 910
diff:  90
items: [50, 200, 200, 200, 350]
```