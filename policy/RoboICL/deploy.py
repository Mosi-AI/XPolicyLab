"""Route the official RoboDojo evaluator through RoboICL's owned rollout."""

from __future__ import annotations

from typing import Any

from roboicl.rollout import eval_one_episode as _eval_one_episode


def eval_one_episode(TASK_ENV: Any, model_client: Any) -> None:
    """Run one official, single-environment RoboDojo episode."""
    _eval_one_episode(TASK_ENV, model_client)
