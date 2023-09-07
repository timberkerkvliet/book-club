from unittest import IsolatedAsyncioTestCase


from acceptance_tests.add_actor_as_a_new_member import AddActorAsANewMember
from acceptance_tests.make_myself_president import MakeMyselfPresident
from acceptance_tests.stage import executable_spec
from acceptance_tests.welcome_received import WelcomeReceived


class Test(IsolatedAsyncioTestCase):
    async def test_added_member_receives_welcome(self) -> None:
        async with executable_spec() as stage:
            timber = stage.actor()
            timber.performs(MakeMyselfPresident())

            daniel = stage.actor()
            timber.performs(AddActorAsANewMember(daniel))

            daniel.expects(WelcomeReceived())
