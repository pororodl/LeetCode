if __name__ == '__main__':
    output = 0
    i=0
    j=0
    s = 'abcabcbb'
    store = set()
    while i<len(s) and j<len(s):
        print('while')
        if not s[j] in store:
            print('if')
            store.add(s[j])
            print(store)
            j=j+1
            output = max(output,j-i)
        else:
            store.remove(s[i])
            i=i+1
    print(output)