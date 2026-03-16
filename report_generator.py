import xml.etree.ElementTree as ET

def generate_xml_report(results):

    root = ET.Element("TestReport")

    total = len(results)
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = total - passed

    summary = ET.SubElement(root, "Summary")

    ET.SubElement(summary, "TotalSignals").text = str(total)
    ET.SubElement(summary, "Passed").text = str(passed)
    ET.SubElement(summary, "Failed").text = str(failed)

    for item in results:

        testcase = ET.SubElement(root, "TestCase")

        ET.SubElement(testcase, "FrameID").text = str(item["frame_id"])
        ET.SubElement(testcase, "Signal").text = item["signal"]
        ET.SubElement(testcase, "Value").text = str(item["value"])
        ET.SubElement(testcase, "Result").text = item["status"]

    tree = ET.ElementTree(root)

    tree.write("report.xml")