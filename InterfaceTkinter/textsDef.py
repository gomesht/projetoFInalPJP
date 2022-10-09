import tkinter as tk

langs = {
    "fr":r"InterfaceTkinter\Texts\fr.lang",
    "en":r"InterfaceTkinter\Texts\en.lang",
    "pt":r"InterfaceTkinter\Texts\pt.lang"
}

langInUse = "pt"

allTranslatedTexts = {}

def changerLanguage(master, língua = None):
    if not língua == None:
        global langInUse
        langInUse = língua

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

                value = value.replace(r"\n", "\n")

                texts.update(((name, value),))
            else:
                raise ErroDeSintaxe(f"Expected '->' in {langArq.name} {langs[langInUse]} line {i}")

        i += 1

    global allTranslatedTexts
    
    if allTranslatedTexts == {}:
        for i in range(0, len(texts)):
            allTranslatedTexts.update(((   tuple(texts.keys())[i] , tk.StringVar(master=master, value=tuple(texts.values())[i])   ),))
    else:
        for i in range(0, len(texts)):
            tuple(allTranslatedTexts.values())[i].set(tuple(texts.values())[i])

class ErroDeSintaxe(SyntaxError):
    def __init__(self, *args) -> None:
        super().__init__(args)

if __name__ == "__main__":
    ...