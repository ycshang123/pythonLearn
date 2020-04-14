"""
查找当前目录所有文件
"""
import os 
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts import options as opts
txt_numbers = 0
jpg_numbers = 0
html_numbers =0
def get_all(cwd):
    result = []
    #遍历当前目录，获取文件列表，
    get_dir = os.listdir(cwd)
    # print(get_dir)
    for i in get_dir:
        # 把第一步获取的文件夹加入路径，自己调试各个步骤结果
        # print(i)
        sub_dir = os.path.join(cwd,i)
        # print(sub_dir)
        #如果当前仍是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            #如果当前路径不是文件夹，则把文件名放入列表
            file_name = os.path.basename(sub_dir)
            if file_name.split(".")[-1] == "txt":
             global txt_numbers
             txt_numbers +=1
            elif file_name.split(".")[-1] == "jpg":
             global jpg_numbers
             jpg_numbers +=1
            elif file_name.split(".")[-1] == "html":
             global html_numbers
             html_numbers +=1
        print("以txt结尾的文件数为:",txt_numbers)
        print("以jpg结尾的文件数为:",jpg_numbers)
        print("以html结尾的文件数为",html_numbers)
      
        print("饼图绘制完成")
    return result

if __name__ == "__main__":
    # 获取当前目录
    cur_path = os.getcwd() + '/pythonLearn/res'
    print(cur_path)
    print('当前目录度所有文件',get_all(cur_path))
    item =['txt文件数','jpg文件数','html文件数']
    data_list =[txt_numbers,jpg_numbers,html_numbers]
    bar =(Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
        .add_xaxis(item)
        .add_yaxis('res文件数分布',data_list)
        .set_global_opts(title_opts=opts.TitleOpts('res各文件数文件汇总')))

    bar.render(path ='./pythonLearn/res/html/res文件汇总.html')
