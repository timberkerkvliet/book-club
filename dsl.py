from typing import Self


class AddANewMember:
    ...



class Actor:
    def __init__(self):
        ...

    def with_president_role(self) -> Self:
        return self

    def with_member_role(self) -> Self:
        return self

    def performs(self, *actions):
        ...

    def expects(self, *assertions):
        ...
