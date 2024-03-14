class Helpers():
    def __init__(self) -> None:
        pass

    def get_coordinate_tuple(self, coordinate_text: str) -> tuple:
        coordinate_list = coordinate_text.split(',')
        coordinate: tuple = int(coordinate_list[0]), int(coordinate_list[1])
        return coordinate