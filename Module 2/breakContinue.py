count = 0
print("Continue")
for count in range(0, 10):
    if count < 5:
        continue
    print(count)

print("Break")
for count in range(0, 10):
    if count > 5:
        break
    print(count)
