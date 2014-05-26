from django.test import TestCase
from django.utils import timezone
import datetime
from polls.models import Poll
# Create your tests here.




class PollMethodTests(TestCase):

    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently() should return False for polls whose
        pub_date is in the future
        """

        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)

    def test_was_published_recently_with_old_poll(self):
        """
        was_published_recently() should return False for polls whose
        pub_date is in the future
        """

        future_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=3))
        self.assertEqual(future_poll.was_published_recently(), False)

    def test_was_published_recently_with_recent_poll(self):
        """
        was_published_recently() should return False for polls whose
        pub_date is in the future
        """

        future_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(future_poll.was_published_recently(), True)

