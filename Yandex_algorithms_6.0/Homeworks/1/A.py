x1, y1, x2, y2, x, y = [int(input()) for i in range(6)]

if x < x1:
    if y > y2:
        print("NW")
    elif (y < y1):
        print("SW")
    else:
        print("W")
elif x > x2:
    if y > y2:
        print("NE")
    elif y < y1:
        print("SE")
    else:
        print("E")
elif y > y2:
    print("N")
else:
    print("S")

# def f(x1, y1, x2, y2, x, y):
#     if x<x1:
#         if y > y2:
#             return "NW"
#         elif (y<y1):
#             return "SW"
#         else:
#             return "W"
#     elif x > x2:
#         if y > y2:
#             return "NE"
#         elif y < y1:
#             return "SE"
#         else:
#             return "E"
#     elif y > y2:
#         return "N"
#     else:
#         return "S"

# if f(-1,-2,5,3,-4,6) == "NW":
#     print("Success 1")

# if f(0,0,2,2,1,-1) == "S":
#     print("Success 2")

# if f(0,0,2,2,1,3) == "N":
#     print("Success 3")

# if f(0,0,2,2,3,0) == "E":
#     print("Success 4")

# if f(0,0,2,2,-3,0) == "W":
#     print("Success 5")

# if f(0,0,2,2,-5,-6) == "SW":
#     print("Success 6")

# if f(0,0,2,2,5,6) == "NE":
#     print("Success 7")

# if f(0,0,2,2,5,-6) == "SE":
#     print("Success 8")
