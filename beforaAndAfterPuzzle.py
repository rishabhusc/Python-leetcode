phrases = ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]


for i in range(len(phrases)):
    phrases[i]=phrases[i].split(" ")
d=set()
for i in range(len(phrases)):
    for j in range(i+1,len(phrases)):
        if phrases[i]==phrases[j]:
            continue
        if phrases[i][-1]==phrases[j][0]:
            d.add(' '.join(phrases[i] + phrases[j][1:]))
        if phrases[j][-1]==phrases[i][0]:
            d.add(' '.join(phrases[j] + phrases[i][1:]))
print(d)

["a chip off the old block party","a man on a mission impossible","a man on a mission statement","a quick bite to eat my words","chocolate bar of soap"]
{'chocolate bar of soap', 'a chip off the old block party', 'a man on a mission impossible', 'a quick bite to eat my words', 'a man on a mission statement'}
