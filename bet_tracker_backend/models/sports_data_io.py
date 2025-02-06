"""Module for containing models for incoming data."""
from dataclasses import dataclass

@dataclass
# TODO: Add more later after concept to enhance
class PlayerGameStats:
    game_key: str
    player_id: int
    season: int
    game_date: str
    week: str
    team: str
    opponent: str
    home_or_away: str
    number: int
    name: str
    position: str
    passing_attempts: int
    passing_completions: int
    passing_yards: int
    passing_touchdowns: int
    passing_interceptions: int
    rushing_attempts: int 
    rusing_yards: str
    rushing_touchdowns: int
    recieving_targets: int
    recieving_touchdowns: int

    

