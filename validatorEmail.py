def isEmailValido(email: str) -> bool:
    if type(email) != str:
        raise ValueError(f"Email inserido não é uma string")

    if email == "" or not "@" in email:
        return False

    part1 = email.split("@")[0]
    part2, part3 = email.split("@")[1].split(".",1)

    for parte in part1.split("."):
        if parte == "" or not parte.isalnum:
            return False

    if part2 == "" or not parte.isalnum:
            return False 

    for parte in part3.split("."):
        if parte == "" or not parte.isalpha:
            return False

    return True