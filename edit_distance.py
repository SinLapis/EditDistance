__author__ = 'SinLapis'

WEIGHT_DELETION = 1
WEIGHT_INSERTION = 0.1
WEIGHT_REPLACEMENT = 1

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
        return WEIGHT_REPLACEMENT

def main(str_simple, str_full):
    len1 = len(str_simple)
    len2 = len(str_full)
    if len1 == 0 and len2 == 0:
        return 0
    if len1 == 0 and len2 > 0:
        return len2 * WEIGHT_INSERTION
    if len2 == 0 and len1 > 0:
        return len1 * WEIGHT_DELETION
    if len1 > 0 and len2 > 0 :
        return min([main(str_simple[0: -1], str_full) + 1,
            main(str_simple, str_full[0: -1]) + 1,
            main(str_simple[0: -1], str_full[0: -1]) +
                last_one(str_simple, str_full)])

if __name__ == '__main__':
    str_simple = input('str_simple:')
    str_full = input('str_full:')
    print(main(str_simple, str_full))
