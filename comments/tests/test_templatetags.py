from datetime import timedelta

from django.apps import apps
from django.contrib.auth.models import User
from django.template import Context, Template
from django.utils import timezone

from blog.models import Category, Post
from .base import CommentDataTestCase
from ..forms import CommentForm
from ..models import Comment
from ..templatetags.comments_extras import show_comment_form, show_comments


class CommentExtraTestCase(CommentDataTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.ctx = Context()

    def test_show_comment_form_with_empty_form(self):
        template = Template("{% load comments_extras %}" "{% show_comment_form post %}")
        form = CommentForm()
        context = Context(show_comment_form(self.ctx, self.post))
        expected_html = template.render(context)
        for field in form:
            label = '<label for="{}">{}：</label>'.format(
                field.id_for_label, field.label
            )
            self.assertInHTML(label, expected_html)
            self.assertInHTML(str(field), expected_html)

    def test_show_comment_form_with_invalid_bound_form(self):
        template = Template(
            "{% load comments_extras %}" "{% show_comment_form post form %}"
        )
        invalid_data = {
            "email": "invalid_email",
        }
        form = CommentForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        context = Context(show_comment_form(self.ctx, self.post, form=form))
        expected_html = template.render(context)
        for field in form:
            label = '<label for="{}">{}：</label>'.format(
                field.id_for_label, field.label
            )
            self.assertInHTML(label, expected_html)
            self.assertInHTML(str(field), expected_html)
            self.assertInHTML(str(field.errors), expected_html)

    def test_show_comments_without_any_comment(self):
        template = Template("{% load comments_extras %}" "{% show_comments post %}")
        ctx_dict = show_comments(self.ctx, self.post)
        ctx_dict["post"] = self.post
        context = Context(ctx_dict)
        expected_html = template.render(context)
        self.assertInHTML("<h3>评论列表，共 <span>0</span> 条评论</h3>", expected_html)
        self.assertInHTML("暂无评论", expected_html)

    def test_show_comments_with_comments(self):
        comment1 = Comment.objects.create(
            name="评论者1", email="a@a.com", text="评论内容1", post=self.post,
        )
        comment2 = Comment.objects.create(
            name="评论者2",
            email="a@a.com",
            text="评论内容2",
            post=self.post,
            created_time=timezone.now() - timedelta(days=1),
        )
        template = Template("{% load comments_extras %}" "{% show_comments post %}")
        ctx_dict = show_comments(self.ctx, self.post)
        ctx_dict["post"] = self.post
        context = Context(ctx_dict)
        expected_html = template.render(context)
        self.assertInHTML("<h3>评论列表，共 <span>2</span> 条评论</h3>", expected_html)
        self.assertInHTML(comment1.name, expected_html)
        self.assertInHTML(comment1.text, expected_html)
        self.assertInHTML(comment2.name, expected_html)
        self.assertInHTML(comment2.text, expected_html)
        self.assertQuerysetEqual(
            ctx_dict["comment_list"], [repr(c) for c in [comment1, comment2]]
        )
