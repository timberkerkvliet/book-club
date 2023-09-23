from dataclasses import dataclass


@dataclass(frozen=True)
class AppContext:
    is_fake: bool

    def __eq__(self, other):
        return False

