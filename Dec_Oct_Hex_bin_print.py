def print_formatted(number):
    width=len(bin(number))-2
    for i in range(1,number+1):
        dec=str(i)
        octal_num=oct(i)[2:]
        hex_num=hex(i)[2:]
        Binar_num=bin(i)[2:]
        print(f"{dec:>{width}} { octal_num:>{width}} { hex_num:>{width}} {Binar_num:>{width}}")
    return

n=int(input("Enter a number"))
print_formatted(n)
