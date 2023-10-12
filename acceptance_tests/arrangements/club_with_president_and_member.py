from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident
from pyplay.character import Character
from pyplay.name import Name


def arrange_club_with_president_and_member(president: Character, member: Name):
    president.performs(
        BecomePresident(),
        AddMember(member)
    )
