from compressor import compress


# (Decompression)
def decompress(tags):
    decompressed_text = []

    for pos, length, next_symbol in tags:
        
        if pos > 0 and length > 0:
            start_index = len(decompressed_text) - pos
            for i in range(length):
                decompressed_text.append(decompressed_text[start_index + i])

        if next_symbol != "":
            decompressed_text.append(next_symbol)

    return "".join(decompressed_text)


# (File Handling)
def write_tags_to_file(tags, filename="file2.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for pos, length, symbol in tags:
            file.write(f"{pos},{length},{symbol}\n")


def read_tags_from_file(filename="file2.txt"):
    tags = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\r\n")
            if not line:
                continue

            parts = line.split(",")
            pos = int(parts[0])
            length = int(parts[1])
            symbol = parts[2] if len(parts) > 2 else ""

            tags.append((pos, length, symbol))
    return tags

