#display future leap year from current year to final year?


from datetime import date
cy = date.today().year
fy = int(input("Enter the final year: "))
print(f"Leap years from ",cy," to" ,fy)
for i in range(cy, fy + 1):
    if (i % 4 == 0 and i % 4 != 100) or (i % 400 == 0):
        print(i)
