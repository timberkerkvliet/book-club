import os
from unittest import IsolatedAsyncioTestCase

from book_club.mail_address import MailAddress
from book_club.member_list.member import Member
from book_club.member_list.member_repository import FileMemberRepository
from book_club.name import Name

FILE_PATH = 'test_file'


class TestFileMemberRepository(IsolatedAsyncioTestCase):
    def tearDown(self) -> None:
        if os.path.isfile(FILE_PATH):
            os.remove(FILE_PATH)

    async def test_no_members(self):
        repository = FileMemberRepository(FILE_PATH)
        member_list = await repository.get_member_list()

        self.assertEqual(len(member_list), 0)

    async def test_load_and_save(self):
        repository = FileMemberRepository(FILE_PATH)
        member_list = await repository.get_member_list()
        member_list.add(
            Member(
                name=Name('Timber'),
                mail_address=MailAddress('a@b.com')
            )
        )
        await repository.save()
        repository = FileMemberRepository(FILE_PATH)
        member_list = await repository.get_member_list()
        self.assertEqual(len(member_list), 1)
