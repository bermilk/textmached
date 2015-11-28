def create_match_table(p):
    d = {}
    for a,b in reversed(list(enumerate(p))):

        if d.has_key(b):
            d[b].append(a)
        else:
            d[b] = [a]
    return d

def search(s, p):                       # search(String, Pattern)
    matches = []
    m_table = create_match_table(p)

        # shifts is a list of ordered pairs.
        # first element in the ordered pair is the pos in s to which the shift length is to be added,
        # the second element is the shift length for the matching char.
    shifts = []                         
    p_length = len(p)               
    p_end    = len(p) - 1               # pos of last character in pattern

    i = j = p_end                       # i -> current char in s
                                            # j -> current char in p
    k = i  

    while i < len(s):

        if s[i] == p[j]:
            if j > 0:                   # see if previous chars match too
                i -= 1
                j -= 1
            elif j == 0:                # a match is found!
                matches.append(i)
                if shifts:
                    i = sum(shifts.pop())
                else:
                    i = k + 1

                k = i    
                j = p_end
        else:
                # shift lengths are only calculated for chars that are before j.
            if m_table.has_key(s[i]):
                for mpos in m_table[s[i]]:
                    if mpos < j:
                            # shifts => [(pos, shift_length), ...]
                        shifts.insert(0, (k, p_end - mpos))

            if shifts:
                i = sum(shifts.pop())
            else:
                i = k + p_end
            k = i
            j = p_end


    return matches    
def radixsort(a):
    "sort list of integers using base-10 radix sort"

    if a:
        bins = [ [],[],[],[],[],[],[],[],[],[] ]
        m = max(a)
        r = 1
        while m > r:
            for e in a:
                bins[(e/r)%10].append(e)
            r = r * 10
            a = []
            for i in range(10):
                a.extend(bins[i])
                bins[i] = []
    return a
def main():
    p=open('product.txt')
    product = p.readlines()
    s=[i.split('\n',1)[0] for i in product]
    p=raw_input("Product Search - Input your keyword: ")
    while(1):
        
        key=p.split()
        for i in range(0,len(s)):
            x=search(s[i],key[0])
            y=search(s[i],key[1])
            if x!=[] or y !=[] :
                if x!=[] and y !=[] :
                    print s[i],'[2:0:0]'
                else:
                    print s[i],'[1:0:0]'
        p=raw_input("\nProduct Search - Input your keyword [Q to exit]: ")
        if p=='Q':
            return
if __name__ == "__main__":
    main()
