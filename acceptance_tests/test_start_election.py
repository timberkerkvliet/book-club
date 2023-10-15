from unittest import IsolatedAsyncioTestCase
from pyplay.play import CharacterCall

from acceptance_tests.actions.command_has_failed import CommandHasFailed
from acceptance_tests.actions.notification_received import NotificationReceived
from acceptance_tests.actions.start_book_election import StartBookElection
from acceptance_tests.book_club_spec import book_club_spec
from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident
from acceptance_tests.arrangements.club_with_president_and_member import set_up_book_club


class TestStartElection(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_members_can_not_start_a_book_election(self, character: CharacterCall) -> None:
        pass

    @book_club_spec
    def test_members_get_notified_about_book_election(self, character: CharacterCall) -> None:
        pass
