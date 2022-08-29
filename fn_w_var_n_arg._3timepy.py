#wap to create a function with variable number of args,
#call this funtion 3 time with diffrent no. of value each time
#show each value with its type
def fn6(*k):
    for i in k:
        print("value is",k)
        print("type of this value is",type(k))


fn6(100)
fn6(True)
fn6("Anas")
fn6(1.5)
