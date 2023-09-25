from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.can_not_kick_member import CanNotKickMember
from acceptance_tests.actions.is_a_member import IsAMember
from acceptance_tests.actions.is_not_a_member import IsNotAMember
from acceptance_tests.actions.leave_club import LetCharacterLeaveClub
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.join_club import LetCharacterJoinClub
from acceptance_tests.actions.become_president import BecomePresident
from acceptance_tests.actions.welcome_received import WelcomeReceived


class TestLeaveClub(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_president_can_kick_member(self, character: CharacterCall) -> None:
        character('John').performs(
            BecomePresident(),
            LetCharacterJoinClub('Chris'),
            LetCharacterLeaveClub('Chris'),
        )
        character('John').asserts(IsNotAMember('Chris'))

    @book_club_spec
    def test_member_can_not_kick(self, character: CharacterCall) -> None:
        character('John').performs(
            BecomePresident(),
            LetCharacterJoinClub('Chris'),
            LetCharacterLeaveClub('Rocky')
        )
        character('Chris').asserts(CanNotKickMember('Rocky'))