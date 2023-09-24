from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.cannot_make_myself_president import CanNotMakeMyselfPresident
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.add_actor_as_a_new_member import AddActorAsANewMember
from acceptance_tests.actions.make_myself_president import BecomePresident
from acceptance_tests.actions.welcome_received import WelcomeReceived


class TestPresident(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_there_can_only_be_one_president(self, character: CharacterCall) -> None:
        character('John').performs(BecomePresident())
        character('Chris').asserts(CanNotMakeMyselfPresident())

