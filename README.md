# 环境配置及功能模块说明

## 项目环境

Python3.11.6

Windows11

Pycharm2022.3.3专业版

VSCODE

NODE.JS 12

Mysql8

后端框架：Flask

## 后端环境配置

**请确保进行此步骤前，配置好python、Pycharm编辑器与mysql8的环境**
打开Pycharm，打开项目，设置项目解释器为Python3.11.6
在pycharm中打开终端(Ternimal)输入来安装依赖

```python
pip install -r requirements.txt
```

安装依赖完成后，在app/config.py中修改数据库连接配置：

![image-20240224063330956](http://sapic.lyh27.top/static/upload/admin/image-20240224063330956.png)

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://你的mysql用户名:你的mysql密码@127.0.0.1/" + DATABASE
```

在app/controller/back_food_controller.py中修改数据库连接配置:

![image-20240216173927117](http://sapic.lyh27.top/static/upload/admin/image-20240216173927117.png)

使用Navicat等数据库管理工具，创建数据库：

![image-20240210204704510](http://sapic.lyh27.top/static/upload/admin/image-20240210204704510.png)

接着打开pycharm中的终端(terminal)，依次输入以下命令进行模型迁移:

```cmd
flask db init
flask db migrate
flask db upgrade
```

最后在pycharm中打开项目根目录下的run.py，如图点击运行按钮，开启后端服务

![image-20240209215020743](http://sapic.lyh27.top/static/upload/admin/image-20240209215020743.png)

后端接口地址：127.0.0.1:5000/

## 前端环境配置

打开VSCODE，在VSCODE中打开前端项目文件夹，接着，在界面最上方点击终端，选择新建终端，如图

![](http://sapic.lyh27.top/static/upload/admin/image-20240210210440741.png)

在打开的终端内，依次输入以下命令

```shell
清除缓存
npm cache clean --force
执行命令取消ssl验证
npm config set strict-ssl false
设置新镜像源
npm config set registry https://registry.npmmirror.com/
安装
npm install
运行
npm run serve
```

前端运行地址：127.0.0.1:8080/

## 模块介绍

### 用户注册登录模块

第一次启动项目，数据库中没有数据，需要注册一个管理员用户。进入前端页面，如图所示进行注册：

![image-20240210205426538](http://sapic.lyh27.top/static/upload/admin/image-20240210205426538.png)

![image-20240210205906408](http://sapic.lyh27.top/static/upload/admin/image-20240210205906408.png)

**最后到后台中，将刚注册的账号设置为管理员，将food_userinfo表中is_admin字段值，修改为1即可，如图所示**

![image-20240210210148079](http://sapic.lyh27.top/static/upload/admin/image-20240210210148079.png)

返回前端页面，使用刚才注册的管理员账号进行登录

![image-20240210210736225](http://sapic.lyh27.top/static/upload/admin/image-20240210210736225.png)

## 美食后台管理

使用管理员账号登录后，点击进入管理员后台

![image-20240210210935955](http://sapic.lyh27.top/static/upload/admin/image-20240210210935955.png)

![image-20240210210946371](http://sapic.lyh27.top/static/upload/admin/image-20240210210946371.png)

### 美食在线爬取及数据导入数据库

进入”美食数据管理“模块中的“美食数据与爬取”，点击开始爬虫，自动与后端建立websocket连接，前端页面显示爬虫的实时爬取信息状态

![image-20240210211552363](http://sapic.lyh27.top/static/upload/admin/image-20240210211552363.png)

![image-20240210211640932](http://sapic.lyh27.top/static/upload/admin/image-20240210211640932.png)

点击停止爬虫，关闭websocket，**想要停止爬虫的时候，一定要点击停止爬虫，稍等几秒弹出等待提示框，一定不要切换页面，如果切换了页面，爬虫程序是依然在后台运行的，会影响其他模块。**

![image-20240210211733465](http://sapic.lyh27.top/static/upload/admin/image-20240210211733465.png)

**注意：由于其他模块的数据都依赖于此功能模块，务必保证爬虫完整运行，最好不要中途停止，否则影响数据预处理及数据导入数据库，**

爬虫爬取美食数据完毕后，点击数据库导入按钮，将爬下来的数据自动写入到数据库当中（为防止重复导入数据，默认情况下数据库导入按钮点击一次变为不可再次点击，需要刷新页面进行重置按钮状态）

![image-20240210211938619](http://sapic.lyh27.top/static/upload/admin/image-20240210211938619.png)

**数据导入如果重复点击，数据库中将会出现重复的美食数据**

### 数据统计与分析

(部分数据的数据分析可视化结果)

![image-20240210212147694](http://sapic.lyh27.top/static/upload/admin/image-20240210212147694.png)

### 用户管理模块

![image-20240210212317054](http://sapic.lyh27.top/static/upload/admin/image-20240210212317054.png)

![image-20240210212331575](http://sapic.lyh27.top/static/upload/admin/image-20240210212331575.png)

### 美食管理模块

![image-20240210212510468](http://sapic.lyh27.top/static/upload/admin/image-20240210212510468.png)

![image-20240210212558476](http://sapic.lyh27.top/static/upload/admin/image-20240210212558476.png)

### 公告管理模块

![image-20240210213649504](http://sapic.lyh27.top/static/upload/admin/image-20240210213649504.png)

![image-20240210213730970](http://sapic.lyh27.top/static/upload/admin/image-20240210213730970.png)

![image-20240210213658364](http://sapic.lyh27.top/static/upload/admin/image-20240210213658364.png)

![image-20240210213711609](http://sapic.lyh27.top/static/upload/admin/image-20240210213711609.png)

## 美食前台页面

![美食分析系统](http://sapic.lyh27.top/static/upload/admin/%E7%BE%8E%E9%A3%9F%E5%88%86%E6%9E%90%E7%B3%BB%E7%BB%9F.png)

![1](http://sapic.lyh27.top/static/upload/admin/1.png)

![2](http://sapic.lyh27.top/static/upload/admin/2.png)

![3](http://sapic.lyh27.top/static/upload/admin/3.png)
