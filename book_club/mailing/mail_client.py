from abc import ABC, abstractmethod

from book_club.mailing.mail import Mail


class MailClient(ABC):
    @abstractmethod
    async def send(self, mail: Mail) -> None:
        """Sends a mail"""
