# 第一个 Django 应用:投票应用

- 一个让人们查看和投票的公共站点

- 一个让你能添加、修改和删除投票的管理站点

## 1.创建项目

- 打开命令行，cd 到一个你想放置你代码的目录，然后运行以下命令

- django-admin startproject mysite

        mysite/
            manage.py
            mysite/
                __init__.py
                settings.py
                urls.py
                wsgi.py

- mysite/ 根目录只是你项目的容器， Django 不关心它的名字，你可以将它重命名为任何你喜欢的名字

- manage.py: 一个让你用各种方式管理 Django 项目的命令行工具

- 里面一层的 mysite/ 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 mysite.urls).

- mysite/__init__.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。

- mysite/settings.py：Django 项目的配置文件。

- mysite/urls.py：Django 项目的 URL 声明，就像你网站的“目录”。

- mysite/wsgi.py：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。


## 2.测试启动

- python manage.py runserver

- 如果要向别的电脑展示或者更换测试端口：python manage.py runserver 0:8000

- 0 是 0.0.0.0 的简写。


## 3.创建投票应用

- 在 Django 中，每一个应用都是一个 Python 包，并且遵循着相同的约定。Django 自带一个工具，可以帮你生成应用的基础目录结构，这样你就能专心写代码，而不是创建目录了。

- 创建应用：python manage.py startapp polls

- polls目录结构
      polls/
          __init__.py
          admin.py
          apps.py
          migrations/
              __init__.py
          models.py
          tests.py
          views.py


## 4.编写第一个视图

- 打开 polls/views.py
      from django.http import HttpResponse
      def index(request):
          return HttpResponse("Hello, world. You're at the polls index.")

- 如果想看见效果，我们需要将一个 URL 映射到它

- 在 polls 目录里新建一个 urls.py 文件

      from django.urls import path
      from . import views
      urlpatterns = [
          path('',views.index),
      ]

- 下一步是要在根 URLconf 文件中指定我们创建的 polls.urls 模块

- 在 mysite/urls.py 文件的 urlpatterns 列表里插入一个 include()

- path('polls/', include('polls.urls')),

#### 测试
- python manage.py runserver

- 浏览器访问 http://localhost:8000/polls/ 看到"Hello, world. You're at the polls index."


---

# 第二部分

## 1.数据库配置

- 打开 mysite/settings.py

- 默认sqlite无需配置

- 通常， INSTALLED_APPS 默认包括了以下 Django 的自带应用

  - django.contrib.admin -- 管理员站点， 你很快就会使用它。

  - django.contrib.auth -- 认证授权系统。

  - django.contrib.contenttypes -- 内容类型框架。

  - django.contrib.sessions -- 会话框架。

  - django.contrib.messages -- 消息框架。

  - django.contrib.staticfiles -- 管理静态文件的框架。

- 默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。python manage.py migrate

## 2.创建模型

- 模型是真实数据的简单明确的描述。它包含了储存的数据所必要的字段和行为。

- 在这个简单的投票应用中，需要创建两个模型：问题 Question 和选项 Choice。Question 模型包括问题描述和发布时间。Choice 模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。

      编辑 polls/models.py 文件
      class Question(models.Model):
          question_text = models.CharField(max_length=200)
          pub_date = models.DateTimeField('date published')
      class Choice(models.Model):
          question = models.ForeignKey(Question, on_delete=models.CASCADE)
          choice_text = models.CharField(max_length=200)
          votes = models.IntegerField(default=0)

## 3.激活模型

- 首先得把 polls 应用安装到我们的项目里
  - 我们需要在配置类 INSTALLED_APPS 中添加设置

- 接着执行生成迁移和迁移操作
  - python manage.py makemigrations polls
  -
