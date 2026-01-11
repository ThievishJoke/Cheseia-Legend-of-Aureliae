import re

class Formatting:
     # === Basic ===
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"

    WHITE = "\033[38;2;255;255;255m"
    GRAY = "\033[38;2;128;128;128m"
    BLACK = "\033[38;2;0;0;0m"
    RED = "\033[38;2;255;0;0m"
    DARK_RED = "\033[38;2;139;0;0m"
    GREEN = "\033[38;2;0;255;0m"
    DARK_GREEN = "\033[38;2;0;128;0m"
    BLUE = "\033[38;2;0;0;255m"
    CYAN = "\033[38;2;0;255;255m"
    AQUA = "\033[38;2;0;255;255m"
    TEAL = "\033[38;2;0;128;128m"
    TURQUOISE = "\033[38;2;64;224;208m"
    LIGHT_BLUE = "\033[38;2;173;216;230m"
    PURPLE = "\033[38;2;128;0;128m"
    LIGHT_PURPLE = "\033[38;2;200;162;255m"
    MAGENTA = "\033[38;2;228;94;183m"
    PINK = "\033[38;2;240;163;196m"
    YELLOW = "\033[38;2;255;255;0m"
    GOLD = "\033[38;2;255;215;0m"
    ORANGE = "\033[38;2;212;128;39m"

    # === Thematic ===
    FIRE = "\033[38;2;255;85;0m"
    WATER = "\033[38;2;0;170;255m"
    EARTH = "\033[38;2;139;69;19m"
    AIR = "\033[38;2;200;200;255m"
    LIGHT = "\033[38;2;255;255;224m"
    DARK = "\033[38;2;90;0;120m"
    BLOOD = "\033[38;2;170;0;0m"
    
    # === Utility ===
    def color_text(text, color):
        """Convenient inline color helper"""
        return f"{color}{text}{Formatting.RESET}"
    
    @staticmethod
    def title_colored(text: str) -> str:
        """
        Applies .title() to visible text while preserving ANSI color codes.
        Example:
            Formatting.title_colored(f"{Formatting.PURPLE} the subtle dust chokes. {Formatting.RESET}")
        """
        ansi_pattern = r'\033\[[0-9;]*m'
        segments = re.split(ansi_pattern, text)
        codes = re.findall(ansi_pattern, text)

        titled_segments = [seg.title() for seg in segments]

        # Recombine text and ANSI codes in order
        result = titled_segments[0]
        for code, seg in zip(codes, titled_segments[1:]):
            result += code + seg
        return result