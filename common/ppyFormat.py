def verticalSplit(data, scema):
    data = data.rstrip() # Remove the extra newline (if it exists)

    if b"\n" in data:
        new_entries = []
        entries = data.split(b"\n")
        for entry in entries:
            values = entry.split(b"|")
            new_entry = {}
            for i in range(0, len(values)):
                new_entry[scema[i]] = values[i].decode("utf-8")
            new_entries.append(new_entry)
        return new_entries
    else:
        values = data.split(b"|")
        entry = {}
        for i in range(0, len(values)):
            entry[scema[i]] = values[i].decode("utf-8")
        return entry