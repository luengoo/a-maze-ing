class ConfigChecker:
    def __init__(self):
        pass

    def opener(self) -> dict:
        config = {}
        try:
            with open("config.txt", "r") as file:
                for line in file:
                    line = line.strip()

                    if not line or line.startswith("#"):
                        continue
                    if "=" not in line:
                        raise ValueError(f"Invalid line: {line}")
                    key, value = line.split("=", 1)
                    config[key.strip()] = self.parse_value(
                        key.strip(), value.strip())
            self.validate_config(config)
            return config
        except (ValueError, FileNotFoundError) as e:
            print(f"Found an error in config.txt file: {e}")

    def parse_value(self, key: str, value: str):
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
                    return (int(parts[0].strip()), int(parts[1].strip()))
                except ValueError:
                    raise ValueError(f"Invalid tuple format for {key}: {value}"
                                     )

        return value

    def blocked_42_zone(self, width, height):
        start_y = height // 2 - 2
        start_x = width // 2 - 6
        blocked_cells = set()
        for dy in range(5):
            for dx in range(8):
                blocked_cells.add((start_y + dy, start_x + dx))
        return blocked_cells

    def validate_config(self, config: dict):
        required_keys = ["WIDTH", "HEIGHT", "ENTRY",
                         "EXIT", "OUTPUT_FILE", "PERFECT"]

        for key in required_keys:
            if key not in config:
                raise ValueError(f"No required key found: {key}")

        if config["WIDTH"] < 0 or config["HEIGHT"] < 0:
            raise ValueError(
                "Invalid width and height: must be equal or greater than 0")

        if not isinstance(config["ENTRY"], tuple):
            raise ValueError("Entry point must be a tuple (X,X)")

        if not isinstance(config["EXIT"], tuple):
            raise ValueError("Exit point must be a tuple (X,X)")

        if (config["ENTRY"] == config["EXIT"]):
            raise ValueError("Exit and Entry must be different.")

        if not isinstance(
         config["WIDTH"], int) or not isinstance(config["HEIGHT"], int):
            raise ValueError("Width and Height must be integers.")

        if not (isinstance(config["PERFECT"], bool)):
            raise ValueError(
                "Perfect value in config must be a bool (True or False)")

        if not (0 <= config["ENTRY"][0] < config["WIDTH"] and
           0 <= config["ENTRY"][1] < config["HEIGHT"]):
            raise ValueError("ENTRY fuera del mapa")

        if not (0 <= config["EXIT"][1] < config["WIDTH"] and
                0 <= config["EXIT"][0] < config["HEIGHT"]):
            raise ValueError("EXIT fuera del mapa")

        blocked_cells = self.blocked_42_zone(config["WIDTH"], config["HEIGHT"])
        if config["ENTRY"] in blocked_cells:
            raise ValueError(
                f"ENTRY {config['ENTRY']} is inside the blocked 42 coords")
        if config["EXIT"] in blocked_cells:
            raise ValueError(
                f"EXIT {config['EXIT']} is inside the blocked 42 coords")
