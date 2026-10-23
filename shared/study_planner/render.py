"""Readable deterministic study-plan output."""

from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Render numbered task titles and allocated hours, or an empty message."""
    if not blocks:
        return "No tasks scheduled."
    lines = [f"Plan ({sum(block.hours for block in blocks):g} h):"]
    lines.extend(
        f"  {index}. {block.task.title}: {block.hours:g} h" for index, block in enumerate(blocks, 1)
    )
    return "\n".join(lines)
