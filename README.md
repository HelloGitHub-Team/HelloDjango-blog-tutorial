

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/readme.gif"/>
  <br><strong>HelloDjango-blog-tutorial</strong><br>
  <strong>完全免费、开源的 HelloDjango 系列教程之博客开发</strong>。<br>
  基于 django 2.2，带你从零开始一步步创建属于自己的博客网站。
</p>

<p align="center">
  <a href="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png"><img src="https://img.shields.io/badge/Talk-%E5%BE%AE%E4%BF%A1%E7%BE%A4-brightgreen.svg?style=popout-square" alt="WeiXin"></a>
  <a href="https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial/stargazers"><img src="https://img.shields.io/github/stars/HelloGitHub-Team/HelloDjango-blog-tutorial.svg?style=popout-square" alt="GitHub stars"></a>
  <a href="https://weibo.com/hellogithub"><img src="https://img.shields.io/badge/%E6%96%B0%E6%B5%AA-Weibo-red.svg?style=popout-square" alt="Sina Weibo"></a>
</p>

## 分支说明

tutorial 分支为项目的主分支，每一篇教程的代码都和历史提交以及标签一一对应。

例如第一篇教程对应第一个 commit，对应标签为 step1，依次类推。

## 资源列表

- [在线演示](https://hellodjango-blog-tutorial-demo.zmrenwu.com/)
- 首发 HelloGitHub 微信公众号，博客同步更新：[HelloDjango - Django博客教程（第二版）](https://zmrenwu.com/courses/hellodjango-blog-tutorial/)
- 项目前端模板：[Blog templates](https://github.com/zmrenwu/django-blog-tutorial-templates)

## 本地运行

### Pipenv

1. **克隆项目到本地**

   ```
   git clone https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial.git
   ```
   
2. **安装 Pipenv（已安装跳过）**

   ```
   pip install pipenv
   ```
   
3. **安装项目依赖**

   ```
   cd HelloDjango-blog-tutorial
   pipenv install --dev
   ```
   
   > 关于如何使用 Pipenv，参阅：[开始进入 django 开发之旅](http://zmrenwu.com/post/3/) 的 Pipenv 创建和管理虚拟环境部分。

4. **迁移数据库**

   在项目根目录运行如下命令迁移数据库：
   ```
   pipenv run python manage.py migrate
   ```

5. **创建后台管理员账户**

   在项目根目录运行如下命令创建后台管理员账户
   
   ```
   pipenv run python manage.py createsuperuser
   ```

   具体请参阅 [创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

6. **运行开发服务器**

   在项目根目录运行如下命令开启开发服务器：

   ```
   pipenv run python manage.py runserver
   ```

   在浏览器访问：http://127.0.0.1:8000

7. **进入后台发布文章**

   在浏览器访问：http://127.0.0.1:8000/admin

   使用第 5 步创建的后台管理员账户登录后台。


### Docker

1. **安装 Docker 和 Docker Compose**

2. **克隆项目到本地**

   ```
   git clone https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial.git
   ```

3. **构建镜像和启动容器**

   ```
   docker-compose -f local.yml build
   docker-compose -f local.yml up
   ```

4. **创建后台管理员账户**

   ```
   docker exec -it hellodjango_blog_tutorial_local python manage.py createsuperuser
   ```

   其中 hellodjango_blog_tutorial_local 为项目预定义容器名

5. 进入后台发布文章

   在浏览器访问：http://127.0.0.1:8000/admin

   使用第 3 步创建的后台管理员账户登录

   具体请参阅 [创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

## 教程目录索引

**基础**

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
16. [Nginx+Gunicorn+Supervisor 部署 Django 博客应用](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/74/)
17. [使用 Fabric 自动化部署](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/75/)
18. [使用 Certbot 向 Let's Encrypt 免费申请 HTTPS 证书](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/76/)
19. [使用 Docker 让部署 Django 项目更加轻松](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/77/)
20. [开发博客文章阅读量统计功能](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/78/)
21. [Django 官方推荐的姿势：类视图](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/79/)
22. [在脚本中使用 ORM：Faker 批量生成测试数据](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/80/)
23. [通过 Django Pagination 实现简单分页](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/81/)
24. [稳定易用的 Django 分页库，完善分页功能](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/82/)
25. [统计各个分类和标签下的文章数](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/83/)
26. [开启 Django 博客的 RSS 功能](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/84/)
27. [Django 博客实现简单的全文搜索](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/85/)
28. [Django Haystack 全文检索与关键词高亮](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/86/)
29. [单元测试：测试 blog 应用](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/87/)
30. [单元测试：测试评论应用](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/88/)
31. [Coverage.py 统计测试覆盖率](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/89/)

## 公众号
<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:70%;"><br>
欢迎关注 HelloGitHub 公众号，获取更多开源项目的资料和内容。
</p>


## 声明
<img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际 </a>进行许可。