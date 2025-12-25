import re

def extract_architecture_components(design_text: str) -> list[str]:
    """
    Extracts architecture components from LLM output in a tolerant way.
    Handles numbering, bullets, and markdown formatting.
    """
    components = []

    # Normalize markdown bold
    text = design_text.replace("**", "")

    # Find architecture section
    match = re.search(r"ARCHITECTURE_COMPONENTS:(.*?)(API_DESIGN:|DATABASE:|SCALING:|BOTTLENECKS:|$)", text, re.S)
    if not match:
        return []

    section = match.group(1)

    for line in section.splitlines():
        line = line.strip()
        if not line:
            continue

        # Match: "1. Component", "- Component"
        numbered = re.match(r"\d+\.\s+(.*)", line)
        dashed = re.match(r"-\s+(.*)", line)

        if numbered:
            components.append(numbered.group(1).strip())
        elif dashed:
            components.append(dashed.group(1).strip())

    return components