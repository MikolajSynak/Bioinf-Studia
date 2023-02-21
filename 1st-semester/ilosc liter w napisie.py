from sys import*
n=input("podaj ilosc liczb: ")
k=0
#zrobione petla for
for m in n:
    if m=='a': k+=1
print("ilosc liter a w napisie: " , k)
#zrobione petla while
while i<len(n):
    if n[i]== 'a' : k+=1
    i+=1
    print("ilosc liter a w napisie: ", k)
#metoda count
print(n.count('a'))
