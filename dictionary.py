capital={"one":1,
         "two":2,
         "three":3
}
print(type(capital))

print(len(capital))
capital["three"]="03"
print(capital)
print(capital.keys())
print(capital.values())
del capital["three"]
print(capital)