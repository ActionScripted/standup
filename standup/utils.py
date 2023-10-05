def recursive_update(original, new_dict):
    """Recursively update dictionary."""
    updated = original.copy()

    for key, value in new_dict.items():
        if isinstance(value, dict):
            updated[key] = recursive_update(updated.get(key, {}), value)
        else:
            updated[key] = value

    return updated
