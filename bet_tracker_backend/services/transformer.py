"""Module to transform data into its various forms."""
import logging
from typing import Optional
from bet_tracker_backend.models.sports_data_io import PlayerGameStats

class PlayerGameStatsTransformer:
    @staticmethod
    def transform(players: dict, dto: PlayerGameStats):

        def _get_attr(obj: dict[str, str], attributes: list[str]) -> Any:
            final_attr: [Any]
            for attribute in attributes:
                final_attr = obj.get(attribute)
                if final_attr is None:
                    break

            return final_attr
        for player in players:
            