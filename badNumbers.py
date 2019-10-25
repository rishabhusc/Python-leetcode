'''

Bad Numbers---

'''

low=-20
high=40
badNumbers = [3, 19, 21]
mx=-1
for i in range(len(badNumbers)-1):
    if mx<((badNumbers[i+1]-1)-badNumbers[i]):
        mx=((badNumbers[i+1]-1)-badNumbers[i])
if badNumbers[i]>low:
    if mx<(badNumbers[0]-1)-low:
        mx=badNumbers[0]-1-low
if badNumbers[len(badNumbers)-1]<high:
    if mx<high-badNumbers[len(badNumbers)-1]:
        mx=high-1-badNumbers[len(badNumbers)-1]
print(mx)
