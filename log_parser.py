def parse_can_log(file_path):
    
    frames = []

    with open(file_path, "r") as f:

        for line in f:

            parts = line.strip().split()

            if len(parts) < 3:
                continue

            frame_id = int(parts[1], 16)
            data = bytes.fromhex(parts[2])

            frames.append((frame_id, data))

    return frames