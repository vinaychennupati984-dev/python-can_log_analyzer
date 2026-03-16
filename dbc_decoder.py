import cantools

def load_dbc(dbc_file):

    db = cantools.database.load_file(dbc_file)

    return db


def decode_frame(db, frame_id, data):

    try:

        message = db.get_message_by_frame_id(frame_id)

        decoded = message.decode(data)

        return decoded

    except Exception:

        return {}