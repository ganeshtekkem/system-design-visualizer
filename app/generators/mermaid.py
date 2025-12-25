from app.generators.normalizer import normalize_node_id

def generate_mermaid(components: list[str]) -> str:
    lines=["graph TD"]
    normalized=[]

    for comp in components:
        node_id=normalize_node_id(comp)
        label=comp.strip()
        normalized.append((node_id, label))
    
    for i in range(len(normalized)-1):
        src_id, src_label = normalized[i]
        dst_id, dst_label = normalized[i+1]
        lines.append(f'    {src_id}["{src_label}"] --> {dst_id}["{dst_label}"]')


    return "\n".join(lines)