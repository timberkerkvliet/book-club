from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.command_has_failed import CommandHasFailed
from acceptance_tests.actions.declare_read import DeclareRead
from acceptance_tests.actions.notification_received import NotificationReceived
from acceptance_tests.arrangements.set_up_book_club import SetUpBookClub
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall


class TestDeclareRead(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_members_receive_notification(self, character: CharacterCall) -> None:
        michael = character('Michael')
        john = character('John')
        michael.performs(
            *SetUpBookClub().with_member(john)
        )

        new_read_title = 'Design Patterns'
        michael.performs(DeclareRead(new_read_title))

        john.expects(
            NotificationReceived()
            .with_content_containing(new_read_title)
        )

    @book_club_spec
    def test_member_can_not_declare_read(self, character: CharacterCall) -> None:
        michael = character('Michael')
        john = character('John')
        michael.performs(
            *SetUpBookClub().with_member(john)
        )

        book_title = 'Design Patterns'
        john.attempts(DeclareRead(book_title))

        john.expects(CommandHasFailed())
