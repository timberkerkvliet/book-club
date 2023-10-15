from unittest import IsolatedAsyncioTestCase

from pyplay.play import CharacterCall

from acceptance_tests.actions.command_has_failed import CommandHasFailed
from acceptance_tests.actions.is_a_member import IsAMember
from acceptance_tests.actions.notification_received import NotificationReceived
from acceptance_tests.arrangements.club_with_president_and_member import arrange_club_with_president_and_member
from acceptance_tests.book_club_spec import book_club_spec
from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident


class TestAddMember(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_president_can_add_members(self, character: CharacterCall) -> None:
        character('Michael').performs(BecomePresident())

        character('Michael').performs(AddMember('John'))

        character('Michael').expects(IsAMember('John'))

    @book_club_spec
    def test_non_president_can_not_add_members(self, character: CharacterCall) -> None:
        john = character('John')
        arrange_club_with_president_and_member(president=character('Michael'), member=john)

        character('John').attempts(AddMember('Britney'))

        character('John').expects(CommandHasFailed())

    @book_club_spec
    def test_new_member_receives_welcome(self, character: CharacterCall) -> None:
        john = character('John')
        arrange_club_with_president_and_member(president=character('Michael'), member=john)

        character('John').expects(
            NotificationReceived()
            .with_content_containing('Welcome')
        )
