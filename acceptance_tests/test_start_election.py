from unittest import IsolatedAsyncioTestCase, skip

from acceptance_tests.actions.book_election_notification_received import BookElectionNotificationReceived
from acceptance_tests.actions.can_not_start_book_election import CanNotStartBookElection
from acceptance_tests.actions.start_book_election import StartBookElection
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident
from acceptance_tests.arrangements.club_with_president_and_member import arrange_club_with_president_and_member

BOOK_NAMES = ['Clean Agile', 'Pragmatic Engineer']


class TestStartElection(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_members_can_not_start_a_book_election(self, character: CharacterCall) -> None:
        arrange_club_with_president_and_member(president=character('Michael'), member='John')

        character('John').asserts(CanNotStartBookElection())
