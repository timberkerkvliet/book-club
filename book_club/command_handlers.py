from book_club.current_read.declare_new_read import DeclareNewRead, declare_new_read
from book_club.member_list.add_member import AddMember, add_member
from book_club.member_list.kick_member import KickMember, kick_member


def command_handlers():
    return {
        AddMember: add_member,
        KickMember: kick_member,
        DeclareNewRead: declare_new_read
    }
