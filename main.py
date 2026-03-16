import argparse

from config_loader import load_config
from log_parser import parse_can_log
from dbc_decoder import load_dbc, decode_frame
from validator import validate_signals
from report_generator import generate_xml_report
from logger import setup_logger

logger = setup_logger()


def process_can_logs(log_file, dbc_file, rules):

    db = load_dbc(dbc_file)

    frames = parse_can_log(log_file)

    results = []

    for frame_id, data in frames:

        decoded = decode_frame(db, frame_id, data)

        validation = validate_signals(decoded, rules)

        for signal, status in validation.items():

            results.append({
                "frame_id": hex(frame_id),
                "signal": signal,
                "value": decoded[signal],
                "status": status
            })

    return results, len(frames)


def main():

    parser = argparse.ArgumentParser(description="Python CAN Log Analyzer")

    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--log")
    parser.add_argument("--dbc")

    args = parser.parse_args()

    config = load_config(args.config)

    log_file = args.log if args.log else config["log_file"]
    dbc_file = args.dbc if args.dbc else config["dbc_file"]

    rules = config["signals"]

    print("Starting CAN Log Analyzer...")
    print(f"Using DBC file: {dbc_file}")
    print(f"Reading CAN log: {log_file}")

    logger.info("Starting CAN Log Analyzer")

    results, frame_count = process_can_logs(log_file, dbc_file, rules)

    print(f"{frame_count} CAN frames parsed")

    generate_xml_report(results)

    print("XML report generated: report.xml")
    print("Execution completed successfully")

    logger.info("Execution completed")


if __name__ == "__main__":
    main()