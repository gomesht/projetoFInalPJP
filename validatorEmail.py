def isEmailValido(email: str) -> bool:
    """ 
    Automaticamente analisa se um email é válido ou não \n
    ATENÇÃO: Remova todos os espaços no começo e no fim da string antes usar este método senão o resultado será False
    """

    if type(email) != str:
        raise ValueError(f"Email inserido não é uma string")

    if email == "" or not "@" in email:
        return False

    if " " in email:
        return False

    try:
        part1 = email.split("@")[0]
        part2, part3 = email.split("@")[1].split(".",1)
    except:
        return False

    for parte in part1.split("."):
        if parte == "" or not parte.isalnum:
            return False

    if part2 == "" or not parte.isalnum:
            return False 

    for parte in part3.split("."):
        if parte == "" or not parte.isalpha:
            return False

    return True