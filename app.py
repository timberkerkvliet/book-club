from functools import lru_cache

from acceptance_tests.mail_client import FakeMailClient
from member_repository import InMemoryMemberRepository


@lru_cache
def app_member_repository():
    return InMemoryMemberRepository()


@lru_cache
def app_mail_client():
    return FakeMailClient()
