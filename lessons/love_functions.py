"""Practice."""


def love(name: str) -> str:
    """Give a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a repeated and loving message."""
    love_note: str = ""
    i: int = 0 
    while i < n:
        love_note += love(to) + "\n"
        i += 1 
    return love_note  