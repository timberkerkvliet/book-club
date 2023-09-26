from book_club.member_list.get_member_list import GetMemberList, get_member_list


def query_handlers():
    return {
        GetMemberList: get_member_list
    }
