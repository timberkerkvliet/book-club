from unittest import IsolatedAsyncioTestCase

from acceptance_tests.actions.is_a_member import IsAMember
from acceptance_tests.book_club_spec import book_club_spec
from pyplay.play import CharacterCall
from acceptance_tests.actions.join_club import LetCharacterJoinClub
from acceptance_tests.actions.make_myself_president import BecomePresident
from acceptance_tests.actions.welcome_received import WelcomeReceived


# class TestNewBook(IsolatedAsyncioTestCase):
#     @book_club_spec
#     def test_members_receive_declaration_notification(self, character: CharacterCall) -> None:
#         character('John').performs(
#             BecomePresident(),
#             LetCharacterJoinClub('Chris'),
#             DeclareNewRead('Design Patterns')
#         )
#
#         character('Chris').asserts(DeclarationNotificationReceived('Design Patterns'))
