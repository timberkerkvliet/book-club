from acceptance_tests import actions
from pyplay.action_executor import find_executors_in_module
from pyplay.logger import pyplay_logger
from pyplay.play_execution import pyplay_spec

book_club_spec = pyplay_spec(
    narrator=pyplay_logger(),
    prop_factories={},
    action_executors=find_executors_in_module(actions)
)
