from core.configs import telegram


def admin(func):
    def wrapped(*args):
        if args[0].chat.id in telegram.ADMIN_IDS:
            func(*args)

    return wrapped
