marks=[95,98,97,"utpal"]
print(marks)

print(marks[1])

#dricresing
print(marks[-1])

#0 to (2-1) projonto print korbe
print(marks[0:2])

for u in marks:
    print(u)

marks.append(99)
print(marks)

marks.insert(0,77)
print(marks)

#find element
print(77 in marks)

#find length
print(len(marks))

i=0
while(i<len(marks)):
    print(marks[i])
    i+=1

#marks.clear()
#print(marks)

#break & Continue Statement
for ut in marks:
    if ut==97:
        break
    print(ut)

for ut in marks:
    if ut==97:
        continue
    print(ut)