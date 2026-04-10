from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    # === TODO ===
    return set(mapping.keys())
    pass
    # === END TODO ===


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    # === TODO ===
    return set(mapping.values())
    pass
    # === END TODO ===


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    # === TODO ===
    for value in mapping.values():
        if value not in target:
            return False
    return True
    pass
    # === END TODO ===


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
    # === TODO ===
    s = set()
    for value in mapping.values():
        if value in s:
            return False
        s.add(value)
    return True
    pass
    # === END TODO ===


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
    # === TODO ===
    for value in mapping.values():
        if value not in mapping.keys():
            return False
    return True
    pass
    # === END TODO ===


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===
