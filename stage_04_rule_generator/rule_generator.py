"""Simplified Stage 4 Rule Generator/RDB - educational.
Auto-Prov uses LLaMA-3 to induce field-wise regex; these teaching
rules are manually defined for one controlled log format.
"""
import re

RDB = {
    "windows_file_access_4663": {
        "Sid": r"^Process ID:[ \t]*(\d+)[ \t]*$",
        "Sname": r"^Process Name:[ \t]*([^\r\n]+)$",
        "Did": r"^Object ID:[ \t]*(\d+)[ \t]*$",
        "Dname": r"^Object Name:[ \t]*([^\r\n]+)$",
        "Itype": r"^Accesses:[ \t]*(\w+)[ \t]*$",
        "time": r"^Time:[ \t]*(\d{2}:\d{2}:\d{2})[ \t]*$"
    }
}


def extract(pattern, log):
    match = re.search(pattern, log.replace("\r\n", "\n"), re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def apply_rules(log, rules):
    result = {}
    for field, pattern in rules.items():
        result[field] = extract(pattern, log)
    # Reject incomplete records before normalizing interaction labels.
    if not all(result.get(field) for field in ("Sid", "Sname", "Did", "Dname", "Itype", "time")):
        return None
    if result["Itype"] == "ReadData":
        result["Itype"] = "READ"
    elif result["Itype"] == "WriteData":
        result["Itype"] = "WRITE"
    else:
        return None
    # Known types for this controlled teaching format.
    result["Stype"] = "process"
    result["Dtype"] = "file"
    return {
        "Sid": result["Sid"], "Stype": result["Stype"],
        "Sname": result["Sname"], "Did": result["Did"],
        "Dtype": result["Dtype"], "Dname": result["Dname"],
        "Itype": result["Itype"], "time": result["time"]
    }


def main():
    new_logs = [
        r"""Event ID: 4663
Process ID: 8888
Process Name: C:\Windows\System32\notepad.exe
Object ID: 7712
Object Name: C:\Users\Lance\Documents\homework.txt
Accesses: WriteData
Time: 18:22:10""",
        r"""Event ID: 4663
Process ID: 9234
Process Name: C:\Program Files\Microsoft\Word\WINWORD.EXE
Object ID: 6612
Object Name: C:\Users\Lance\Documents\essay.docx
Accesses: ReadData
Time: 09:15:27"""
    ]
    rules = RDB["windows_file_access_4663"]
    print("RDB =", RDB)
    for i, log in enumerate(new_logs, 1):
        print("Record", i, "=", apply_rules(log, rules))

if __name__ == "__main__":
    main()
