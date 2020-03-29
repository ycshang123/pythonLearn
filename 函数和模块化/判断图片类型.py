"""
判断一组文件中图片的个数
"""
def count_image(file_list):
    """
    判断一组文件中图片的个数
    :param file_list:文件列表
    :return:图片文件数
    """
    count =0
    for file in file_list:
        if file.endswith('png') or file.endswith('jpg') or \
            file.endswith('webp') or file.endswith('bnp'):
            count = count +1
    return count

    #调用函数
img_list = ['1.jpg','2.text','3.png','4.md','5.webp','6.pdf','7.bnp']
result = count_image(img_list)
print('一共有',result,'个图片')
    