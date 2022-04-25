def buy_chocolate(x,y):
    change=x%y
    bars=int((x-change)/y)
    print("You can buy ",bars, " chocolate bars. And the money left is ",change,".")
    return[bars,change]
#Here's example

print(buy_chocolate(100,7))
#will return:
#You can buy  14  chocolate bars. And the money left is  2 .
#[100, 7]
