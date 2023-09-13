from acceptance_tests.add_actor_as_a_new_member import add_actor_as_new_member
from acceptance_tests.make_myself_president import make_myself_president
from acceptance_tests.welcome_received import welcome_received
from pyplay.logger import pyplay_logger
from pyplay.play_execution import pyplay_spec

book_club_spec = pyplay_spec(
    narrator=pyplay_logger(),
    prop_factories={},
    action_executors=[
        make_myself_president,
        welcome_received,
        add_actor_as_new_member
    ]
)
