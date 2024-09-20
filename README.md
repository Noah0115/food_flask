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

<img src="https://immich.lyh27.top/api/assets/ecc02a90-359d-46bd-a59d-b3e447b4c19f/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240224063330956" />

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://你的mysql用户名:你的mysql密码@127.0.0.1/" + DATABASE
```

在app/controller/back_food_controller.py中修改数据库连接配置:

<img src="https://immich.lyh27.top/api/assets/c02e579c-bc0e-4141-a60f-a112ef590d11/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240216173927117" />

使用Navicat等数据库管理工具，创建数据库：

<img src="https://immich.lyh27.top/api/assets/63105134-93c1-4eb7-96f4-b22a2629daa5/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210204704510" />

接着打开pycharm中的终端(terminal)，依次输入以下命令进行模型迁移:

```cmd
flask db init
flask db migrate
flask db upgrade
```

最后在pycharm中打开项目根目录下的run.py，如图点击运行按钮，开启后端服务

<img src="https://immich.lyh27.top/api/assets/4b8ff3c2-6d89-419c-8757-aeced4bc0ab6/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240209215020743" />

后端接口地址：127.0.0.1:5000/

## 前端环境配置

打开VSCODE，在VSCODE中打开前端项目文件夹，接着，在界面最上方点击终端，选择新建终端，如图

<img src="https://immich.lyh27.top/api/assets/644e8aba-2903-4fa1-aee4-83740b40b96b/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" />

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

<img src="https://immich.lyh27.top/api/assets/84e5696e-478e-4f3c-a7e9-03e08d9c1c21/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210205426538" />

<img src="https://immich.lyh27.top/api/assets/76b859dc-13a0-48cf-812f-fd8e883f7649/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210205906408" />

**最后到后台中，将刚注册的账号设置为管理员，将food_userinfo表中is_admin字段值，修改为1即可，如图所示**

<img src="https://immich.lyh27.top/api/assets/69984ebd-0348-418d-94be-fa658fa667ad/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210210148079" />

返回前端页面，使用刚才注册的管理员账号进行登录

<img src="https://immich.lyh27.top/api/assets/a0659cc4-9a17-4d84-8fd0-ee8177c75fdf/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210210736225" />

## 美食后台管理

使用管理员账号登录后，点击进入管理员后台

<img src="https://immich.lyh27.top/api/assets/a490c89c-cac6-4433-9030-beecf0216d28/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210210935955" />

<img src="https://immich.lyh27.top/api/assets/c0c72d3f-ee9b-43b2-a6b2-c8fccad2ff59/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210210946371" />

### 美食在线爬取及数据导入数据库

进入”美食数据管理“模块中的“美食数据与爬取”，点击开始爬虫，自动与后端建立websocket连接，前端页面显示爬虫的实时爬取信息状态

<img src="https://immich.lyh27.top/api/assets/29345fa4-485a-4785-9e91-216496acac38/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210211552363" />

<img src="https://immich.lyh27.top/api/assets/97d47798-04af-413f-9d66-5d5b42ea1197/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210211640932" />

点击停止爬虫，关闭websocket，**想要停止爬虫的时候，一定要点击停止爬虫，稍等几秒弹出等待提示框，一定不要切换页面，如果切换了页面，爬虫程序是依然在后台运行的，会影响其他模块。**

<img src="https://immich.lyh27.top/api/assets/60a42c00-cdd2-4da3-9544-0e8eed078117/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210211733465" />

**注意：由于其他模块的数据都依赖于此功能模块，务必保证爬虫完整运行，最好不要中途停止，否则影响数据预处理及数据导入数据库，**

爬虫爬取美食数据完毕后，点击数据库导入按钮，将爬下来的数据自动写入到数据库当中（为防止重复导入数据，默认情况下数据库导入按钮点击一次变为不可再次点击，需要刷新页面进行重置按钮状态）

<img src="https://immich.lyh27.top/api/assets/9cc0cf85-6929-4a92-830c-7c6ddf2a3a05/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210211938619" />

**数据导入如果重复点击，数据库中将会出现重复的美食数据**

### 数据统计与分析

(部分数据的数据分析可视化结果)

<img src="https://immich.lyh27.top/api/assets/412b94f9-f95c-4ca7-8a99-1709c218bba9/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210212147694" />

### 用户管理模块

<img src="https://immich.lyh27.top/api/assets/1886f86c-eff3-4e58-a297-55b723596f11/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210212317054" />

<img src="https://immich.lyh27.top/api/assets/10d0524b-7b33-48d2-aca4-ce8790564055/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210212331575" />

### 美食管理模块

<img src="https://immich.lyh27.top/api/assets/b4dba485-21b8-4ab1-badf-68d847f3f2de/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210212510468" />

<img src="https://immich.lyh27.top/api/assets/4e854263-0fb9-42ac-b618-557692c63dfb/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210212558476" />

### 公告管理模块

<img src="https://immich.lyh27.top/api/assets/8b1d371b-7422-4fbd-ad40-011569b9e8b7/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210213649504" />

<img src="https://immich.lyh27.top/api/assets/223add4c-62b8-4e1c-a093-9a5549d1c21e/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210213730970" />

<img src="https://immich.lyh27.top/api/assets/7fa8eb20-de52-421a-a6ad-d4d1303ca617/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210213658364" />

<img src="https://immich.lyh27.top/api/assets/08a17fd0-5a9b-4211-ac1c-e0587fd46cff/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240210213711609" />

## 美食前台页面

<img src="https://immich.lyh27.top/api/assets/4580ca64-d848-4125-afab-ad7783f78c53/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="美食分析系统" />

<img src="https://immich.lyh27.top/api/assets/4580ca64-d848-4125-afab-ad7783f78c53/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="1" />

<img src="https://immich.lyh27.top/api/assets/7b6938b4-ca89-4155-bf63-4742abded976/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="2" />


