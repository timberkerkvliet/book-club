from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.is_a_member import IsAMember
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.add_actor_as_a_new_member import AddActorAsANewMember
from acceptance_tests.actions.make_myself_president import BecomePresident
from acceptance_tests.actions.welcome_received import WelcomeReceived


class TestAddNewMember(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_added_member_receives_welcome(self, character: CharacterCall) -> None:
        timber = character('John').performs(BecomePresident())

        chris = character('Chris')
        timber.performs(AddActorAsANewMember('Chris'))

        chris.asserts(WelcomeReceived())

    @book_club_spec
    def test_added_member_is_added(self, character: CharacterCall) -> None:
        character('John').performs(
            BecomePresident(),
            AddActorAsANewMember('Chris'),
            IsAMember('Chris')
        )
