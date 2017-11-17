from sklearn import tree

#Impeative programming in python 
a = [10,20]
len(a)
type(a)
print(type(a))

#OOP programming in python 
dt = tree.DecisionTreeClassifier()

#Traditional functional programming
age = [1,2,3,4,]
i = 0
for e in age:
    age[i] = e + 10
    i = i + 1
print(age)

#Convert above traditional functional programming to better in python
age = [1,2,3,4,]
i = 0
for i,e in enumerate(age):
    age[i] = e + 10
print(age)

#Convert above traditional functional programming to MOST EFFICIENT in python by using
#map object is more effective and parallel process operator instead of for loop
#map object more scalable. Use map object instead of for loop
age = [1,2,3,4,]
i = 0
def incr(e):
    return e+10
age = map(incr, age)
print(age) #This returns an object.

age = list(map(incr, age)) #Let's convert this object to list for display purpose
print(age)

#Let us write even shorter code
#Using lambda. Lambda is anonymous function/in-line funtion
age = [1,2,3,4,]
i = 0
age = list(map(lambda e:e+10, age)) #labda is replace incr function.
print(age)

#Note that lambda is used only when you don't want to re-use the function and just at one place.