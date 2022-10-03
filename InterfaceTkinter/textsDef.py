langs = {
    "fr":r"InterfaceTkinter\Texts\fr.lang",
    "en":r"InterfaceTkinter\Texts\en.lang",
    "pt":r"InterfaceTkinter\Texts\pt.lang"
}

langInUse = "pt"

allTranslatedTexts = {}

def changerLanguage():
    langArq = open(langs[langInUse], "rt", encoding="utf-8")

    lines = langArq.read().split("\n")

    langArq.close()

    texts = {}
    i = 1
    for line in lines:
        if not (line.startswith("*") or line.strip() == ""):
            if "->" in line:
                name, value = line.split("->", 1)
                name, value = name.strip(), value.strip()

                texts.update(((name, value),))
            else:
                raise ErroDeSintaxe(f"Expected '->' in {langArq.name} {langs[langInUse]} line {i}")

        i += 1
    
    global allTranslatedTexts
    allTranslatedTexts = texts

class ErroDeSintaxe(SyntaxError):
    def __init__(self, *args) -> None:
        super().__init__(args)

changerLanguage()

if __name__ == "__main__":
    changerLanguage()
    print(allTranslatedTexts)