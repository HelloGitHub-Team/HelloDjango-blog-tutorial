from django.apps import apps
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Category, Post, Tag
from ..search_indexes import PostIndex


class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.cate = Category.objects.create(name="测试")

    def test_str_representation(self):
        self.assertEqual(self.cate.__str__(), self.cate.name)


class TagModelTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="测试")

    def test_str_representation(self):
        self.assertEqual(self.tag.__str__(), self.tag.name)


class PostModelTestCase(TestCase):
    def setUp(self):
        # 断开 haystack 的 signal，测试生成的文章无需生成索引
        apps.get_app_config("haystack").signal_processor.teardown()
        user = User.objects.create_superuser(
            username="admin", email="admin@hellogithub.com", password="admin"
        )
        cate = Category.objects.create(name="测试")
        self.post = Post.objects.create(
            title="测试标题", body="测试内容", category=cate, author=user,
        )

    def test_str_representation(self):
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_auto_populate_modified_time(self):
        self.assertIsNotNone(self.post.modified_time)

        old_post_modified_time = self.post.modified_time
        self.post.body = "新的测试内容"
        self.post.save()
        self.post.refresh_from_db()
        self.assertTrue(self.post.modified_time > old_post_modified_time)

    def test_auto_populate_excerpt(self):
        self.assertIsNotNone(self.post.excerpt)
        self.assertTrue(0 < len(self.post.excerpt) <= 54)

    def test_get_absolute_url(self):
        expected_url = reverse("blog:detail", kwargs={"pk": self.post.pk})
        self.assertEqual(self.post.get_absolute_url(), expected_url)

    def test_increase_views(self):
        self.post.increase_views()
        self.post.refresh_from_db()
        self.assertEqual(self.post.views, 1)

        self.post.increase_views()
        self.post.refresh_from_db()
        self.assertEqual(self.post.views, 2)


class SearchIndexesTestCase(TestCase):
    def setUp(self):
        apps.get_app_config("haystack").signal_processor.teardown()
        user = User.objects.create_superuser(
            username="admin", email="admin@hellogithub.com", password="admin"
        )
        cate = Category.objects.create(name="测试")
        Post.objects.create(
            title="测试标题", body="测试内容", category=cate, author=user,
        )
        another_cate = Category.objects.create(name="另一个测试")
        Post.objects.create(
            title="另一个测试标题", body="另一个测试内容", category=another_cate, author=user,
        )
        self.index_instance = PostIndex()

    def test_get_model(self):
        self.assertTrue(issubclass(self.index_instance.get_model(), Post))

    def test_index_queryset(self):
        expected_qs = Post.objects.all()
        self.assertQuerysetEqual(
            self.index_instance.index_queryset(), [repr(p) for p in expected_qs]
        )
