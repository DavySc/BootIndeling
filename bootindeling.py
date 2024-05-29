from typing import NamedTuple

class Record(NamedTuple):
    finishedrounds: list
    groups: list
    nextplayer: int = 0
    totalCost: int = 0
    weights: None

class SeatingChart(NamedTuple):
    participants: list
    total_groups: int
    seats_per_group: int
    rounds: int

player_count = len(SeatingChart.participants)


