import cantools

def load_dbc(dbc_file):

    db = cantools.database.load_file(dbc_file)

    return db


def decode_frame(db, can_id, data):

    try:
        decoded = db.decode_message(can_id, data)

        return decoded

    except:

        return {}