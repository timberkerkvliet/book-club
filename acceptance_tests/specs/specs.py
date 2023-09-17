from unittest import IsolatedAsyncioTestCase

from acceptance_tests.specs.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.add_actor_as_a_new_member import AddActorAsANewMember
from acceptance_tests.actions.make_myself_president import MakeMyselfPresident
from acceptance_tests.actions.welcome_received import WelcomeReceived


class Test(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_added_member_receives_welcome(self, character: CharacterCall) -> None:
        timber = character('John').performs(MakeMyselfPresident())

        chris = character('Chris')
        timber.performs(AddActorAsANewMember('Chris'))

        chris.asserts(WelcomeReceived())
