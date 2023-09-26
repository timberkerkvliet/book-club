from acceptance_tests.actions.become_president import MyInvokerIs
from acceptance_tests.actions.member_joined import MemberJoined
from book_club.invoker import Anonymous, Member, Invoker
from pyplay.log_book import LogBook


def get_invoker(log_book: LogBook, character_name: str) -> Invoker:
    invoker_logs = log_book.find().by_actor(character_name).by_type(MyInvokerIs)
    if len(list(invoker_logs)) > 0:
        return invoker_logs.one().invoker

    member_joined_log = log_book.find().by_type(MemberJoined)
    if len(list(member_joined_log)) > 0:
        return Member(member_joined_log.one().member_name)

    return Anonymous()
