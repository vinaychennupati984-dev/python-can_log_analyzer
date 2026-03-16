import xml.etree.ElementTree as ET


def generate_xml_report(decoded_frames, errors):

    root = ET.Element("TestReport")

    signals_node = ET.SubElement(root, "Signals")

    for frame in decoded_frames:

        frame_node = ET.SubElement(signals_node, "Frame")

        for signal, value in frame.items():

            sig = ET.SubElement(frame_node, signal)

            sig.text = str(value)

    errors_node = ET.SubElement(root, "Errors")

    for err in errors:

        e = ET.SubElement(errors_node, "Error")

        e.text = err

    tree = ET.ElementTree(root)

    tree.write("report.xml")