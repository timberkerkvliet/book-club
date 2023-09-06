from unittest import IsolatedAsyncioTestCase

from dsl import Actor, AddANewMember, executable_play


class Test(IsolatedAsyncioTestCase):
    async def test_added_member_receives_welcome(self) -> None:
        async with executable_play() as play:
            timber = play.with_actor_called('Timber').who_can_access_presidential_interface()
            daniel = play.with_actor_called('Daniel')

            timber.performs(
                AddANewMember().for_actor(daniel)
            )

            daniel.expects(WelcomeReceived())

    async def test_when_add_a_member_then_president_receives_updated_list(self) -> None:
        timber = Actor().with_president_role()

        timber.performs(
            AddANewMember().with_name('Daniel').with_mail_address('lklk@mailli')
        )

        timber.expects(
            MemberListReceived().with_member('Daniel')
        )
