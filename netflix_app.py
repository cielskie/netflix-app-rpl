def f(a, b):
    if b == 1:
        print("Play " + a)
    elif b == 2:
        print("Add " + a + " to fav")
    else:
        print("Error")

def p(x):
    for i in range(len(x)):
        print(x[i])

movies = ["Wednesday", "Stranger Things", "Money Heist"]

p(movies)
f("Wednesday", 1)
