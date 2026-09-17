#!/usr/bin/env python3
import json, subprocess

def _run(cmd, timeout=240):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)

def _payload(spec, prompt):
    p={}; setp=False
    for prm in spec.get('parameters',[]):
        n=prm.get('name',''); l=n.lower(); req=bool(prm.get('required',False)); d=prm.get('default')
        if l in {'message','prompt','text','query','input','instruction','user_message'}:
            p[n]=prompt; setp=True
        elif l in {'chat_history','history','messages'}: p[n]=[]
        elif l in {'max_new_tokens','max_tokens','maximum_new_tokens'}: p[n]=700
        elif l=='temperature': p[n]=0.1
        elif l=='top_p': p[n]=0.9
        elif req and d is None: return None
    return p if setp else None

def invoke(space,prompt):
    info=_run(['hf-gradio','info',space],120)
    if info.returncode!=0: return False,'',{'stage':'info','error':(info.stderr or info.stdout)[-1200:]}
    try: api=json.loads(info.stdout)
    except Exception as e: return False,'',{'stage':'decode','error':repr(e)}
    pref=['/generate','/chat','/predict','/respond','/infer','/run']
    eps=list(api.items()); eps.sort(key=lambda kv:(pref.index(kv[0]) if kv[0] in pref else 99,kv[0]))
    errs=[]
    for ep,spec in eps:
        payload=_payload(spec,prompt)
        if payload is None: continue
        r=_run(['hf-gradio','predict',space,ep,json.dumps(payload,ensure_ascii=False)],240)
        if r.returncode==0 and (r.stdout or '').strip():
            raw=r.stdout.strip()
            try:
                obj=json.loads(raw)
                if isinstance(obj,dict):
                    for k in ('Response','response','text','output','message'):
                        if isinstance(obj.get(k),str): return True,obj[k].strip(),{'endpoint':ep}
            except: pass
            return True,raw,{'endpoint':ep}
        errs.append((r.stderr or r.stdout)[-700:])
    return False,'',{'stage':'predict','error':' | '.join(errs[-3:])}
