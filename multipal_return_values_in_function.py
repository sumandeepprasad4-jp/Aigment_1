def arithmetic(q,p):
    add=q+p
    sub=q-p
    mul=q*p
    return add,sub,mul
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c,d,f=arithmetic(a,b)
print(f"addition of {a} and {b} = {c}")
print(f"subtraction of {a} and {b} = {d}")
print(f"multiplication of {a} and {b} ={f}")