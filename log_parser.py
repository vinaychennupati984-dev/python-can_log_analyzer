def parse_can_log(file_path):
    
    frames = []

    with open(file_path) as f:
        for line in f:

            parts = line.strip().split()

            can_id = int(parts[0], 16)

            data = bytes(int(x, 16) for x in parts[2:])

            frames.append((can_id, data))

    return frames