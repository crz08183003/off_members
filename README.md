# -flask-web-# flyingstudio-off_member

# 本地预览
> 依次按以下命令执行

``` stylus
// 创建虚拟环境
$ virtualenv venv
//进入venv\Scripts目录 激活虚拟环境
$ activate
//安装依赖包
(venv)$ pip install -r requirements.txt
//进入off_member目录
$ python manager.py runserver
```
> 等待本地浏览页面

# 添加管理员

``` stylus
(venv)$ python manager.py shell
//生成数据库
$ db.create_all()
//创建管理员,admin属性一定要设置为True,stu_number要求8位以上
$ admin=User(name='icbtbo',stu_number='21315452',password='123',admin=True)
$ db.session.add(admin)
$ db.session.commit()
```

# 添加组别，会议类型

``` stylus
(venv)$ python manager.py shell
//添加组别
$ group = Grouptype(group='后端组')
$ db.session.add(group)
$ db.session.commit()
//添加会议类型
$ meeting = Meetingtype(group='后端组')
$ db.session.add(meeting)
$ db.session.commit()

```

# 导入用户数据
- 从excel文件中导入
- 所选文件需重命名为 users.xlsx
- 所选文件放在根目录下

操作命令：

``` stylus
(venv)$ python manager.py shell
//执行导入数据函数
$ read_excel()
```
