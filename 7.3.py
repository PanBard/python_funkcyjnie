
def search_list(srch_list,start,end,target):
    if start > end:
        print("start>end")
        return False

    x = (start + end)//2

    if srch_list[x] == target:
        print(f"Target: {target} found on position {x}")

    if srch_list[x] < target: return search_list(srch_list , x+1 , end , target)
    if srch_list[x] > target: return search_list(srch_list , start , x-1 , target)

def main():

    list_1 = [12,23,434,11234,124,3214,123,23,142,15,2,3,4,5,6,5,4,3,22,2]
    print(list_1)
    sort_list = list_1.copy()
    sort_list.sort()
    print(sort_list)

    target = 4
    search_list(sort_list,0,len(sort_list)-1,target)

if __name__ == '__main__':
    main()

