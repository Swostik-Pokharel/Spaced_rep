from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional

class DifficultyLevel(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

@dataclass
class Concept:
    id: Optional[int]
    name: str
    last_review: date = field(default_factory=date.today)
    count: int = 0
    avg_success_rate: Optional[float] = None

@dataclass
class Task:
    id: Optional[int]
    concept_id: int
    is_problem: bool  # True = problem, False = question
    difficulty: DifficultyLevel
    last_review: date = field(default_factory=date.today)
    success_rate: Optional[float] = None
    count: int = 0

@dataclass
class Question:
    id: Optional[int]
    task_id: int
    question: str
    answer: str
    last_score: int

@dataclass
class Problem:
    id: Optional[int]
    task_id: int
    problem: str
    solution: str
    last_time: int  # time in minutes to complete
