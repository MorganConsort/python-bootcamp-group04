"""Tests for the three additional study_planner modules: summarise, filter_tasks, export."""

import json
from datetime import date
from pathlib import Path

import pytest

from shared.contract import Block, Task
from shared.study_planner.export import export_plan, import_plan_titles
from shared.study_planner.filter_tasks import filter_by_deadline, filter_by_importance
from shared.study_planner.summarise import summarise

# ── Fixtures ────────────────────────────────────────────────────────────────

TASK_A = Task("DS exam", 5, 6.0, date(2026, 10, 30))
TASK_B = Task("Assignment", 4, 1.5, date(2026, 10, 27))
TASK_C = Task("Essay", 2, 3.0, date(2026, 11, 5))


# ── summarise ───────────────────────────────────────────────────────────────

class TestSummarise:
    def test_empty_plan(self):
        result = summarise([])
        assert result == {
            "task_count": 0,
            "total_hours": 0.0,
            "avg_hours": 0.0,
            "tasks": [],
        }

    def test_single_block(self):
        blocks = [Block(TASK_A, 4.0)]
        result = summarise(blocks)
        assert result["task_count"] == 1
        assert result["total_hours"] == 4.0
        assert result["avg_hours"] == 4.0
        assert result["tasks"] == [{"title": "DS exam", "hours": 4.0}]

    def test_multiple_blocks(self):
        blocks = [Block(TASK_A, 3.0), Block(TASK_B, 1.5)]
        result = summarise(blocks)
        assert result["task_count"] == 2
        assert result["total_hours"] == 4.5
        assert result["avg_hours"] == 2.25
        assert len(result["tasks"]) == 2


# ── filter_tasks ────────────────────────────────────────────────────────────

class TestFilterByDeadline:
    def test_within_range(self):
        tasks = [TASK_A, TASK_B, TASK_C]
        result = filter_by_deadline(tasks, date(2026, 10, 25), date(2026, 10, 31))
        assert result == [TASK_A, TASK_B]

    def test_exact_boundary(self):
        result = filter_by_deadline([TASK_A], date(2026, 10, 30), date(2026, 10, 30))
        assert result == [TASK_A]

    def test_no_match(self):
        result = filter_by_deadline([TASK_A], date(2026, 12, 1), date(2026, 12, 31))
        assert result == []

    def test_start_after_end_raises(self):
        with pytest.raises(ValueError, match="start"):
            filter_by_deadline([TASK_A], date(2026, 11, 1), date(2026, 10, 1))

    def test_empty_list(self):
        result = filter_by_deadline([], date(2026, 1, 1), date(2026, 12, 31))
        assert result == []


class TestFilterByImportance:
    def test_high_importance(self):
        tasks = [TASK_A, TASK_B, TASK_C]
        result = filter_by_importance(tasks, 4)
        assert result == [TASK_A, TASK_B]

    def test_all_pass(self):
        result = filter_by_importance([TASK_A, TASK_B, TASK_C], 1)
        assert result == [TASK_A, TASK_B, TASK_C]

    def test_none_pass(self):
        result = filter_by_importance([TASK_C], 5)
        assert result == []


# ── export ──────────────────────────────────────────────────────────────────

class TestExport:
    def test_export_and_reimport(self, tmp_path: Path):
        blocks = [Block(TASK_A, 3.0), Block(TASK_B, 1.5)]
        out = tmp_path / "plan.json"
        export_plan(blocks, out)

        data = json.loads(out.read_text(encoding="utf-8"))
        assert len(data) == 2
        assert data[0]["task"] == "DS exam"
        assert data[0]["deadline"] == "2026-10-30"
        assert data[0]["hours"] == 3.0

    def test_import_titles(self, tmp_path: Path):
        blocks = [Block(TASK_A, 3.0), Block(TASK_B, 1.5)]
        out = tmp_path / "plan.json"
        export_plan(blocks, out)

        titles = import_plan_titles(out)
        assert titles == ["DS exam", "Assignment"]

    def test_empty_export(self, tmp_path: Path):
        out = tmp_path / "empty.json"
        export_plan([], out)
        data = json.loads(out.read_text(encoding="utf-8"))
        assert data == []
        assert import_plan_titles(out) == []
