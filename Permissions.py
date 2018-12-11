class Permissions:
    # Определение групп прав пользователей
    Guest = 0
    Anyone = 0
    Default = Guest
    User = 1
    Admin = 2
    Console = 3
    Perms = ("Guest", "User", "Admin", "Console")
