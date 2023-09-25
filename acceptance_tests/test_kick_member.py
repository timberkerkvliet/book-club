from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.can_not_kick_member import CanNotKickMember
from acceptance_tests.actions.is_a_member import IsAMember
from acceptance_tests.actions.is_not_a_member import IsNotAMember
from acceptance_tests.actions.leave_club import KickMember
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident
from acceptance_tests.actions.welcome_received import WelcomeReceived


class TestKickMember(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_president_can_kick_member(self, character: CharacterCall) -> None:
        character('John').performs(
            BecomePresident(),
            AddMember('Chris'),
            KickMember('Chris'),
        )
        character('John').asserts(IsNotAMember('Chris'))

    @book_club_spec
    def test_member_can_not_kick(self, character: CharacterCall) -> None:
        character('John').performs(
            BecomePresident(),
            AddMember('Chris'),
            KickMember('Rocky')
        )
        character('Chris').asserts(CanNotKickMember('Rocky'))
