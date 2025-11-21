def safe_print(*args, **kwargs):
    try:
        print(*args, **kwargs)
    except Exception:
        pass
