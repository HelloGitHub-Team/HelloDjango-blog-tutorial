from datetime import timedelta

from django.apps import apps
from django.contrib.auth.models import User
from django.template import Context, Template
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from ..models import Category, Post, Tag
from ..templatetags.blog_extras import (
    show_archives,
    show_categories,
    show_recent_posts,
    show_tags,
)


class BlogExtrasTestCase(TestCase):
    def setUp(self):
        apps.get_app_config("haystack").signal_processor.teardown()
        self.user = User.objects.create_superuser(
            username="admin", email="admin@hellogithub.com", password="admin"
        )
        self.cate = Category.objects.create(name="测试")
        self.ctx = Context()

    def test_show_recent_posts_without_any_post(self):
        template = Template("{% load blog_extras %}" "{% show_recent_posts %}")
        expected_html = template.render(self.ctx)
        self.assertInHTML('<h3 class="widget-title">最新文章</h3>', expected_html)
        self.assertInHTML("暂无文章！", expected_html)

    def test_show_recent_posts_with_posts(self):
        post = Post.objects.create(
            title="测试标题", body="测试内容", category=self.cate, author=self.user,
        )
        context = Context(show_recent_posts(self.ctx))
        template = Template("{% load blog_extras %}" "{% show_recent_posts %}")
        expected_html = template.render(context)
        self.assertInHTML('<h3 class="widget-title">最新文章</h3>', expected_html)
        self.assertInHTML(
            '<a href="{}">{}</a>'.format(post.get_absolute_url(), post.title),
            expected_html,
        )

    def test_show_recent_posts_nums_specified(self):
        post_list = []
        for i in range(7):
            post = Post.objects.create(
                title="测试标题-{}".format(i),
                body="测试内容",
                category=self.cate,
                author=self.user,
            )
            post_list.insert(0, post)
        context = Context(show_recent_posts(self.ctx, 3))
        template = Template("{% load blog_extras %}" "{% show_recent_posts %}")
        expected_html = template.render(context)
        self.assertInHTML('<h3 class="widget-title">最新文章</h3>', expected_html)
        self.assertInHTML(
            '<a href="{}">{}</a>'.format(
                post_list[0].get_absolute_url(), post_list[0].title
            ),
            expected_html,
        )
        self.assertInHTML(
            '<a href="{}">{}</a>'.format(
                post_list[1].get_absolute_url(), post_list[1].title
            ),
            expected_html,
        )
        self.assertInHTML(
            '<a href="{}">{}</a>'.format(
                post_list[2].get_absolute_url(), post_list[2].title
            ),
            expected_html,
        )

    def test_show_categories_without_any_category(self):
        self.cate.delete()
        context = Context(show_categories(self.ctx))
        template = Template("{% load blog_extras %}" "{% show_categories %}")
        expected_html = template.render(context)
        self.assertInHTML('<h3 class="widget-title">分类</h3>', expected_html)
        self.assertInHTML("暂无分类！", expected_html)

    def test_show_categories_with_categories(self):
        cate_with_posts = Category.objects.create(name="有文章的分类")
        Post.objects.create(
            title="测试标题-1", body="测试内容", category=cate_with_posts, author=self.user,
        )
        another_cate_with_posts = Category.objects.create(name="另一个有文章的分类")
        Post.objects.create(
            title="测试标题-2",
            body="测试内容",
            category=another_cate_with_posts,
            author=self.user,
        )
        context = Context(show_categories(self.ctx))
        template = Template("{% load blog_extras %}" "{% show_categories %}")
        expected_html = template.render(context)
        self.assertInHTML('<h3 class="widget-title">分类</h3>', expected_html)

        url = reverse("blog:category", kwargs={"pk": cate_with_posts.pk})
        num_posts = cate_with_posts.post_set.count()
        frag = '<a href="{}">{} <span class="post-count">({})</span></a>'.format(
            url, cate_with_posts.name, num_posts
        )
        self.assertInHTML(frag, expected_html)

        url = reverse("blog:category", kwargs={"pk": another_cate_with_posts.pk})
        num_posts = another_cate_with_posts.post_set.count()
        frag = '<a href="{}">{} <span class="post-count">({})</span></a>'.format(
            url, another_cate_with_posts.name, num_posts
        )
        self.assertInHTML(frag, expected_html)

    def test_show_tags_without_any_tag(self):
        context = Context(show_tags(self.ctx))
        template = Template("{% load blog_extras %}" "{% show_tags %}")
        expected_html = template.render(context)
        self.assertInHTML('<h3 class="widget-title">标签云</h3>', expected_html)
        self.assertInHTML("暂无标签！", expected_html)

    def test_show_tags_with_tags(self):
        tag1 = Tag.objects.create(name="测试1")
        tag2 = Tag.objects.create(name="测试2")
        tag3 = Tag.objects.create(name="测试3")
        tag2_post = Post.objects.create(
            title="测试标题", body="测试内容", category=self.cate, author=self.user,
        )
        tag2_post.tags.add(tag2)
        tag2_post.save()

        another_tag2_post = Post.objects.create(
            title="测试标题", body="测试内容", category=self.cate, author=self.user,
        )
        another_tag2_post.tags.add(tag2)
        another_tag2_post.save()

        tag3_post = Post.objects.create(
            title="测试标题", body="测试内容", category=self.cate, author=self.user,
        )
        tag3_post.tags.add(tag3)
        tag3_post.save()

        context = Context(show_tags(self.ctx))
        template = Template("{% load blog_extras %}" "{% show_tags %}")
        expected_html = template.render(context)
        self.assertInHTML('<h3 class="widget-title">标签云</h3>', expected_html)

        tag2_url = reverse("blog:tag", kwargs={"pk": tag2.pk})
        tag2_num_posts = tag2.post_set.count()
        frag = '<a href="{}">{} <span class="post-count">({})</a>'.format(
            tag2_url, tag2.name, tag2_num_posts
        )
        self.assertInHTML(frag, expected_html)

        tag3_url = reverse("blog:tag", kwargs={"pk": tag3.pk})
        tag3_num_posts = tag3.post_set.count()
        frag = '<a href="{}">{} <span class="post-count">({})</a>'.format(
            tag3_url, tag3.name, tag3_num_posts
        )
        self.assertInHTML(frag, expected_html)

    def test_show_archives_without_any_post(self):
        context = Context(show_archives(self.ctx))
        template = Template("{% load blog_extras %}" "{% show_archives %}")
        expected_html = template.render(context)
        self.assertInHTML('<h3 class="widget-title">归档</h3>', expected_html)
        self.assertInHTML("暂无归档！", expected_html)

    def test_show_archives_with_post(self):
        post1 = Post.objects.create(
            title="测试标题-1",
            body="测试内容",
            category=self.cate,
            author=self.user,
            created_time=timezone.now(),
        )
        post2 = Post.objects.create(
            title="测试标题-1",
            body="测试内容",
            category=self.cate,
            author=self.user,
            created_time=timezone.now() - timedelta(days=50),
        )

        context = Context(show_archives(self.ctx))
        template = Template("{% load blog_extras %}" "{% show_archives %}")
        expected_html = template.render(context)
        self.assertInHTML('<h3 class="widget-title">归档</h3>', expected_html)

        created_time = post1.created_time
        url = reverse(
            "blog:archive",
            kwargs={"year": created_time.year, "month": created_time.month},
        )
        frag = '<a href="{}">{} 年 {} 月</a>'.format(
            url, created_time.year, created_time.month
        )
        self.assertInHTML(frag, expected_html)

        created_time = post2.created_time
        url = reverse(
            "blog:archive",
            kwargs={"year": created_time.year, "month": created_time.month},
        )
        frag = '<a href="{}">{} 年 {} 月</a>'.format(
            url, created_time.year, created_time.month
        )
        self.assertInHTML(frag, expected_html)
