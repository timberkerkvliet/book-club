from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.can_not_declare_read import CanNotDeclareRead
from acceptance_tests.actions.declare_read import DeclareRead
from acceptance_tests.actions.new_read_notification_received import NewReadNotificationReceived
from acceptance_tests.actions.notification_received import NotificationReceived
from acceptance_tests.arrangements.club_with_president_and_member import arrange_club_with_president_and_member
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall


class TestDeclareRead(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_members_receive_notification(self, character: CharacterCall) -> None:
        arrange_club_with_president_and_member(president=character('Michael'), member='John')

        character('Michael').performs(DeclareRead(book_name='Design Patterns'))

        character('John').asserts(
            NotificationReceived()
            .with_content_containing('Design Patterns')
        )

    @book_club_spec
    def test_member_can_not_declare_read(self, character: CharacterCall) -> None:
        arrange_club_with_president_and_member(president=character('Michael'), member='John')

        character('John').asserts(CanNotDeclareRead('Design Patterns'))
