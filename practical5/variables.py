a=19245301# The number of cases of COVID-19 in March 7th, 2022
b=4218520# The number of cases of COVID-19 in 2021
c=271# The number of cases of COVID-19 in 2020
d=b-c#difference between 2021 and 2020,meaning new cases in 2020
e=a-b#difference between 2022 and 2021,meaning new cases in 2021
print("d is "+str(d))
print("e is "+str(e))
if d<e:
    print("d is less than e, " + "meaning there's more new cases in 2021")
if d==e:
    print("d is the same as e, "+ "meaning there's same new cases in 2020 and 2021")
if d>e:
    print("d is more than e, " + "meaning there's more new cases in 2020")
#I'm not so sure about "test all the probable value"
#Does it means that X\Y are input values?
print("Here is an example, you can input the bool value for X and Y and the program will caculate the 'and' result of it")
X=True
Y=False
print("X is "+str(X))
print("Y is "+str(Y))
W= X and Y
print ("W is "+str(W))
#Above is an example of the "and" result of 2 variables.
#Now is the place to test other results of the "and" caculation of bool value
print("Now input your own value for X and Y")
X=input()
Y=input()
W=X and Y
print("W is "+str(W))
#3.2
