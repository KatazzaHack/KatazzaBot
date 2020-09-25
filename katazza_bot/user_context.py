from collections import defaultdict


class UserContext:
    length_minutes = None
    theme = None


contexts = defaultdict(UserContext)
