"""
pyecharts绘制柱状图
"""
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

from pyecharts import options as opts

#内置主题类型可查看 pyecharts.globals.ThemeType
#第一幅图
bar =(
    Bar(int_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(['服饰','箱包','鞋帽','电子','数码','户外'])
    .add_yaxis("京东",[5,23,32,12,54,90])
    .add_yaxis('天猫',[15,6,32,74,54,90])
    .set_global_opts(title_opts=opts.TitleOpts(title='电商销售对比'))
      )
bar.render(path='./电商销售对比.html')

#第二张图
items =['Java','C','Python','C++','JavaScript','C#','PHP','SQL']
data_list1 = [188,166,110,108,90,80,55,45]
data_list2 = [190,160,140,100,80,70,50,40]
bar1 =(Bar(init_opts= opts.InitOpts(theme=ThemeType.CHALK))
       .add_xaxis(items)
       .add_yaxis('2020年',data_list1)
       .add_yaxis("2019年",data_list2)
       .set_global_opts(title_opts=opts.TitleOpts(title='编程语言排行',subtitle='2019-2020'))
    )
bar1.render(path='./编程语言排行.html')
#第三张图
item =['互联网','房产','教育','计算机软件','餐饮','医疗','零售','加工制造','汽车','基金']
data_list3 =[10.94,8.82,5.86,4.48,3.53,3.34,3.17,3.06,3.05,2.84]
bar2 =(Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    .add_xaxis(item)
    .add_yaxis('求职Top10',data_list3)
    .set_global_opts(title_opts=opts.TitleOpts(title='向互联网产业投递简历的求职者当前从事行业TOP10'))
    )
bar2.render(path="./求职Top10.html")