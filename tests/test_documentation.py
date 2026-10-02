from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_explainability_headings():
    text=(ROOT/"EXPLAINABILITY.md").read_text()
    for h in ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]: assert text.count(h)==1
    for h in ["## Inputs","## Decision","## Limits"]: assert f"\n{h}\n" not in text

def test_declared_skills_exist():
    import yaml
    manifest=yaml.safe_load((ROOT/"agent.yaml").read_text())
    for skill in manifest["skills"]: assert (ROOT/"skills"/skill/"SKILL.md").exists()

def test_declared_tools_exist():
    import yaml
    manifest=yaml.safe_load((ROOT/"agent.yaml").read_text())
    for tool in manifest["tools"]: assert (ROOT/"tools"/f"{tool.replace('-','_')}.py").exists()
