HANS_DIGIT = "零壹贰叁肆伍陆柒捌玖"
HANS_UNIT =  ['万', '仟', '佰', '拾', '亿', '仟', '佰', '拾', '万', '仟', '佰', '拾', '元整']
DECIMAL_UNIT = ['角', '分']

def int_to_words(amount) -> str:
    *amount_list, = str(amount)
    lth = len(amount_list)
    
    digits_in_words = map(lambda x : HANS_DIGIT[int(x)], amount_list)
    digits_in_words = list(digits_in_words)
    
    unit_in_words = HANS_UNIT[-lth:]
    
    res_zip = zip(digits_in_words, unit_in_words)
    res_str = "".join(list(map(lambda x : x[0] + x[1], res_zip)))
    
    # Remove unnecessary units
    res_str = res_str.replace('零拾', '零')
    res_str = res_str.replace('零佰', '零')
    res_str = res_str.replace('零仟', '零')
    res_str = res_str.replace('零万', '零')
    
    # Remove trailing zeros
    while '零零' in res_str:
        res_str = res_str.replace('零零', '零')
    
    # Remove unnecessary zero
    res_str = res_str.replace('零亿', '亿')
    res_str = res_str.replace('零元', '元')
    
    return res_str


def decimal_to_words(amount) -> str:
    raise NotImplementedError('Function decimal_to_words not implemented.')


def amount_to_words(amount) -> str:
    if '.' in str(amount):
        before, after = str(amount).split('.')
        
        before = int_to_words(before)
        after = decimal_to_words(after)
        
        res = before + after
    else:
        res = int_to_words(amount)
    return res