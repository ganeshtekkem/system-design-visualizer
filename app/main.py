from fastapi import FastAPI
from pydantic import BaseModel
from app.generators.extractor import extract_architecture_components
from app.llm.llm_client import generate_response
from app.generators.mermaid import generate_mermaid


app = FastAPI(title="AI System Design Visualizer")

class DesignRequest(BaseModel):
    system_name: str
    traffic: str

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/design")
def generate_design(request: DesignRequest):
    with open("app/prompts/system_design.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(
        system_name=request.system_name,
        traffic=request.traffic
    )
    design_text = generate_response(prompt)

    components = extract_architecture_components(design_text)
    architecture_mermaid = generate_mermaid(components) if components else "No components found."

    

    return {

        "system": request.system_name,
        "traffic": request.traffic,
        "design": design_text,
        "architecture_diagram": architecture_mermaid
        }
    
