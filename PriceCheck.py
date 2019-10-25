'''


Different Product Prices

'''

product=["egg","milk","chease"]
productPrices=[2.89,3.29,5.79]
productsold=["egg","egg","chease","milk"]
prices=[2.89,2.99,5.97,3.29]
d={}
for i in range(len(product)):
    d[product[i]]=productPrices[i]
x={}
for i in range(len(productsold)):
    x[productsold[i]]=prices[i]
count=0
for k,v in x.items():
    if d[k]!=v:
        count+=1
print(count)

