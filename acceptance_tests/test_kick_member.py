from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.is_a_member import IsAMember
from acceptance_tests.actions.is_not_a_member import IsNotAMember
from acceptance_tests.actions.leave_club import KickMember
from acceptance_tests.arrangements.club_with_president_and_member import set_up_book_club
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall


class TestKickMember(IsolatedAsyncioTestCase):
    @book_club_spec
    def test_president_can_kick_member(self, character: CharacterCall) -> None:
        john = character('John')
        michael = character('Michael')
        set_up_book_club(president=michael, member=john)

        michael.performs(KickMember('John'))
        michael.expects(IsNotAMember('John'))

    @book_club_spec
    def test_member_can_not_kick(self, character: CharacterCall) -> None:
        john = character('John')
        michael = character('Michael')
        set_up_book_club(president=michael, member=john)

        character('John').attempts(KickMember('John'))

        character('Michael').expects(IsAMember('John'))
