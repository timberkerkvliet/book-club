from dsl import Actor, AddANewMember


async def test_added_member_receive_welcome_mail():
    timber = Actor().with_president_role()
    daniel = Actor().with_member_role()

    timber.performs(
        AddANewMember().with_name('Daniel').with_mail_address('lklk@mailli')
    )

    daniel.expects(
        WelcomeMailReceived()
    )


async def test_when_add_a_member_then_president_receives_updated_list():
    timber = Actor().with_president_role()

    timber.performs(
        AddANewMember().with_name('Daniel').with_mail_address('lklk@mailli')
    )

    timber.expects(
        MemberListMailReceived().with_member('Daniel')
    )
