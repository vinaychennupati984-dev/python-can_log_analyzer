from log_parser import parse_can_log
from dbc_decoder import load_dbc, decode_frame
from validator import build_validation_rules, validate_signals
from report_generator import generate_xml_report
from logger import setup_logger

logger = setup_logger()


def main():

    logger.info("Starting CAN log analyzer")

    dbc_file = "vehicle.dbc"
    log_file = "sample_log.txt"

    db = load_dbc(dbc_file)

    logger.info("DBC loaded")

    rules = build_validation_rules(db)

    frames = parse_can_log(log_file)

    logger.info(f"{len(frames)} frames parsed")

    decoded_frames = []

    errors = []

    for can_id, data in frames:

        logger.info(f"Decoding frame ID {hex(can_id)}")

        decoded = decode_frame(db, can_id, data)

        if decoded:

            decoded_frames.append(decoded)

            err = validate_signals(decoded, rules)

            if err:
                logger.error(err)

            errors.extend(err)

    generate_xml_report(decoded_frames, errors)

    logger.info("XML report generated")


if __name__ == "__main__":

    main()