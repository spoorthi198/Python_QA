def check_even_odd(list1):
    even_num = []
    for i in (list1):
        if i%2 == 0:
            even_num.append(i)
        else:
            pass

    return even_num


res= check_even_odd ([12,3,45,6,8,90,65])
print("even num found are", res)




