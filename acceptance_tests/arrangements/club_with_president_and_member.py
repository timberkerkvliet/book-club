from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident
from pyplay.character import Character
from pyplay.name import Name


def set_up_book_club(president: Character, member: Character):
    president.performs(
        BecomePresident(),
        AddMember(member.name)
    )
