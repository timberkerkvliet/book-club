from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.get_invoker import get_invoker
from acceptance_tests.actions.invoke_api import invoke_api
from book_club.app import App
from book_club.app_context import AppContext
from book_club.book_election.start_book_election import StartBookElection as StartBookElectionCommand
from book_club.request_handler import request_handler

from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


class StartBookElection(Action):
    def __init__(self):
        self._book_names = []

    def with_candidates(self, *options: str) -> StartBookElection:
        self._book_names += options
        return self

    @property
    def candidates(self) -> list[str]:
        return self._book_names


@executes(StartBookElection)
async def add_actor_as_new_member(
    action: StartBookElection,
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    await invoke_api(
        command=StartBookElectionCommand(
            candidates=action.candidates
        ),
        app=await stage_props(App),
        log_book=log_book,
        character_name=actor.character_name
    )
