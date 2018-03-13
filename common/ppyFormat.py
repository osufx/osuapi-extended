def verticalSplit(data, scema):
    new_entries = []
    entries = data.rstrip().split(b"\n")
    for entry in entries:
        values = entry.split(b"|")
        new_entry = {}
        for i in range(0, len(values)):
            new_entry[scema[i]] = values[i].decode("utf-8")
        new_entries.append(new_entry)
    return new_entries