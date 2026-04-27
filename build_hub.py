import os

# 1. Build the polished index.html landing page
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Pedagogy & Curriculum Projects — Steve Schneider</title>
<style>
  :root {
    --bg: #fafaf8;
    --surface: #ffffff;
    --border: #c8c8c0;
    --text: #1a1a1a;
    --muted: #4a4a45;
    --accent: #1e4f78;
    --accent-hover: #153a5b;
    --serif: Georgia, 'Times New Roman', serif;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    max-width: 900px;
    margin: 0 auto;
    padding: 3rem 2rem;
    line-height: 1.6;
  }
  header {
    text-align: center;
    margin-bottom: 4rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--border);
  }
  h1 {
    font-family: var(--serif);
    font-weight: normal;
    color: var(--accent);
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
  }
  .subtitle {
    color: var(--muted);
    font-size: 1.2rem;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }
  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    display: flex;
    flex-direction: column;
  }
  .card h2 {
    font-family: var(--serif);
    color: var(--accent);
    margin-top: 0;
    font-size: 1.5rem;
  }
  .card p {
    flex-grow: 1;
    margin-bottom: 1.5rem;
  }
  .btn {
    display: inline-block;
    background: var(--accent);
    color: #ffffff;
    text-decoration: none;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    font-weight: 500;
    text-align: center;
    transition: background 0.2s;
  }
  .btn:hover {
    background: var(--accent-hover);
  }
  .btn-outline {
    background: transparent;
    color: var(--accent);
    border: 1px solid var(--accent);
  }
  .btn-outline:hover {
    background: #f0f4f8;
  }
  footer {
    margin-top: 5rem;
    text-align: center;
    color: var(--muted);
    font-size: 0.9rem;
    border-top: 1px solid var(--border);
    padding-top: 2rem;
  }
</style>
</head>
<body>

  <header>
    <h1>AI Pedagogy & Curriculum Projects</h1>
    <div class="subtitle">Steve Schneider · SUNY AI Fellow for the Public Good</div>
    <p style="max-width: 600px; margin: 1.5rem auto 0; color: var(--muted);">
      Operationalizing AI literacy through the RTW (Reading, Thinking, Writing) framework. Treating generative AI as a medium for literate practice, rather than merely a subject matter.
    </p>
  </header>

  <div class="grid">
    
    <div class="card">
      <h2>📚 AI Literacy Curriculum</h2>
      <p>The foundational conceptual development records and operative curriculum scaffolds designed for the SUNY AI literacy integration mandate.</p>
      <ul style="margin-top: 0; padding-left: 1.2rem; margin-bottom: 1.5rem; color: var(--muted);">
        <li><strong>Learner's Permit:</strong> 15-exercise foundational scaffold.</li>
        <li><strong>Agentic License:</strong> 15-exercise advanced operation scaffold.</li>
      </ul>
      <a href="conversations/00_index.html" class="btn">Enter the Conversation Archive</a>
    </div>

    <div class="card">
      <h2>⚙️ rss2zotero</h2>
      <p>An automated workflow and tool connecting higher-ed RSS feeds to Zotero for scholarly literature monitoring. Utilizes Claude to summarize articles relevant to AI and pedagogy.</p>
      <a href="https://github.com/stevesunypoly/rss2zotero" class="btn btn-outline">View GitHub Repository</a>
    </div>

    <div class="card">
      <h2>🚦 DesignWriteStudio / DWIT</h2>
      <p>A three-strand course architecture utilizing a Traffic Light constraint framework (Red/Yellow/Green AI constraints across Wikipedia, TiddlyWiki, and Wikiversity).</p>
      <a href="#" class="btn btn-outline" style="opacity: 0.6; cursor: default;">Coming Soon</a>
    </div>

  </div>

  <footer>
    <p>Developed at the Artificial Intelligence Exploration (AIX) Center · SUNY Polytechnic Institute</p>
  </footer>

</body>
</html>
"""

# 2. Build the README.md
readme_content = """# AI Pedagogy & Curriculum Projects

**Steve Schneider** | SUNY AI Fellow for the Public Good | Co-Director, AIX Center at SUNY Polytechnic Institute

This repository serves as the central hub for open-source AI pedagogy tools, curriculum scaffolds, and conceptual frameworks. The work herein operationalizes AI literacy through the **RTW (Reading, Thinking, Writing)** framework—treating generative AI as a medium for literate practice, rather than merely a subject matter.

---

## 📚 1. AI Literacy Curriculum Archive
*This repository contains the foundational generation transcripts and conceptual development records for the SUNY AI Literacy Curriculum.*

These Claude.ai design sessions produced:
* **The Learner's Permit (LP):** A 15-exercise foundational scaffold for AI literacy.
* **The Agentic License (CDL):** A 15-exercise scaffold for agentic AI operation.

**👉 [Explore the Curriculum Conversation Archive](https://stevesunypoly.github.io/ai-literacy-curriculum-archive/)**

---

## ⚙️ 2. rss2zotero
An automated workflow and tool connecting higher-ed RSS feeds to Zotero for scholarly literature monitoring. It polls feeds (Inside Higher Ed, EDUCAUSE, etc.), filters items by AI/pedagogy keywords, utilizes Claude for summarization, and pushes the results directly to a Zotero group library.

**👉 [View the rss2zotero Repository](https://github.com/stevesunypoly/rss2zotero)**

---

## 🚦 3. DesignWriteStudio / DWIT *(Coming Soon)*
A three-strand course architecture utilizing a Traffic Light framework (Red/Yellow/Green AI constraints across Wikipedia, TiddlyWiki, and Wikiversity).

---

### About the Project Context
These materials were developed in alignment with SUNY Board Resolution 2024-64 regarding AI literacy integration across 64 campuses. All materials are open and freely adaptable.
"""

# Write files
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Success! Overwrote README.md and created your new landing page (index.html).")
