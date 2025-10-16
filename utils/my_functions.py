import re

def unify_column_names(name: str) -> str:
    """Converts column names to lowercase, replaces spaces/hyphens with underscores, and handles MultiIndex."""
    return (
        tuple(re.sub(r"[-\s]+", "_", str(n).lower()) for n in name)
        if isinstance(name, tuple)
        else re.sub(r"[-\s]+", "_", str(name).lower())
    )