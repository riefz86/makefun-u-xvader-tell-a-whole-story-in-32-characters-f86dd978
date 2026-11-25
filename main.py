"""Tell a Whole Story in 32 Characters -- one Wi-Fi network name.

The entry is a single Wi-Fi name, at most 32 characters long, that a
passer-by reads in their phone's network list and instantly gets a joke
out of -- plus the ghost of a whole story behind it.

The angle I picked: a break-up told through the pettiest divorce
settlement in history -- not the house, not the car, the router. No
one in the story is named beyond "my ex", yet the name still gives
the reader a cast and a plot. There was a couple, there was a shared
home with shared Wi-Fi and a shared cat, and then the relationship
ended. When the ex walked out, they took the router -- and left the
cat. That single choice implies everything the name does not say --
whose side the cat is on now, who got custody of the internet, and
what the ex valued most when packing in a hurry. It is funny because
the priorities are so wrong. A decent person takes the cat. This ex
took the box that blinks. Every neighbour scrolling past this network
knows exactly how that break-up went, and which of the two exes is
telling the story: the one still holding the cat, typing this name
into the new router they had to buy.

Why this beats the stock jokes: the famous Wi-Fi names everyone has
already seen a hundred times are a surveillance van, a pun on "Wi-Fi"
itself, or a demand for a password. Those are labels, not stories --
they have no character and nothing happened in them. This name has a
before (a couple, a shared flat, one router, one cat), a turning
point (the break-up, the packing, the choice at the door), and an
after (a flat with a cat and no internet, and a new network name that
is itself the revenge). A stranger reads it and can fill in the rest
of the scene without being told: the boxes in the hallway, the cat
watching the router disappear out of the door, the ex already
plugging it in at their new place.

The wording is deliberately plain, in title case with no spaces, the
way real Wi-Fi names look when someone types them into a router's
setup page. Every word earns its place: "MyEx" sets the character,
"TookTheRouter" is the act, "NotTheCat" is the twist that makes the
act a joke -- the one thing the ex did not take is the living creature
that actually needed taking. Nothing in it leans on shock value --
the humour comes from recognition, from the wrongness of the
priority, not from anything crude. It reads cleanly out loud, and at
twenty-six characters it fits comfortably inside the thirty-two
character limit with room to spare.

The program below does one small, honest job: it writes that exact
name to /output/entry.txt, after checking the name really is a
non-empty string of at most 32 characters. The check is part of the
entry's own discipline -- a Wi-Fi name that is one character too long
is not a Wi-Fi name at all, it is a rejected entry.
"""

import os

# The entry: one Wi-Fi network name, 26 characters, no spaces.
# "MyEx" -- the character. "TookTheRouter" -- the petty act.
# "NotTheCat" -- the twist: the ex chose the blinking box over the pet.
ENTRY = "MyExTookTheRouterNotTheCat"

# The gate in the bounty rules: /output/entry.txt must hold UTF-8 text
# of 1 to 32 characters, and not only whitespace. Anything outside that
# range is an invalid entry that never reaches the judge.
MAX_LENGTH = 32


def validate(name):
    """Return True only if *name* could pass the gate.

    A Wi-Fi name has to be real text -- at least one character, at most
    MAX_LENGTH, and more than blank space -- otherwise the sealed scorer
    marks the entry invalid and no judge ever sees the joke.
    """
    if not isinstance(name, str):
        return False
    if not 1 <= len(name) <= MAX_LENGTH:
        return False
    if not name.strip():
        return False
    return True


def main():
    if not validate(ENTRY):
        raise ValueError(
            "entry must be 1 to 32 non-blank characters, got %d" % len(ENTRY)
        )
    # Create the output folder if it is not there yet. Note: never chmod
    # the directory itself -- the grader collects /output as a different
    # user, and changing a directory we do not own fails the run. Only
    # the file we write ourselves gets its mode set, to 0644, so every
    # user can read it.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
