import subprocess,sys,json,pathlib
r=subprocess.run([sys.executable,"worker/visual_mvp.py"],check=False); assert r.returncode==0
x=json.loads(pathlib.Path("artifacts/visual_mvp.json").read_text()); assert x["passed"] and x["preserved_tbd"] and x["source_artifact"]=="F49-DEMO-001"
