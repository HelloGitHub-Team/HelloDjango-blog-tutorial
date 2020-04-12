

<p align="center">
  <img src="./cover.jpg"/>
  <br><strong>HelloDjango-blog-tutorial</strong><br>
  <strong>完全免费、开源的 HelloDjango 系列教程之博客开发</strong>。<br>
  基于 django 2.2，带你从零开始一步步创建属于自己的博客网站。
</p>


<p align="center">
  <a href="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png"><img src="https://img.shields.io/badge/Talk-%E5%BE%AE%E4%BF%A1%E7%BE%A4-brightgreen.svg?style=popout-square" alt="WeiXin"></a>
  <a href="https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial/stargazers"><img src="https://img.shields.io/github/stars/HelloGitHub-Team/HelloDjango-blog-tutorial.svg?style=popout-square" alt="GitHub stars"></a>
  <a href="https://weibo.com/hellogithub"><img src="https://img.shields.io/badge/%E6%96%B0%E6%B5%AA-Weibo-red.svg?style=popout-square" alt="Sina Weibo"></a>
</p>

**特别说明**：本项目不仅仅是教程用的演示项目！我们的目标是开发一个功能完善、测试充分、可用于生产环境的开源博客系统。和其他开源博客系统不同点在于，我们以教程的形式详细记录项目从 0 到 1 的开发过程。

## 分支说明

master 分支为项目的主分支，每一步关键功能的开发都对应一篇详细的教程，并和历史提交以及标签一一对应。例如第一篇教程对应第一个 commit，对应标签为 step1，依次类推。

## 资源列表

