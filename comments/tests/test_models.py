from .base import CommentDataTestCase
from ..models import Comment


class CommentModelTestCase(CommentDataTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.comment = Comment.objects.create(
            name="评论者", email="a@a.com", text="评论内容", post=self.post,
        )

    def test_str_representation(self):
        self.assertEqual(self.comment.__str__(), "评论者: 评论内容")
