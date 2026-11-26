import os

LINE = "Beautiful, but only works nights, vanishes for days, and still expects me to howl. One star."
OUT = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
