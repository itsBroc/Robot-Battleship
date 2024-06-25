from components import Segment, Ship, Cell, InvalidPlacementException, InvalidPositionException, InvalidShipTypeException, Board
from random import Random

class Robot:

    def __init__(self):
        self.positions_played = []

    def generate_placements(self) -> list[tuple[str, str]]:
        ship_order = ["battleship", "carrier", "destroyer", "submarine", "patrol boat"]
        rand = Random()
        board = Board()
        placements = []
        invalid_placements = {ship_type: [] for ship_type in ship_order}

        for ship_type in ship_order:
            while len(placements) < len(ship_order):
                try:
                    ship = Ship.createShip(ship_type)
                    row = rand.choice('ABCDEFGHIJ')
                    col = str(rand.randint(1, 10))
                    direction = rand.choice(["across", "down"])
                    position = row + col

                    board.place_ship(ship, position, direction)

                except (InvalidPlacementException, InvalidPositionException):
                    invalid_placements[ship_type].append((position, direction))
                    continue
                placements.append((position, direction))
                break
                
        return placements

    def get_attack(self) -> str:
        if len(self.positions_played) >= 100:
            return None
        
        rand = Random()
        while len(self.positions_played) < 100:
            row = rand.choice('ABCDEFGHIJ')
            col = str(rand.randint(1, 10))
            position = row + col

            if position not in self.positions_played:
                self.positions_played.append(position)
                return position

    def give_result(self, result: str, board_state: list[list[str]]) -> None:
        pass