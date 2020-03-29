"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
"""
import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len:验证码的长度默认为4个字符
    :return:由大小写英文字母和数字构成的随机验证码
    """
    all_chars ='1234567890zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return '验证码为:' + code

    # 调用函数
code = generate_code(6)
print(code)