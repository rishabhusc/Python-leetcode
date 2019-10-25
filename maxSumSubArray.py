ls=[12,3,4,2,7,-20,-10,40]
max_sum_seek=-1
max_value=0
for i in range(len(ls)):
    max_value+=ls[i]
    if max_sum_seek<max_value:
        max_sum_seek=max_value
    if max_value<0:
        max_value=0

print(max_sum_seek)