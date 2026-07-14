def infinite_soda():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refil = infinite_soda()

for _ in range(10):
    print(next(refil))