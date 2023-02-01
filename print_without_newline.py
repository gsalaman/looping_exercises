# to print without a newline, you specify the "end" condition, like so:
print("This ", end="")
print("doesn't ", end="")
print("have ", end="")
print("newlines")

#note the last one doesn't specify an end, as I want a newline before the next section.


# note you can use any string as your end condition...and it will print that.  
print("underlines",end="_")
print("between",end="_")
print("words")
