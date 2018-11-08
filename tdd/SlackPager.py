from unittest.mock import Mock, patch
from nose.tools import assert_is_none, assert_list_equal, assert_true

from SlackPager import SlackPager


class TestSlackPager:


    @classmethod
    def setup(cls):
        cls.mock_os_patcher = patch('SlackPager.os.environ')
        cls.mock_post_patcher = patch('SlackPager.requests.post')
        cls.mock_post = cls.mock_post_patcher.start()
        cls.mock_os = cls.mock_os_patcher.start()


    @classmethod
    def teardown(cls):
        cls.mock_post_patcher.stop()
        cls.mock_os_patcher.stop()


    def test_send_slack_pager_message_is_ok(self):
        self.mock_post.return_value.ok = True

        message: str = 'ERROR: logged'

        self.mock_post.return_value = Mock()
        self.mock_os.return_value = Mock()
        self.mock_os.return_value.url = 'https://slack.test.com/'

        sp = SlackPager(message)
        response = sp.send_slack_pager_message()

        assert_true(response)

