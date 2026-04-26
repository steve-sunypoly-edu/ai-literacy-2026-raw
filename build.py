import json
import zipfile
import os
import glob
import html
from datetime import datetime

try:
    import markdown
except ImportError:
    print("Error: Please install markdown first by running: pip3 install markdown")
    exit()

ordered_files = [
    "AI literacy development through iterative refinement",
    "AI-FYE document structure and course design",
    "AI integration across course levels",
    "AI literacy curriculum project invitation",
    "AI document edits and review",
    "The teacher, the student and the LLM",
    "Seeking feedback",
    "AI adoption in academic integrity and learning outcomes",
    "AI literacy progression framework",
    "Project memory update",
    "Project context report generation",
    "Processing podcast links with curriculum tagging"
]

zip_files = glob.glob("*.zip")
conversations = {}

for zp in zip_files:
    try:
        with zipfile.ZipFile(zp, 'r') as z:
            for filename in z.namelist():
                if not filename.endswith('.json') or 'export_summary' in filename:
                    continue
                with z.open(filename) as f:
                    try:
                        data = json.load(f)
                        name = data.get("name")
                        if name:
                            conversations[name] = data
                    except:
                        pass
    except Exception as e:
        pass

conversations_dir = "conversations"
os.makedirs(conversations_dir, exist_ok=True)
generated_files = []

