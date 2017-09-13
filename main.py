import hello

hello.hello()




# Run through every single last thing in the hello module, and try to execute it >:)
for thing in dir(hello):
    try:
        thing()
        print("Successfully executed thing: %s" % str(thing))
    except TypeError:
        print("Could not execute thing: %s. (TypeError)" % str(thing))




























hello.helloMemeBoi()
hello.goodbye()









hello.benchmark()

