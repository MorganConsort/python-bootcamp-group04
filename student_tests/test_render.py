"""Acceptance tests for the rendering module, independent of other modules."""

from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def test_render_numbered_blocks():
    t = Task("DS exam", 5, 6, date(2026, 10, 30))
    assert render([Block(t, 0.5)]) == "Plan (0.5 h):\n  1. DS exam: 0.5 h"


def test_render_empty_plan():
    assert render([]) == "No tasks scheduled."
