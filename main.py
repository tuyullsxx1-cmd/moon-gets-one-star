import os

LINE = "Beautiful, but only works nights, vanishes for days, and still expects me to howl. One star."


def main():
    os.makedirs("/output", exist_ok=True)
    # single line, no trailing newline: the gate counts every character
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
