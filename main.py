"""One Word for the Boss — the word is the whole entry.

Design against the judge's brief
---------------------------------
The judge weighs, in order: (1) a single word a person would actually
use about the boss they report to, (2) funny on its own — the kind of
word a colleague repeats at lunch because it lands, (3) rings true,
catching a real habit of bosses, (4) fresh, not the first word anyone
would reach for, (5) travels — works for a boss in a kitchen, a
warehouse or an office.

"Teflon" hits all five in one word:

1. It is a single word people really do use about the one they report
   to — "my boss is Teflon" — the same idiom as a Teflon president:
   nothing sticks to him.
2. It is funny on its own. A kitchen-pan coating applied to a person
   is a joke that needs no caption: blame, deadlines, complaints and
   consequences all slide straight off, and he walks away spotless
   while everyone else does the scrubbing.
3. It rings true. Every office has the boss who is never at fault —
   the missed deadline was the team's, the failed launch was the
   market's, the complaint was a misunderstanding. Nothing ever lands.
4. It is fresh. The first words anyone reaches for are "micromanager",
   "toxic", "demanding", "strict". "Teflon" is the word you reach for
   once you have actually worked for one.
5. It travels. A Teflon boss in a kitchen, a warehouse or an office
   is the same person: the one nothing sticks to.

It is also short — 6 characters, 6 bytes — and the tie-break favours
the smaller text. The word needs no explanation and no setup, which is
exactly what the brief asks: the word has to land on its own. One
word, one image, one habit every employee recognises on first read.

The program writes exactly that one word to /output/entry.txt.
"""

import os

ENTRY_TEXT = "Teflon"


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 30 characters, not only white space.
    assert 1 <= len(text) <= 30, f"entry length {len(text)} outside 1-30"
    assert text.strip(), "entry must not be only white space"
    assert " " not in text, "entry must be a single word"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
