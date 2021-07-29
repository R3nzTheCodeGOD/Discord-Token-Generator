class FileSystem:
    def create_file() -> None:
        with open(f"Token.txt", "a", encoding="utf-8"): pass
        with open(f"Blacklist.txt", "a", encoding="utf-8"): pass

    def write_token(text: str) -> None:
        with open(f"Token.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")

    def write_blacklist(text: str) -> None:
        with open(f"Blacklist.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")

    def read_blacklist() -> list[str]:
        with open(f"Blacklist.txt", "r", encoding="utf-8") as f:
            return f.read().split()