def search(a,key,low,high):
    if low>high:
        return False
    mid = (low + high)//2
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return search(a,key,low,mid-1)
    else:
        return search(a,key,mid+1,high)

if __name__ == '__main__':
    a = [1,14,23,47,55,67,81,88,90,97]
    ret = search(a,92,1,10)
    print("索引为%s,key为%s"%(ret,a[ret]))