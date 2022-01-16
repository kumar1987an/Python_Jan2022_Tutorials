print("=======================================")
L1 = "spam ham egg bacon spring boot".split()
print(L1)
print("=======================================")
# Indexing

print(f"{L1[3] = }")  # forward indexing
print(f"{L1[-2] = }")  # reverse indexing
print(f"{L1[4] = }")  # forward indexing
print(f"{L1[5] = }")  # forward indexing
print(f"{L1[2] = }")  # forward indexing
print(f"{L1[-6] = }")  # reverse indexing
print(f"{L1[0] = }")  # forward indexing

print()

# Forward Index Slicing

## L1[start: stop: step]

print(f"{L1[0:1] = }")
print(f"{L1[0:2] = }")
print(f"{L1[0:3] = }")
print(f"{L1[0:4] = }")
print(f"{L1[0:5] = }")
print(f"{L1[0:6] = }")
print(f"{L1[0:7] = }")
print(f"{L1[:] = }")
print(f"{L1[::] = }")
print(L1)

print()

# Reverse Index Slicing

print(f"{L1[-6::-1] = }")
print(f"{L1[-5::-1] = }")
print(f"{L1[-4::-1] = }")
print(f"{L1[-3::-1] = }")
print(f"{L1[-2::-1] = }")
print(f"{L1[-1::-1] = }")

print()
# Forward listing with negative index

print(f"{L1[-6:] = }")
print(f"{L1[-6:-1] = }")
print(f"{L1[-6:-2] = }")
print(f"{L1[-6:-3] = }")
print(f"{L1[-6:-4] = }")
print(f"{L1[-6:-5] = }")

print()

# Forward listing using step values

print(f"{L1[::2] = }")
print(f"{L1[1::2] = }")

print()
# Reverse Listing using step values

print(L1)
print(f"{L1[::-1] = }")
print(f"{L1[-2::-2] = }")