for i, base_name in enumerate(ordered_files, 1):
    data = None
    for k, v in conversations.items():
        if base_name in k:
            data = v
            break
    
    if not data:
        print(f"Warning: Could not find raw JSON data for '{base_name}'")
        continue

    title = data.get("name", "Conversation")
    summary_md = data.get("summary", "No summary available.")
    
    summary_md = summary_md.replace("Steve Schneider", "The author").replace("steve schneider", "the author")
    summary_md = summary_md.replace("Steve", "the author").replace("steve", "the author")
    summary_html = markdown.markdown(summary_md)

    messages = data.get("chat_messages", data.get("messages", []))
    if not messages and isinstance(data, list):
        messages = data

    exchanges = []
    current_human = None

    for msg in messages:
        sender = msg.get("sender")
        content_blocks = msg.get("content", [])
        text = ""
        for block in content_blocks:
            if block.get("type") == "text":
                text += block.get("text", "")
                
        created_at_str = msg.get("created_at", "")
        try:
            dt = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            time_str = dt.strftime("%I:%M %p")
        except:
            time_str = ""

        if sender == "human":
            current_human = {"text": text, "time": time_str}
        elif sender == "assistant" and current_human:
            exchanges.append({
                "human": current_human,
                "assistant": {"text": text, "time": time_str}
            })
            current_human = None

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<style>
:root {{ --bg: #fafaf8; --surface: #ffffff; --border: #c8c8c0; --text: #1a1a1a; --muted: #4a4a45; --accent: #1e4f78; --prompt-bg: #f0f0ec; --ts-color: #5a5a55; --mono: 'Courier New', monospace; --serif: Georgia, serif; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg: #111110; --surface: #1c1c1a; --border: #3a3a34; --text: #e8e8e0; --muted: #b0b0a8; --accent: #7bbde8; --prompt-bg: #222220; }} }}
body {{ font-family: -apple-system, sans-serif; background: var(--bg); color: var(--text); max-width: 800px; margin: 0 auto; padding: 2rem; line-height: 1.6; }}
header {{ margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border); }}
h1 {{ font-family: var(--serif); font-weight: normal; margin: 0 0 0.5rem 0; color: var(--accent); }}
.summary-box {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-bottom: 2rem; }}
details {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; margin-bottom: 1rem; overflow: hidden; }}
summary {{ padding: 1rem; cursor: pointer; background: var(--prompt-bg); display: flex; justify-content: space-between; font-weight: 500; gap: 1rem; }}
summary::-webkit-details-marker {{ display: none; }}
.ptext {{ flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.ts {{ font-size: 0.85em; color: var(--ts-color); white-space: nowrap; }}
.exchange {{ padding: 1.5rem; border-top: 1px solid var(--border); }}
.full-prompt-block {{ background: var(--prompt-bg); padding: 1rem; border-radius: 4px; margin-bottom: 1.5rem; font-style: italic; white-space: pre-wrap; border-left: 4px solid var(--accent); }}
pre {{ background: var(--bg); padding: 1rem; border-radius: 4px; overflow-x: auto; font-family: var(--mono); font-size: 0.9em; }}
code {{ font-family: var(--mono); font-size: 0.9em; }}
blockquote {{ border-left: 3px solid var(--accent); margin: 0; padding-left: 1rem; color: var(--muted); }}
</style>
</head>
<body>
<header><h1>{html.escape(title)}</h1><p style="color: var(--muted);">AI Literacy Curriculum Project — Generated Record</p></header>
<div class="summary-box">{summary_html}</div>
"""

    for ex in exchanges:
        human_text = ex["human"]["text"]
        clean_human_text = human_text.replace('\n', ' ').strip()
        short_prompt = clean_human_text[:1000] + ("..." if len(clean_human_text) > 1000 else "")
        if not short_prompt: short_prompt = "[Attachment or Voice Input]"
        
        full_prompt_html = f"<div class='full-prompt-block'><strong>Full Prompt:</strong><br>{html.escape(human_text)}</div>"
        assistant_html = markdown.markdown(ex["assistant"]["text"], extensions=['fenced_code', 'tables'])
        
        html_template += f"""<details><summary><span class="ptext">{html.escape(short_prompt)}</span><span class="ts">{ex["human"]["time"]}</span></summary>
        <div class="exchange">{full_prompt_html}{assistant_html}</div></details>\n"""

    html_template += "<footer><p>AIX Center · SUNY Polytechnic Institute</p></footer></body></html>"

    clean_name = base_name.replace(" ", "_").replace(",", "").python3 -c '
import json, zipfile, os, glob, html
from datetime import datetime
import markdown

ordered = ["AI literacy development through iterative refinement", "AI-FYE document structure and course design", "AI integration across course levels", "AI literacy curriculum project invitation", "AI document edits and review", "The teacher, the student and the LLM", "Seeking feedback", "AI adoption in academic integrity and learning outcomes", "AI literacy progression framework", "Project memory update", "Project context report generation", "Processing podcast links with curriculum tagging"]

convs = {}
for zp in glob.glob("*.zip"):
    try:
        with zipfile.ZipFile(zp, "r") as z:
            for fn in z.namelist():
                if fn.endswith(".json") and "export_summary" not in fn:
                    with z.open(fn) as f:
                        try:
                            d = json.load(f)
                            if d.get("name"): convs[d["name"]] = d
                        except: pass
    except: pass

os.makedirs("conversations", exist_ok=True)
gen_files = []

for i, b in enumerate(ordered, 1):
    d = next((v for k, v in convs.items() if b in k), None)
    if not d: continue
    
    t = d.get("name", "Conversation")
    s_md = d.get("summary", "").replace("Steve Schneider", "The author").replace("steve schneider", "the author").replace("Steve", "the author").replace("steve", "the author")
    s_html = markdown.markdown(s_md)
    
    msgs = d.get("chat_messages", d.get("messages", []))
    if not msgs and isinstance(d, list): msgs = d
    
    exchanges, cur = [], None
    for m in msgs:
        txt = "".join(blk.get("text", "") for blk in m.get("content", []) if blk.get("type") == "text")
        try: ts = datetime.strptime(m.get("created_at", ""), "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%I:%M %p")
        except: ts = ""
        if m.get("sender") == "human": cur = {"text": txt, "time": ts}
        elif m.get("sender") == "assistant" and cur:
            exchanges.append({"human": cur, "assistant": {"text": txt, "time": ts}})
            cur = None

    out = f"<!DOCTYPE html><html><head><meta charset=\\"UTF-8\\"><title>{html.escape(t)}</title><style>:root{{--bg:#fafaf8;--surface:#ffffff;--border:#c8c8c0;--text:#1a1a1a;--muted:#4a4a45;--accent:#1e4f78;--prompt-bg:#f0f0ec;--ts-color:#5a5a55;--mono:monospace;--serif:Georgia,serif;}}body{{font-family:sans-serif;background:var(--bg);color:var(--text);max-width:800px;margin:0 auto;padding:2rem;line-height:1.6;}}header{{border-bottom:1px solid var(--border);padding-bottom:1rem;margin-bottom:2rem;}}h1{{font-family:var(--serif);font-weight:normal;color:var(--accent);margin:0;}}.summary-box{{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:1.5rem;margin-bottom:2rem;}}details{{background:var(--surface);border:1px solid var(--border);border-radius:8px;margin-bottom:1rem;}}summary{{padding:1rem;cursor:pointer;background:var(--prompt-bg);display:flex;justify-content:space-between;font-weight:500;gap:1rem;}}summary::-webkit-details-marker{{display:none;}}.ptext{{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}.ts{{color:var(--ts-color);white-space:nowrap;}}.exchange{{padding:1.5rem;border-top:1px solid var(--border);}}.full-prompt-block{{background:var(--prompt-bg);padding:1rem;border-radius:4px;margin-bottom:1.5rem;font-style:italic;white-space:pre-wrap;border-left:4px solid var(--accent);}}pre{{background:var(--bg);padding:1rem;border-radius:4px;overflow-x:auto;}}blockquote{{border-left:3px solid var(--accent);padding-left:1rem;color:var(--muted);margin:0;}}</style></head><body><header><h1>{html.escape(t)}</h1><p style=\\"color:var(--muted);\\">AI Literacy Curriculum Project — Generated Record</p></header><div class=\\"summary-box\\">{s_html}</div>"
    
    for ex in exchanges:
        hx = ex["human"]["text"]
        cx = hx.replace("\\n", " ").strip()
        sp = cx[:1000] + ("..." if len(cx) > 1000 else "") or "[Attachment or Voice Input]"
        fh = f"<div class=\\"full-prompt-block\\"><strong>Full Prompt:</strong><br>{html.escape(hx)}</div>"
        ah = markdown.markdown(ex["assistant"]["text"], extensions=["fenced_code", "tables"])
        out += f"<details><summary><span class=\\"ptext\\">{html.escape(sp)}</span><span class=\\"ts\\">{ex["human"]["time"]}</span></summary><div class=\\"exchange\\">{fh}{ah}</div></details>"
        
    out += "<footer><p>AIX Center · SUNY Polytechnic Institute</p></footer></body></html>"
    
    nn = f"{i:02d}_{b.replace(" ", "_").replace(",", "").replace("-", "_").lower()}.html"
    with open(os.path.join("conversations", nn), "w") as f: f.write(out)
    gen_files.append((b, nn))

idx = "<!DOCTYPE html><html><head><meta charset=\\"UTF-8\\"><title>Index</title><style>body{font-family:sans-serif;max-width:800px;margin:0 auto;padding:2rem;line-height:1.6;color:#1a1a1a;background:#fafaf8;}h1{font-family:Georgia,serif;color:#1e4f78;border-bottom:1px solid #c8c8c0;padding-bottom:1rem;}.index-list{background:#ffffff;border:1px solid #c8c8c0;border-radius:8px;padding:2rem;}li{margin-bottom:1rem;}a{color:#1e4f78;text-decoration:none;font-weight:500;}a:hover{text-decoration:underline;}</style></head><body><h1>AI Literacy Project — Conversation Archive</h1><div class=\\"index-list\\"><ol>"
for b, nn in gen_files: idx += f"<li><a href=\\"{nn}\\">{b}</a></li>"
with open(os.path.join("conversations", "00_index.html"), "w") as f: f.write(idx + "</ol></div></body></html>")

rm = """# AI Literacy Curriculum Archive

This repository contains the foundational generation transcripts and conceptual development records for the AI Literacy Curriculum at SUNY Polytechnic Institute.

## Contents
The `conversations/` directory contains 12 chronologically ordered, verbatim HTML exports of the Claude.ai sessions used to design the curricula. 

These sessions produced:
1. **The Learner's Permit (LP):** A 15-exercise foundational scaffold for AI literacy.
2. **The Agentic License (Commercial Driver's License):** A 15-exercise scaffold for agentic AI operation.

To explore the archive, open `conversations/00_index.html` in any web browser.

## Project Context
These materials were developed by the author as part of the SUNY AI Fellows for the Public Good initiative, aligning with SUNY Board Resolution 2024-64 regarding AI literacy integration.
"""
with open("README.md", "w") as f: f.write(rm)
with open(".gitignore", "w") as f: f.write("*.zip\\n*.json\\n")
print("Repository built locally!")
'
