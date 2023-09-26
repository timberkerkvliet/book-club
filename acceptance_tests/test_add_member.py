from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.can_not_add_member import CanNotAddMember
from acceptance_tests.actions.is_a_member import IsAMember
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident
from acceptance_tests.actions.welcome_received import WelcomeReceived


class TestAddMember(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_president_can_add_members(self, character: CharacterCall) -> None:
        character('John').performs(
            BecomePresident(),
            AddMember('Chris')
        )
        character('John').asserts(IsAMember('Chris'))

    @book_club_spec
    def test_non_president_can_not_add_members(self, character: CharacterCall) -> None:
        character('John').asserts(CanNotAddMember('Chris'))

    @book_club_spec
    def test_new_member_receives_welcome(self, character: CharacterCall) -> None:
        character('John').performs(
            BecomePresident(),
            AddMember('Chris')
        )

        character('Chris').asserts(WelcomeReceived())
