def print_msg(nsg):
    def printer():
        print(nsg)
    return printer
print_msg("Hello")

