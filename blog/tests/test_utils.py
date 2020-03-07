from django.test import TestCase
from ..utils import Highlighter


class HighlighterTestCase(TestCase):
    def test_highlight(self):
        document = "这是一个比较长的标题，用于测试关键词高亮但不被截断。"
        highlighter = Highlighter("标题")
        expected = '这是一个比较长的<span class="highlighted">标题</span>，用于测试关键词高亮但不被截断。'
        self.assertEqual(highlighter.highlight(document), expected)

        highlighter = Highlighter("关键词高亮")
        expected = '这是一个比较长的标题，用于测试<span class="highlighted">关键词高亮</span>但不被截断。'
        self.assertEqual(highlighter.highlight(document), expected)

        highlighter = Highlighter("标题")
        document = "这是一个长度超过 200 的标题，应该被截断。" + "HelloDjangoTutorial" * 200
        self.assertTrue(
            highlighter.highlight(document).startswith(
                '...<span class="highlighted">标题</span>，应该被截断。'
            )
        )
