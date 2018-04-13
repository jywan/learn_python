def countfeq(s):
    d = {}
    s_list = s.split('/')
    [s_list.remove(item) for item in s_list if item in ',.']
    for word in s_list:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

if __name__ == "__main__":
   s = input()
   s_dict = countfeq(s)
   print(len(s_dict.keys()))