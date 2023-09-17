from functools import lru_cache

from book_club.mail_client import FakeMailClient
from book_club.member_repository import InMemoryMemberRepository


@lru_cache
def app_member_repository():
    return InMemoryMemberRepository()


@lru_cache
def app_mail_client():
    return FakeMailClient()
