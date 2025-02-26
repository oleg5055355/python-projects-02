
import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    """Run the Spongecase program."""
    print('''sPoNgEtExT

eNtEr YoUr MeSsAgE:''')
    spongecase = englishToSpongecase(input('> '))
    print()
    print(spongecase)

    try:
        pyperclip.copy(spongecase)
        print('(cOpIed SpOnGeCasE to ClIpbOaRd.)')
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def englishToSpongecase(message):
    """Return the spongecase form of the given string."""
    spongecase = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongecase += character
            continue

        if useUpper:
            spongecase += character.upper()
        else:
            spongecase += character.lower()

        # Flip the case, 90% of the time.
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper  # Flip the case.
    return spongecase


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
