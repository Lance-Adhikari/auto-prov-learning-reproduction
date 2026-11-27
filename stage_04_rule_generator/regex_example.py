"""Extract individual fields from a sample log using regex."""

import re


def main():
    log = r"""Process ID: 9234
Process Name: C:\Program Files\Microsoft\Word\WINWORD.EXE
Object ID: 6612
Object Name: C:\Users\Lance\Documents\essay.docx
Accesses: ReadData
Time: 09:15:27"""

    patterns = {
        "Sid": r"^Process ID:[ \t]*(\d+)[ \t]*$",
        "Sname": r"^Process Name:[ \t]*([^\r\n]+)$",
        "Did": r"^Object ID:[ \t]*(\d+)[ \t]*$",
        "Dname": r"^Object Name:[ \t]*([^\r\n]+)$",
        "Itype": r"^Accesses:[ \t]*(\w+)[ \t]*$",
        "time": r"^Time:[ \t]*(\d{2}:\d{2}:\d{2})[ \t]*$"
    }

    # Capture raw field values before interaction-label normalization.
    for field, pattern in patterns.items():
        match = re.search(pattern, log.replace("\r\n", "\n"), re.MULTILINE)
        if match:
            print(field, "=", match.group(1))


if __name__ == "__main__":
    main()
