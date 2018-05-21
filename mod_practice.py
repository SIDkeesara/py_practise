from ad import ad
import sub
import mul
import div

def add(*nums):
    total=0
    for a_num in nums:
        total += a_num
    return total


    
print(ad.ad(6,3))  
print(sub.sub(6,3))  
print(mul.mul(6,3))  
print(div.div(6,3))  
print(ad(3,5))
