requests = [
    (1, 4, "1"),
    (1, 2, "2"),
    (2, 3, "3"),
    (3, 5, "4"),
    (3, 4, "5"),
    (4, 5, "6")
]

sorted_requests = sorted(requests, key=lambda x: x[1])

selected_requests = []
last = 0

for start, end, num in sorted_requests:
    if start >= last:
        selected_requests.append((start, end, num))
        last = end


for s, e, num in selected_requests:
    print(f"Заявка номер {num}: Старт:{s}, Конец:{e}")