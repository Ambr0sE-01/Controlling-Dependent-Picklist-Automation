import pandas as pd
import xml.etree.ElementTree as ET
import os
import shutil

EXCEL_FILE = "locations.xlsx"
INPUT_FILE = "metadata/customfields/Shipping_State__c.field-meta.xml"
OUTPUT_FILE = "metadata/customfields/Shipping_State__c.field-meta.updated.xml"
BACKUP_FILE = "metadata/customfields/Shipping_State__c.field-meta.backup.xml"

NAMESPACE = "http://soap.sforce.com/2006/04/metadata"
NS = {"sf": NAMESPACE}
ET.register_namespace("", NAMESPACE)


def indent(elem, level=0):
    i = "\n" + level * "    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        for child in elem:
            indent(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i


def update_dependencies(df, tree):
    root = tree.getroot()

    value_set = root.find("sf:valueSet", NS)
    if value_set is None:
        raise Exception("❌ <valueSet> not found!")

    # --------- KEEP THE EXISTING PICKLIST VALUES UNTOUCHED ---------

    # Remove old valueSettings only
    for vs in value_set.findall("sf:valueSettings", NS):
        value_set.remove(vs)

    # --------- ADD NEW VALUE SETTINGS BASED ON EXCEL ---------
    for i, row in df.iterrows():
        vs = ET.SubElement(value_set, f"{{{NAMESPACE}}}valueSettings")

        c = ET.SubElement(vs, f"{{{NAMESPACE}}}controllingFieldValue")
        c.text = row["Country"]

        vn = ET.SubElement(vs, f"{{{NAMESPACE}}}valueName")
        vn.text = row["State"]

    return tree


def main():
    print("Loading Excel…")
    df = pd.read_excel(EXCEL_FILE).drop_duplicates()

    print("Creating backup…")
    shutil.copyfile(INPUT_FILE, BACKUP_FILE)

    print("Reading metadata XML…")
    tree = ET.parse(INPUT_FILE)

    print("Updating dependencies… (labels + values remain unchanged)")
    updated_tree = update_dependencies(df, tree)

    print("Formatting XML…")
    indent(updated_tree.getroot())

    print("Saving updated file…")
    updated_tree.write(OUTPUT_FILE, encoding="UTF-8", xml_declaration=True)

    print("\n✅ DONE!")
    print(f"Backup created:  {BACKUP_FILE}")
    print(f"Updated file:   {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
