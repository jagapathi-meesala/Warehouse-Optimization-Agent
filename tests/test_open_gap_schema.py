from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]

def test_manifest_open_gap_core_rules():
    m=yaml.safe_load((ROOT/"agent.yaml").read_text())
    assert m["spec_version"]=="0.1.0"
    assert m["name"]=="warehouse-optimization-agent"
    assert set(m)-{"spec_version","name","version","description","license","skills","tools","runtime","tags","metadata"}==set()
    assert all(" " not in s and s==s.lower() for s in m["skills"]+m["tools"])
    assert all((ROOT/"skills"/f"{s}.md").exists() for s in m["skills"])
