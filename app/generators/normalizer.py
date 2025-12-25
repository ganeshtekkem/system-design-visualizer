import re

def normalize_node_id(name: str) -> str:
    name=name.strip()

    name = re.sub(r"\(.*?\)", "", name)

    name = re.sub(r"[^a-zA-Z0-9_ ]", "", name)

    name=name.replace(" ","_")

    return name if name else "Unnamed_Node"

