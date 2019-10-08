'''
def ack(m,n):
    if m == 0:
        return n+1
    if m>0 and n==0:
        return ack(m-1,1)
    if m>0 and n>0:
        return ack(m-1,ack(m,n-1))
        
print ack(100,200)
'''
cache = {}

def ack(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1,1)
    try:
        return cache[m,n]
    except KeyError:
        cache[m,n] = ack(m-1, ack(m,n-1))
        return cache[m,n]
        
print ack(3,4)
print ack(23,40)