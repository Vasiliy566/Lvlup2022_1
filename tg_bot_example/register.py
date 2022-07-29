def create_user(telegram_id, name, email):
    with open("users.txt", mode="w") as f:
        f.write(f"{telegram_id} | {name} | {email}")


def is_user_exists(telegram_id):
    with open("users.txt") as f:
        for line in f.readlines():
            # f"123 | ivanov | example@mail.ru"
            saved_tg_id = line.split("|")[0].strip()
            if saved_tg_id == str(telegram_id):
                return True
        return False

