from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.can_not_declare_read import CanNotDeclareRead
from acceptance_tests.actions.declare_read import DeclareRead
from acceptance_tests.actions.is_a_member import IsAMember
from acceptance_tests.actions.new_read_notification_received import NewReadNotificationReceived
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident
from acceptance_tests.actions.welcome_received import WelcomeReceived


class TestDeclareRead(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_members_receive_declaration_notification(self, character: CharacterCall) -> None:
        character('Michael').performs(
            BecomePresident(),
            AddMember('John'),
        )

        character('Michael').performs(DeclareRead('Design Patterns'))

        character('John').asserts(NewReadNotificationReceived('Design Patterns'))

    @book_club_spec
    def test_only_president_can_declare_read(self, character: CharacterCall) -> None:
        character('Michael').asserts(CanNotDeclareRead('Design Patterns'))
