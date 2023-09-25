from unittest import IsolatedAsyncioTestCase

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
        character('John').performs(
            BecomePresident(),
            AddMember('Chris'),
            DeclareRead('Design Patterns')
        )

        character('Chris').asserts(NewReadNotificationReceived('Design Patterns'))
