def insertion(N, M, i, j):
    mask = 2**(i-j+1) - 1
    mask = ~(mask << i)
    return (mask & N) | (M << i)

def bin_to_str(i):
    if not 0<=i<1:
        return False
    string = "."
    base = 0.5
    while i>0:
        if len(string)>32:
            return False
        elif i>base:
            string += "1"
            i -=base
        else:
            string += "0"
    return string

def flip_bit(i):
    sequence = [0, 0, 0]
    max_seq = 1
    target = 0
    while i!=0:
        if i&1!=target:
            if target==1:
                max_seq = max(max_seq, get_max(sequence))
            target = i&1
            sequence[2]=sequence[1]
            sequence[1]=sequence[0]
            sequence[0]=1
        i>>=1
    if target==0:
        sequence[2]=sequence[1]
        sequence[1]=sequence[0]
        sequence[0]=1
    return max(max_seq, get_max(sequence))

def get_max(arr):
    if arr[1]==1:
        return arr[0] + arr[2] + 1
    elif arr[1]==0:
        return max(arr[0], arr[2])
    else:
        return max(arr[0], arr[2]) + 1

def get_next(i):
    trailing_zeros = 0
    trailing_ones = 0
    temp = i
    while temp&1==0:
        trailing_zeros+=1
        temp>>=1
    while temp&1==1:
        trailing_ones+=1
        temp>>=1
    i|= (1<< (trailing_ones + trailing_zeros))
    i&= ~((1<< (trailing_ones + trailing_zeros))-1)
    i|= (1<<trailing_ones-1)-1
    return i

def get_prev(i):
    trailing_zeros = 0
    trailing_ones = 0
    temp = i
    while temp&1==1:
        trailing_ones+=1
        temp>>=1
    while temp&1==0:
        trailing_zeros+=1
        temp>>=1
    i&= (~(1<<trailing_zeros + trailing_ones))
    i&= ~((1<< (trailing_ones + trailing_zeros))-1)
    i|= ((1<<(trailing_ones+1))-1) << (trailing_zeros-1)

def conversion(a, b):
    final = a^b
    bits = 0
    while final!=0:
        if final&1==1:
            bit+=1
        final>>=1

def pairwise_swap(i):
    mask = 0
    while i!=0:
        mask = (mask*4)+2
        i>>=2
    return (i&mask)>>1 | (i&mask<<1)>>1
