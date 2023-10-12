from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.book_election_notification_received import BookElectionNotificationReceived
from acceptance_tests.actions.can_not_start_book_election import CanNotStartBookElection
from acceptance_tests.actions.start_book_election import StartBookElection
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident

BOOK_NAMES = ['Clean Agile', 'Pragmatic Engineer']


class TestStartElection(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_only_president_can_start_book_election(self, character: CharacterCall) -> None:
        character('John').asserts(CanNotStartBookElection())
