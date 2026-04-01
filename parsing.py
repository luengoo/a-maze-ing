import shutil
import importlib


class ConfigChecker:

    """Config checking class"""

    def opener(self) -> dict:
        """Opens the config file and returns the values"""
        config = {}
        with open("config.txt", "r") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    raise ValueError(f"Invalid line: {line}")
                key, value = line.split("=", 1)
                key = key.strip()
                if key in config:
                    raise ValueError(f"Duplicate key detected. '{key}'")
                config[key] = self.parse_value(key, value.strip())

        self.validate_config(config)
        return config

    def parse_value(self, key: str, value: str) -> tuple:
        """Gets key value pairs"""

        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            pass

        if value in ["True", "False"]:
            if value == "True":
                return True
            else:
                return False

        if key in ["ENTRY", "EXIT"]:
            parts = value.split(",")
            if len(parts) == 2:
                try:
                    return (int(parts[1].strip()), int(parts[0].strip()))
                except ValueError:
                    raise ValueError(f"Invalid tuple format for {key}: {value}"
                                     )

        return value

    def blocked_42_zone(self, width: int, height: int) -> set:
        """Defines the 42 drawing as blocked cells"""
        start_y = height // 2 - 2
        start_x = width // 2 - 6
        blocked_cells = set()
        for dy in range(5):
            for dx in range(8):
                blocked_cells.add((start_y + dy, start_x + dx))
        return blocked_cells

    def validate_config(self, config: dict) -> None:
        """Check that the files has the required keys,
            validates each key and value, raises errors
            in case of an issue"""

        required_keys = ["WIDTH", "HEIGHT", "ENTRY",
                         "EXIT", "PERFECT"
                         , "OUTPUT_FILE"]
        

        for key in required_keys:
            if key not in config:
                raise ValueError(f"No required key found: {key}")

        width = config["WIDTH"]
        height = config["HEIGHT"]
        entry = config["ENTRY"]
        exit = config["EXIT"]
        perfect = config["PERFECT"]
        output = config["OUTPUT_FILE"]

        if width <= 0 or height <= 0:
            raise ValueError(
                "Invalid width and height: must be greater than 0.")

        if not isinstance(entry, tuple):
            raise ValueError("Entry point must be a tuple (X,X)")

        if not isinstance(exit, tuple):
            raise ValueError("Exit point must be a tuple (X,X)")

        if (entry == exit):
            raise ValueError("Exit and Entry must be different.")

        if not isinstance(
         width, int) or not isinstance(height, int):
            raise ValueError("Width and Height must be integers.")

        if not (isinstance(perfect, bool)):
            raise ValueError(
                "Perfect value in config must be a bool (True or False)")

        if not (0 <= entry[1] < width and
           0 <= entry[0] < height):
            raise ValueError("ENTRY outside of the map.")

        if not (0 <= exit[1] < width and
                0 <= exit[0] < height):
            raise ValueError("EXIT outside of the map.")

        if not output.endswith(".txt"):
            raise ValueError("Output file should be '.txt'.")

        if height >= 7 or width >= 12:
            blocked_cells = self.blocked_42_zone(width, height)
            if entry in blocked_cells:
                raise ValueError(
                    f"ENTRY {config['ENTRY']} is inside the blocked 42 coords")
            if exit in blocked_cells:
                raise ValueError(
                    f"EXIT {config['EXIT']} is inside the blocked 42 coords")


def check_terminal_size(width: int, height: int) -> None:
    """checks if terminal size is big enough for the maze"""

    col, row = shutil.get_terminal_size()

    required_cols = width * 4 + 1
    required_rows = height * 2 + 1 + 9  # maze + bottom border + footer

    if col < required_cols or row < required_rows:
        raise RuntimeError("Terminal is too small. Please resize")

def check_dep(reqs: list[str]) -> None:

    missing = []
    for req in reqs:
        try:
           _ = importlib.import_module(req)

        except ModuleNotFoundError:
            missing.append(req)
    
    if len(missing) > 0:
        dep_str =  ", ".join(missing)
        raise ModuleNotFoundError(f"Missing dependencies: {dep_str}")
    

