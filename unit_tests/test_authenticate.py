import os
from unittest import IsolatedAsyncioTestCase

from book_club.authenticate import authenticate
from book_club.invoker import President, Member


class TestAuthenticate(IsolatedAsyncioTestCase):
    async def test_president(self):
        os.environ['PRESIDENTIAL_TOKEN'] = 'president'
        self.assertEqual(
            await authenticate(token='president'),
            President()
        )

    async def test_member(self):
        self.assertEqual(
            await authenticate(token='Chris'),
            Member('Chris')
        )
