from unittest import IsolatedAsyncioTestCase

from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.add_actor_as_a_new_member import AddActorAsANewMember
from acceptance_tests.make_myself_president import MakeMyselfPresident
from acceptance_tests.welcome_received import WelcomeReceived


class Test(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_added_member_receives_welcome(self, character: CharacterCall) -> None:
        timber = character('Timber').performs(MakeMyselfPresident())

        daniel = character('Daniel')
        timber.performs(AddActorAsANewMember('Daniel'))

        daniel.asserts(WelcomeReceived())
