__author__ = 'SinLapis'

def min(num_list):
    min_num = num_list[0]
    for num in num_list:
        if min_num > num:
            min_num = num
    return num

def last_one(str1, str2):
    if str1[-1] == str2[-1]:
        return 0
    else:
        return 1

def main(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 == 0 and len2 == 0:
        return 0
    if len1 == 0 and len2 > 0:
        return len2
    if len2 == 0 and len1 > 0:
        return len1
    if len1 > 0 and len2 > 0 :
        return min([main(str1[0: -1], str2) + 1,
            main(str1, str2[0: -1]),
            main(str1[0: -1], str2[0: -1]) + last_one(str1, str2)])

if __name__ == '__main__':
    str1 = input('str1:')
    str2 = input('str2:')
    print(main(str1, str2))
