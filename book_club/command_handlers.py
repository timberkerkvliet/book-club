from book_club.current_read.declare_new_read import DeclareNewRead, declare_current_book
from book_club.member_list.join_club import JoinClub, join_club
from book_club.member_list.kick_member import KickMember, kick_member


def command_handlers():
    return {
        JoinClub: join_club,
        KickMember: kick_member,
        DeclareNewRead: declare_current_book
    }
