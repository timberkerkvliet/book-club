from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.command_has_failed import CommandHasFailed
from acceptance_tests.actions.declare_read import DeclareRead
from acceptance_tests.actions.notification_received import NotificationReceived
from acceptance_tests.arrangements.club_with_president_and_member import arrange_club_with_president_and_member
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall


class TestDeclareRead(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_members_receive_notification(self, character: CharacterCall) -> None:
        michael = character('Michael')
        john = character('John')
        book_title = 'Design Patterns'
        arrange_club_with_president_and_member(president=michael, member=john)

        michael.performs(DeclareRead(book_title))

        john.expects(
            NotificationReceived()
            .with_content_containing(book_title)
        )

    @book_club_spec
    def test_member_can_not_declare_read(self, character: CharacterCall) -> None:
        john = character('John')
        arrange_club_with_president_and_member(president=character('Michael'), member=john)

        character('John').attempts(DeclareRead('DP'))

        character('John').expects(CommandHasFailed())
