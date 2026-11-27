"""Simplified Stage 3 CPE/PDB - educational, not GPT-4o CPE.
"""
def parse_fields(raw_log):
    fields = {}
    for line in raw_log.splitlines():
        line = line.strip()
        if ":" in line:
            # Split once so colons in paths and times remain intact.
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def majority_vote(directions):
    """Return the most frequent direction, choosing the first seen on a tie."""
    if not directions:
        raise ValueError("At least one direction vote is required.")
    counts = {}
    for direction in directions:
        if direction not in counts:
            counts[direction] = 0
        counts[direction] = counts[direction] + 1
    # Dictionary order makes ties deterministic.
    return max(counts, key=counts.get)


def extract_components(raw_log, votes):
    f = parse_fields(raw_log)
    sid, sname = f.get("Process ID"), f.get("Process Name")
    did, dname = f.get("Object ID"), f.get("Object Name")
    access, time = f.get("Accesses"), f.get("Time")
    if not all([sid, sname, did, dname, access, time]):
        return None
    if access == "ReadData":
        itype = "READ"
    elif access == "WriteData":
        itype = "WRITE"
    else:
        return None
    # Entity types and names are indexed by their IDs.
    V_l = {sid: "process", did: "file"}
    N_l = {sid: sname, did: dname}
    # Votes are supplied examples, not model-generated predictions.
    direction = majority_vote(votes)
    if direction == sid + "->" + did:
        E_l = {"Sid": sid, "Did": did, "Itype": itype, "time": time}
    elif direction == did + "->" + sid:
        E_l = {"Sid": did, "Did": sid, "Itype": itype, "time": time}
    else:
        raise ValueError("Invalid direction vote")
    return E_l, V_l, N_l


def build_record(E_l, V_l, N_l):
    sid, did = E_l["Sid"], E_l["Did"]
    return {
        "Sid": sid, "Stype": V_l[sid], "Sname": N_l[sid],
        "Did": did, "Dtype": V_l[did], "Dname": N_l[did],
        "Itype": E_l["Itype"], "time": E_l["time"]
    }


def main():
    log = r"""Event ID: 4663
Process ID: 7210
Process Name: C:\Windows\System32\powershell.exe
Object ID: 5542
Object Name: C:\Users\Lance\Documents\config.txt
Accesses: WriteData
Time: 14:42:31"""
    votes = ["7210->5542"] * 5 + ["5542->7210"] * 2
    E_l, V_l, N_l = extract_components(log, votes)
    PDB = {"log_001": [build_record(E_l, V_l, N_l)]}
    print("V_l =", V_l)
    print("N_l =", N_l)
    print("E_l =", E_l)
    print("PDB =", PDB)

if __name__ == "__main__":
    main()