- [成品在线预览](https://hellodjango-blog-tutorial-demo.zmrenwu.com/)
- 教程首发 HelloGitHub 微信公众号和 [追梦人物的博客](https://www.zmrenwu.com/)，在线学习地址：[HelloDjango - Django博客教程（第二版）](https://zmrenwu.com/courses/hellodjango-blog-tutorial/)
- 项目 [源码仓库](https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial)
- 项目 [前端模板源码仓库](https://github.com/zmrenwu/django-blog-tutorial-templates)

## 本地运行

可以使用 Virtualenv、Pipenv、Docker 等在本地运行项目，每种方式都只需运行简单的几条命令就可以了。

> **注意：**
>
> 因为博客全文搜索功能依赖 Elasticsearch 服务，如果使用 Virtualenv 或者 Pipenv 启动项目而不想搭建 Elasticsearch 服务的话，请先设置环境变量 `ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no` 以关闭实时索引，否则无法创建博客文章。如果关闭实时索引，全文搜索功能将不可用。
>
> Windows 设置环境变量的方式：`set ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no`
>
> Linux 或者 macOS：`export ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no`
>
> 使用 Docker 启动则无需设置，因为会自动启动一个包含 Elasticsearch 服务的 Docker 容器。

无论采用何种方式，先克隆代码到本地：

```bash
$ git clone https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial.git
```

### Virtualenv

1. 创建虚拟环境并激活虚拟环境，具体方法可参考：[开始进入 django 开发之旅：使用虚拟环境](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/59/#%E4%BD%BF%E7%94%A8%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)

2. 安装项目依赖

   ```bash
   $ cd HelloDjango-blog-tutorial
   $ pip install -r requirements.txt
   ```

3. 迁移数据库

   ```bash
   $ python manage.py migrate
   ```

4. 创建后台管理员账户

   ```bash
   $ python manage.py createsuperuser
   ```

   具体请参阅 [创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

5. 运行开发服务器

   ```bash
   $ python manage.py runserver
   ```

6. 浏览器访问 http://127.0.0.1:8000/admin，使用第 4 步创建的管理员账户登录后台发布文章，如何发布文章可参考：[创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

   或者执行 fake 脚本批量生成测试数据：

   ```bash
   $ python -m scripts.fake
   ```

   > 批量脚本会清除全部已有数据，包括第 4 步创建的后台管理员账户。脚本会再默认生成一个管理员账户，用户名和密码都是 admin。

9. 浏览器访问：http://127.0.0.1:8000，可进入到博客首页

### Pipenv

1. 安装 Pipenv（已安装可跳过）

    ```bash
    $ pip install pipenv
    ```

2. 安装项目依赖

    ```bash
    $ cd HelloDjango-blog-tutorial
    $ pipenv install --dev
    ```

    关于如何使用 Pipenv，参阅：[开始进入 django 开发之旅](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/59/) 的 Pipenv 创建和管理虚拟环境部分。

3. 迁移数据库

    在项目根目录运行如下命令迁移数据库：
    ```bash
    $ pipenv run python manage.py migrate
    ```

4. 创建后台管理员账户

   在项目根目录运行如下命令创建后台管理员账户
   
   ```bash
   $ pipenv run python manage.py createsuperuser
   ```

   具体请参阅 [创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

5. 运行开发服务器

   在项目根目录运行如下命令开启开发服务器：

   ```bash
   $ pipenv run python manage.py runserver
   ```

6. 浏览器访问 http://127.0.0.1:8000/admin，使用第 4 步创建的管理员账户登录后台发布文章，如何发布文章可参考：[创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

   或者执行 fake 脚本批量生成测试数据：

   ```bash
   $ pipenv run python -m scripts.fake
   ```

   > 批量脚本会清除全部已有数据，包括第 4 步创建的后台管理员账户。脚本会再默认生成一个管理员账户，用户名和密码都是 admin。

7. 在浏览器访问：http://127.0.0.1:8000/，可进入到博客首页。

### Docker

1. 安装 Docker 和 Docker Compose

3. 构建和启动容器

   ```bash
   $ docker-compose -f local.yml build
   $ docker-compose -f local.yml up
   ```

4. 创建后台管理员账户

   ```bash
   $ docker exec -it hellodjango_blog_tutorial_local python manage.py createsuperuser
   ```

   其中 hellodjango_blog_tutorial_local 为项目预定义容器名。

4. 浏览器访问 http://127.0.0.1:8000/admin，使用第 3 步创建的管理员账户登录后台发布文章，如何发布文章可参考：[创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

   或者执行 fake 脚本批量生成测试数据：

   ```bash
   $ docker exec -it hellodjango_blog_tutorial_local python -m scripts.fake
   ```

   >  批量脚本会清除全部已有数据，包括第 3 步创建的后台管理员账户。脚本会再默认生成一个管理员账户，用户名和密码都是 admin。

5. 为 fake 脚本生成的博客文章创建索引，这样就可以使用 Elasticsearch 服务搜索文章

   ```bash
   $ docker exec -it hellodjango_blog_tutorial_local python manage.py rebuild_index
   ```

   > 通过 admin 后台添加的文章会自动创建索引。

6. 在浏览器访问：http://127.0.0.1:8000/，可进入到博客首页。

### 线上部署

线上部署的详细文档请参考下方教程目录索引中的 **部署篇** 部分，如果不想了解细节或已了解细节，使用 Docker 仅需以下几个简单步骤就可以上线运行：

> **小贴士：**
>
> 国内服务器请设置好镜像加速，否则 Docker 构建容器的过程会非常缓慢！具体可参考 **部署篇** Docker 部署 django 中线上部署部分的内容。

1. 克隆代码到服务器

   ```bash
   $ git clone https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial.git
   ```

2. 创建环境变量文件用于存放项目敏感信息

   ```bash
   $ cd HelloDjango-blog-tutorial
   $ mkdir .envs
   $ touch .envs/.production
   ```

3. 在 .production 文件写入下面的内容并保存

   ```
   # django 用于签名和加密等功能的密钥，泄露会严重降低网站的安全性
   # 推荐使用这个工具生成：https://miniwebtool.com/django-secret-key-generator/
   DJANGO_SECRET_KEY=0p72%e@r3qr$bq%%&bxj#_bem+na2t^0(#((fom6eewrg)gyb^
   
   # 设置 django 启动时加载的配置文件
   DJANGO_SETTINGS_MODULE=blogproject.settings.production
   ```

4. 修改 Nginx 配置：复制 compose/nginx/hellodjango-blog-tutorial.conf-tmpl 到同一目录，并重命名为 hellodjango-blog-tutorial.conf，修改第 6 行的 server_name 为自己的域名（如果没有域名就改为服务器的公网 ip 地址）

5. 启动容器

   ```bash
   $ docker-compose -f production.yml up --build -d
   ```

6. 执行 docker ps 检查容器启动状况，看到如下的 3 个容器说明启动成功：

   - hellodjango_blog_tutorial_nginx
   - hellodjango_blog_tutorial_elasticsearch
   - hellodjango_blog_tutorial

7. 配置 HTTPS 证书（没有配置域名无法配置，只能通过服务器 ip 以 HTTP 协议访问）

   ```bash
   $ docker exec -it hellodjango_blog_tutorial_nginx certbot --nginx -n --agree-tos --redirect --email email@hellodjango.com -d hellodjango-blog-tutorial-demo.zmrenwu.com
   ```

   解释一下各参数的含义：

   - --nginx，使用 Nginx 插件
   - -n 非交互式，否则会弹出询问框
   - --redirect，自动配置 Nginx，将所有 http 请求都重定向到 https
   - --email xxx@xxx.com，替换为自己的 email，用于接收通知
   - -d 域名列表，开启 https 的域名，替换为自己的域名，多个域名用逗号分隔

8. 浏览器访问域名或者服务器 ip 即可进入博客首页

## 教程目录索引

**基础篇**

1. [开始进入 django 开发之旅](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/59/)
2. ["空空如也"的博客应用](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/60/)
3. [创建 Django 博客的数据库模型](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/61/)
4. [Django 迁移、操作数据库](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/62/)
5. [Django 的接客之道](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/63/)
6. [博客从“裸奔”到“有皮肤”](https://www.zmrenwu.com/courseqs/hellodjango-blog-tutorial/materials/64/)
7. [创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)
8. [开发博客文章详情页](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/66/)
9. [让博客支持 Markdown 语法和代码高亮](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/67/)
10. [Markdown 文章自动生成目录，提升阅读体验](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/68/)
11. [自动生成文章摘要](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/69/)
12. [页面侧边栏：使用自定义模板标签](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/70/)
13. [分类、归档和标签页](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/71/)
14. [交流的桥梁：评论功能](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/72/)
15. [优化博客功能细节，提升使用体验](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/73/)

**部署篇**

16. [Nginx+Gunicorn+Supervisor 部署 Django 博客应用](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/74/)
17. [使用 Fabric 自动化部署](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/75/)
18. [使用 Certbot 向 Let's Encrypt 免费申请 HTTPS 证书](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/76/)
19. [使用 Docker 让部署 Django 项目更加轻松](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/77/)

**进阶篇**

20. [开发博客文章阅读量统计功能](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/78/)
21. [Django 官方推荐的姿势：类视图](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/79/)
22. [在脚本中使用 ORM：Faker 批量生成测试数据](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/80/)
23. [通过 Django Pagination 实现简单分页](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/81/)
24. [稳定易用的 Django 分页库，完善分页功能](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/82/)
25. [统计各个分类和标签下的文章数](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/83/)
26. [开启 Django 博客的 RSS 功能](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/84/)
27. [Django 博客实现简单的全文搜索](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/85/)
28. [Django Haystack 全文检索与关键词高亮](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/86/)

**测试篇**

29. [单元测试：测试 blog 应用](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/87/)
30. [单元测试：测试评论应用](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/88/)
31. [Coverage.py 统计测试覆盖率](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/89/)

## 继续学习
有了以上的 django 基础，让我继续学习 [django REST framework 教程](https://www.zmrenwu.com/courses/django-rest-framework-tutorial/)

## 公众号
<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:70%;"><br>
欢迎关注 HelloGitHub 公众号，获取更多开源项目的资料和内容。
</p>


## QQ 群

加入 QQ 群和更多的 django 开发者进行交流：

Django学习小组主群：696899473

## 版权声明

<img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际 </a>进行许可。