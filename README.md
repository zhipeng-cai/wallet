TODO

0. install pyqt5 and sqlite3

1. 数据库表设计，现在只是GPT简单生成的，目前用户使用username作为key，按照题目要求每个用户可以有多个邮箱，电话，银行账户

2. 参考main.py, mainwindow.py已有代码的样子来编写按钮点击的处理逻辑（数据库读写），所有的按钮点击后都会触发事件，查询或者更改数据库，编写对应的回调函数来处理这部分逻辑，输入信息可以获取文本框这种组件的值，读取数据库后的数据可以先print()到终端，后面我修改成弹出一个子窗口来显示查询到的新数据