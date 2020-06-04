var1 = 5
def some_func():
    var2 = 6
#    print(var2)
    def some_inner_function():
        var3 = 7
        return var3
    some_inner_function()

    
    return var2
x = some_func()
print(x)
