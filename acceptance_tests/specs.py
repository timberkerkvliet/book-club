from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actor_name import ActorName
from acceptance_tests.add_actor_as_a_new_member import AddActorAsANewMember
from acceptance_tests.make_myself_president import MakeMyselfPresident
from acceptance_tests.screenplay import screenplay
from acceptance_tests.welcome_received import WelcomeReceived


class Test(IsolatedAsyncioTestCase):
    async def test_added_member_receives_welcome(self) -> None:
        async with screenplay() as screen_play:
            timber = screen_play.actor_named(ActorName('Timber'))
            timber.performs(MakeMyselfPresident())

            daniel = screen_play.actor_named(ActorName('Daniel'))
            timber.performs(AddActorAsANewMember(daniel.name))

            daniel.expects(WelcomeReceived())
