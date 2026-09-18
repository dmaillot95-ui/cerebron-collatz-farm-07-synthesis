#!/usr/bin/env python3
"""CEREBRON Ω — SPIRALIX farm adapter v0.1.
Deterministic transport envelope. Retrieval/routing aid; never upgrades evidence.
"""
import json, hashlib

REQUIRED=("farm_id","domain","objective","method","evidence_level","validation","priority","task_type")
EVIDENCE={f"E{i}" for i in range(9)}

def encode(**kw):
    missing=[k for k in REQUIRED if k not in kw]
    if missing: raise ValueError("missing:"+",".join(missing))
    if kw["evidence_level"] not in EVIDENCE: raise ValueError("invalid evidence_level")
    x={"language":"SPIRALIX-OMEGA","layer":"GLYPH-VECTOR-OMEGA","vector":{k:kw[k] for k in REQUIRED},"payload":kw.get("payload",{})}
    raw=json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False)
    x["sha256"]=hashlib.sha256(raw.encode()).hexdigest()
    return x

def verify(x):
    y=dict(x); claimed=y.pop("sha256",None)
    raw=json.dumps(y,sort_keys=True,separators=(",",":"),ensure_ascii=False)
    return claimed==hashlib.sha256(raw.encode()).hexdigest()

def decode(x):
    if not verify(x): raise ValueError("HASH_MISMATCH")
    return x["vector"],x.get("payload",{})

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser(); p.add_argument("--farm",required=True); p.add_argument("--domain",required=True); a=p.parse_args()
    x=encode(farm_id=a.farm,domain=a.domain,objective="interop-self-test",method="deterministic-roundtrip",evidence_level="E2",validation="VERIFY",priority="normal",task_type="interop",payload={"claim":"transport test only"})
    v,payload=decode(x)
    assert v["farm_id"]==a.farm and payload["claim"]=="transport test only"
    print(json.dumps({"status":"VERIFIED","farm_id":a.farm,"sha256":x["sha256"]}))
