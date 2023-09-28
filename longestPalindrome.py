string = 'abdccdceeebebc'

def longestPalindrome(string):
    hmap = {}
    count = 0

    for n in string:
        hmap[n] = 1 + hmap.get(n,0)
        count +=1
    
    for n in hmap:
        if hmap.get(n) == 1:
            hmap[n] = 0
        elif hmap.get(n)%2 == 0:
            hmap[n]
        else:
            hmap[n] = hmap.get(n) - 1
    sum = 0
    for n in hmap:
        sum += hmap.get(n)
    if len(string) > sum:
        sum +=1
    else:
        sum
    return sum

print(longestPalindrome(string))
    