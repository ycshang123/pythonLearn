"""
类和对象
"""
class Student(object):
    #_init_是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以问学生对象绑定name和age两个属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self,course_name):
        print('%s正在学习%s' % (self.name,course_name))

    # PEP 8要求标识符的名字全小写多个单词用下划线连接
    def watch_movie(self):
        if self.age <18:
            print('%s只能看《熊出没》.' % self.name)
        else:
            print('%s正在看3D大片.' % self.name)
    

def main():
    #创建学上对象并指定姓名和年龄
    stu1 = Student('张晨',28)
    #给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发消息
    stu1.watch_movie()
    stu2 = Student('王大锤',15)
    stu2.study('思想品德')
    stu2.watch_movie()

if __name__ == "__main__":
    main()