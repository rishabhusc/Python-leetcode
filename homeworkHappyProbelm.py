'''
I don\'t think this is dp, but rather greedy.' \
\n\n
Find the first index where happy[idx] - happy[0] >= threshold.\n\nthen the answer is (idx + 1) / 2 + 1.
'''
happy=[1,2,3,5]
threshold=5
for i in range(1,len(happy)):
    if happy[i]-happy[0]>=threshold:
        print((i+1)//2+1)
        break
print(len(happy))
