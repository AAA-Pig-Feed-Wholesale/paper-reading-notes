#!/usr/bin/env python3
"""为《jev_925.md》笔记生成 7 张结构化配图（HTML -> Playwright 截图 PNG）。

用法: python build_figures.py
输出: 同目录下 fig1..fig7 七张 PNG（2x 高清）。
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

OUT_DIR = Path(__file__).resolve().parent
WIDTH = 1240

# 延续 9.18 批次米色纸感；角色色：Code=墨灰 slate，Jev=低饱和朱砂 blush，LLM=低饱和青绿 qing
BASE_CSS = """
:root{--bg:#f5f2eb;--paper:#fdfbf6;--ink:#292c2a;--dark:#233b3c;--text:#383c38;
--muted:#71766f;--edge:#dddcd0;--dai:#334f50;--qing:#567d72;--celadon:#e8f0e9;
--ochre:#a77e4b;--blush:#a6675e;--slate:#55605c;--violet:#796e82}
*{box-sizing:border-box;margin:0}
body{background:var(--bg);font:15px/1.62 "Noto Sans CJK SC","Source Han Sans SC","Microsoft YaHei",system-ui,sans-serif;color:var(--text);
padding:34px 40px 26px;width:1240px}
.overline{letter-spacing:.22em;font:600 11px/1.2 Georgia,serif;color:var(--qing);text-transform:uppercase}
.overline .no{color:var(--blush);margin-right:10px}
h1{font-size:29px;font-weight:750;letter-spacing:-.03em;line-height:1.28;color:var(--dark);margin:11px 0 9px;max-width:1120px}
.thesis{margin:12px 0 18px;border-left:4px solid var(--blush);background:#eeeae2;padding:12px 17px;
font-size:15px;color:#3a4540;border-radius:0 8px 8px 0}
.thesis b{color:#874b44}
.foot{margin-top:16px;padding-top:11px;border-top:1px dashed #cbc9bc;color:#8a8d83;font-size:11.5px;display:flex;justify-content:space-between}
.card{background:var(--paper);border:1px solid var(--edge);border-radius:12px;box-shadow:0 4px 16px rgba(38,45,37,.045)}
.b{font-weight:700}.en{font-family:Georgia,serif}
.arrow{color:var(--ochre);font-weight:700}
"""


def page(body: str, extra_css: str = "") -> str:
    return f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<style>{BASE_CSS}{extra_css}</style></head><body>{body}</body></html>"""


# ---------------------------------------------------------------- 图 1 · 总览：三类能力分工
FIG1 = page("""
<div class="overline"><span class="no">图 1 / 总览</span>JEV · THREE CAPABILITY LAYERS</div>
<h1>Agent 系统中的三类能力分工</h1>
<div class="thesis"><b>全文主线：</b>Agent 系统中的每一个智能决策，真的都应该交给生成式 LLM 吗？——不是。<b>确定性逻辑、有限语义判断、开放式生成</b>应当由三类不同组件分别承担。</div>

<div class="tri">
  <div class="col c-code">
    <div class="cap">CODE</div>
    <div class="role">Deterministic Logic</div>
    <div class="cn">确定性控制</div>
    <ul><li>Permission</li><li>Schema</li><li>State Machine</li><li>Hard Policy</li><li>Timeout</li></ul>
  </div>
  <div class="col c-jev">
    <div class="cap">JEV</div>
    <div class="role">Decision Layer</div>
    <div class="cn">有限语义判断</div>
    <ul><li>Intent</li><li>Routing</li><li>Risk</li><li>Score</li><li>Escalation</li></ul>
  </div>
  <div class="col c-llm">
    <div class="cap">LLM</div>
    <div class="role">Generation Layer</div>
    <div class="cn">开放式智能</div>
    <ul><li>Reasoning</li><li>Planning</li><li>Response</li><li>Summary</li><li>Code</li></ul>
  </div>
</div>

<div class="map card">
  <span>确定性问题 <b class="arrow">→</b> <b class="sl">Code</b></span>
  <span>有限语义判断 <b class="arrow">→</b> <b class="jl">Decision Model</b></span>
  <span>开放式生成 / 推理 <b class="arrow">→</b> <b class="gl">Generative LLM</b></span>
</div>

<div class="foot"><span>Jev 学习笔记 · 图 1</span><span>三类能力各司其职，共同组成 Harness</span></div>
""", """
.tri{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.col{background:var(--paper);border:1px solid var(--edge);border-radius:14px;padding:16px 18px 13px;text-align:center;
box-shadow:0 5px 18px rgba(38,45,37,.05);border-top:5px solid var(--slate)}
.c-jev{border-top-color:var(--blush)} .c-llm{border-top-color:var(--qing)}
.cap{font:750 24px Georgia,serif;letter-spacing:.08em;color:var(--slate)}
.c-jev .cap{color:var(--blush)} .c-llm .cap{color:var(--qing)}
.role{font:600 12.5px Georgia,serif;color:var(--muted);letter-spacing:.05em;margin-top:3px}
.cn{font-size:13px;font-weight:700;color:var(--dark);margin:3px 0 8px}
.col ul{list-style:none;padding:0;text-align:left;margin:0 auto;max-width:220px}
.col li{font:600 13px/1.42 ui-monospace,Consolas,monospace;color:#4b534c;padding:3px 2px;border-bottom:1px dashed var(--edge)}
.col li:last-child{border-bottom:0}
.map{margin-top:12px;padding:11px 22px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;
font-size:14.5px;color:#4b534c}
.map b{font-family:Georgia,serif}
.sl{color:var(--slate)} .jl{color:var(--blush)} .gl{color:var(--qing)}
""")

# ---------------------------------------------------------------- 图 2 · 机制对比
FIG2 = page("""
<div class="overline"><span class="no">图 2 / 机制</span>GENERATIVE LLM × JEV</div>
<h1>从"生成"到"决策"：两种模型的根本差异</h1>
<div class="thesis"><b>核心区别：</b>unstructured state in, <b>typed probabilistic decisions out</b> —— 一个是被约束成决策接口的生成模型，一个本身就是 Decision Interface。</div>

<div class="vs-row">
  <div class="side s-llm">
    <div class="head">Generative LLM</div>
    <div class="step">Unstructured Input</div><div class="dn">↓</div>
    <div class="step hi">Token-by-token<br>Autoregressive Generation</div><div class="dn">↓</div>
    <div class="step">String / JSON / Tool Call</div><div class="dn">↓</div>
    <div class="step">Parsing</div><div class="dn">↓</div>
    <div class="step end">Software Action</div>
    <div class="tag">Generate Tokens</div>
  </div>
  <div class="badge">VS</div>
  <div class="side s-jev">
    <div class="head">Jev</div>
    <div class="step">Unstructured State</div><div class="dn">↓</div>
    <div class="step hi">Decision Model</div><div class="dn">↓</div>
    <div class="step hi2">Typed Probabilistic Decision<br><small>Typed Answer + Probability + Confidence</small></div><div class="dn">↓</div>
    <div class="step">Choice / Score / Noul</div><div class="dn">↓</div>
    <div class="step end">Software Action</div>
    <div class="tag">Make Decisions</div>
  </div>
</div>

<div class="warn"><b>避免误解：</b>Jev 不是「输入 → 分类器 → Label」。它的输出是 <b>Typed Answer + Probability + Confidence</b>——这正是 Probability → Threshold → Action 工程闭环的起点。</div>

<div class="foot"><span>Jev 学习笔记 · 图 2</span><span>System One Model · RLCD</span></div>
""", """
.vs-row{display:grid;grid-template-columns:1fr 56px 1fr;gap:10px;align-items:stretch}
.side{background:var(--paper);border:1px solid var(--edge);border-radius:14px;padding:14px 16px 11px;text-align:center;
box-shadow:0 5px 18px rgba(38,45,37,.05)}
.s-llm{border-top:5px solid var(--qing)} .s-jev{border-top:5px solid var(--blush)}
.head{font:750 18px Georgia,serif;color:var(--qing);margin-bottom:9px}
.s-jev .head{color:var(--blush)}
.step{background:#f0ede4;border:1px solid var(--edge);border-radius:9px;padding:6.5px 10px;font:600 13px/1.45 ui-monospace,Consolas,monospace;color:#4b534c}
.step.hi{background:#e3ebe6;border-color:#c3d4c8;color:#31544a}
.step.hi2{background:#f3e4de;border-color:#e0c4bb;color:#7e4438}
.step.hi2 small{font-size:11px;font-weight:600;color:#9a6a5f;display:block;margin-top:2px}
.step.end{background:var(--dai);border-color:var(--dai);color:#eef4f0}
.dn{color:var(--ochre);font-weight:700;line-height:1.05;font-size:11.5px}
.badge{align-self:center;justify-self:center;width:42px;height:42px;border-radius:50%;background:var(--dai);color:#f2f6f3;
display:flex;align-items:center;justify-content:center;font:750 13px Georgia,serif;box-shadow:0 4px 12px rgba(35,59,60,.25)}
.tag{margin-top:8px;display:inline-block;font:700 11.5px Georgia,serif;letter-spacing:.1em;color:var(--qing);
border:1px solid #c1d4c7;background:var(--celadon);border-radius:20px;padding:3px 13px}
.s-jev .tag{color:#8a4f44;border-color:#dcc0b7;background:#f6e9e4}
.warn{margin-top:12px;background:#faf1e9;border:1px solid #ead8c6;border-radius:10px;padding:10px 15px;font-size:13.5px;color:#6b5140}
.warn b{color:#8f5547}
""")

# ---------------------------------------------------------------- 图 3 · 三 Primitive
FIG3 = page("""
<div class="overline"><span class="no">图 3 / 接口</span>NOUL · CHOICE · SCORE</div>
<h1>Noul、Choice、Score：把"判断"做成软件接口</h1>
<div class="thesis"><b>三类决策原语：</b>Choice 选哪个、Score 程度多高、Noul 是否成立 —— 输出永远带概率，而不是一段自然语言。</div>

<div class="trio">
  <div class="p-card">
    <div class="pname">Choice</div><div class="pcn">多选一</div>
    <div class="demo">
      <div class="q">用户 Intent 是？</div>
      <div class="opt"><span>退款</span><i style="width:71%"></i><b>0.71</b></div>
      <div class="opt"><span>技术故障</span><i style="width:17%"></i><b>0.17</b></div>
      <div class="opt"><span>账单问题</span><i style="width:8%"></i><b>0.08</b></div>
      <div class="opt"><span>投诉</span><i style="width:4%"></i><b>0.04</b></div>
    </div>
    <div class="use">适用：Intent / Agent / Model / Tool Routing</div>
  </div>
  <div class="p-card">
    <div class="pname">Score</div><div class="pcn">有序评分</div>
    <div class="demo">
      <div class="q">用户情绪强度</div>
      <div class="scale"><span>1</span><span>2</span><span class="mark">3</span><span>4</span><span>5</span></div>
      <div class="caret">▲</div>
      <div class="exp">Expected Score = <b>3.4</b></div>
      <div class="range"><small>平静</small><small>愤怒</small></div>
    </div>
    <div class="use">适用：Risk / Priority / Quality / Urgency</div>
  </div>
  <div class="p-card">
    <div class="pname">Noul</div><div class="pcn">命题概率</div>
    <div class="demo">
      <div class="q">"这个 Tool Call 是否危险？"</div>
      <div class="pbar"><i class="t" style="width:82%"></i><i class="f" style="width:18%"></i></div>
      <div class="plegend"><span>P(True) = <b>0.82</b></span><span>P(False) = 0.18</span></div>
      <div class="pchain">Probability → Threshold → Action</div>
    </div>
    <div class="use">适用：Allow / Block · Escalation · Pass / Fail</div>
  </div>
</div>

<div class="sum card"><b>Choice</b> = 选哪个　·　<b>Score</b> = 程度多高　·　<b>Noul</b> = 是否成立</div>

<div class="foot"><span>Jev 学习笔记 · 图 3</span><span>Probability → Threshold → Action</span></div>
""", """
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:13px}
.p-card{background:var(--paper);border:1px solid var(--edge);border-top:5px solid var(--blush);border-radius:14px;
padding:15px 16px 12px;box-shadow:0 5px 18px rgba(38,45,37,.05)}
.pname{font:750 21px Georgia,serif;color:var(--blush)}
.pcn{font-size:12.5px;font-weight:700;color:var(--muted);margin-bottom:8px}
.demo{background:#f4f1e8;border:1px solid var(--edge);border-radius:10px;padding:11px 12px;min-height:150px}
.q{font-size:13px;font-weight:600;color:var(--dark);margin-bottom:7px}
.opt{display:grid;grid-template-columns:58px 1fr 36px;gap:8px;align-items:center;margin:5.5px 0;font-size:12.5px;color:#4b534c}
.opt i{display:block;height:9px;border-radius:6px;background:linear-gradient(90deg,#b98a7d,#a6675e)}
.opt b{text-align:right;font-family:Georgia,serif;color:#7e4438}
.scale{display:flex;justify-content:space-between;font:700 15px Georgia,serif;color:#5a615a;margin:4px 4px 0}
.scale .mark{color:var(--blush)}
.caret{text-align:center;color:var(--blush);font-size:14px;line-height:1.1}
.exp{text-align:center;font-size:13px;margin-top:4px}
.exp b{font-family:Georgia,serif;color:#7e4438;font-size:15px}
.range{display:flex;justify-content:space-between;margin-top:4px}
.range small{color:var(--muted);font-size:11px}
.pbar{display:flex;height:13px;border-radius:8px;overflow:hidden;margin:4px 0 7px}
.pbar .t{background:linear-gradient(90deg,#b98a7d,#a6675e)}
.pbar .f{background:#d8d3c6}
.plegend{display:flex;justify-content:space-between;font-size:12px;color:#4b534c}
.plegend b{font-family:Georgia,serif;color:#7e4438}
.pchain{margin-top:8px;text-align:center;font:600 11px/1.5 ui-monospace,Consolas,monospace;color:var(--muted)}
.use{margin-top:9px;font:600 12px/1.55 ui-monospace,Consolas,monospace;color:var(--qing)}
.sum{margin-top:11px;padding:9px 18px;text-align:center;font-size:14.5px;color:#3a4a42}
.sum b{font-family:Georgia,serif;color:var(--blush)}
""")

# ---------------------------------------------------------------- 图 4 · Harness 中的 Decision Layer
FIG4 = page("""
<div class="overline"><span class="no">图 4 / 架构</span>JEV AS DECISION LAYER IN HARNESS</div>
<h1>Jev 在 Agent Harness 中的位置</h1>
<div class="thesis"><b>架构原则：</b>模型做语义判断，<b>最终控制逻辑依然留在 Harness</b> —— Jev 之后是 Policy / Code，再是 Action，而不是 Jev 直接执行。</div>

<div class="flow-top card">
  <span>User Request</span><b class="arrow">→</b><span>Generative LLM</span><b class="arrow">→</b><span>Proposed Decision</span>
</div>
<div class="branch-arrows">↓　　　　　　　　　　　　　　↓</div>

<div class="branches">
  <div class="br">
    <div class="btag">Model Routing</div>
    <div class="node">Proposed Model Choice</div><div class="dn">↓</div>
    <div class="node jev">Jev · Choice</div><div class="dn">↓</div>
    <div class="node split">Fast <span class="arrow">/</span> Powerful</div><div class="dn">↓</div>
    <div class="node end">Model</div><div class="dn">↓</div>
    <div class="node split">Confidence → Agent State<br><small>后续 fallback / 二次确认</small></div>
  </div>
  <div class="br">
    <div class="btag">Tool Risk Gating</div>
    <div class="node">Proposed Tool Call</div><div class="dn">↓</div>
    <div class="node jev">Jev · Noul</div><div class="dn">↓</div>
    <div class="node split">Safe <span class="arrow">/</span> Risky <span class="arrow">/</span> Uncertain</div><div class="dn">↓</div>
    <div class="node policy">Policy Layer</div>
    <div class="three"><span class="allow">Allow</span><span class="review">Review</span><span class="block">Block</span></div>
  </div>
</div>

<div class="ioput card">
  <b>Jev 输出</b>：decision · probability · confidence ——
  probability / confidence 存入 Agent State，可供后续 fallback、二次确认或人工升级使用
</div>

<div class="foot"><span>Jev 学习笔记 · 图 4</span><span>Jev → Policy / Code → Action</span></div>
""", """
.flow-top{padding:10px 22px;display:flex;justify-content:center;gap:14px;align-items:center;font:600 14px/1.4 ui-monospace,Consolas,monospace;color:#3d4a44}
.branch-arrows{text-align:center;color:var(--ochre);font-weight:700;font-size:14px;line-height:1.3;letter-spacing:.5em}
.branches{display:grid;grid-template-columns:1fr 1.25fr;gap:13px;margin-top:0}
.br{background:#f8f5ec;border:1px solid var(--edge);border-radius:14px;padding:12px 16px 10px}
.btag{display:inline-block;font:700 12px Georgia,serif;color:var(--qing);border:1px solid #c1d4c7;background:var(--celadon);
border-radius:20px;padding:2.5px 11px;margin-bottom:9px}
.node{background:var(--paper);border:1px solid var(--edge);border-radius:9px;text-align:center;padding:6.5px 9px;
font:600 13px/1.4 ui-monospace,Consolas,monospace;color:#4b534c;box-shadow:0 2px 8px rgba(38,45,37,.04)}
.node.jev{background:#f3e4de;border-color:#e0c4bb;color:#7e4438;font-weight:700}
.node.split{font-size:12px}
.node.split small{font-size:10.5px;color:#6a716a;display:block}
.node.policy{background:var(--dai);border-color:var(--dai);color:#eef4f0}
.node.end{background:#e3ebe6;border-color:#c3d4c8;color:#31544a}
.dn{text-align:center;color:var(--ochre);font-weight:700;line-height:1.05;font-size:11px}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:6px}
.three span{text-align:center;border-radius:8px;padding:5.5px 4px;font:700 12.5px Georgia,serif}
.allow{background:#e3ebe6;color:#31544a;border:1px solid #c3d4c8}
.review{background:#f1eadf;color:#8a6a3d;border:1px solid #e0d3b8}
.block{background:#f3e4de;color:#7e4438;border:1px solid #e0c4bb}
.ioput{margin-top:11px;padding:10px 16px;font-size:13.5px;color:#3a4a42}
.ioput b{color:var(--blush)}
""")

# ---------------------------------------------------------------- 图 5 · Runtime + Eval 双角色
FIG5 = page("""
<div class="overline"><span class="no">图 5 / 闭环</span>JEV AT RUNTIME × AS A JUDGE</div>
<h1>同一个 Decision Model：运行时做决策，运行后做评测</h1>
<div class="thesis"><b>统一视角：</b>Runtime 问"下一步应该怎么办？"，Evaluation 问"刚才做得怎么样？" —— 两件事用的是同一种概率化判断能力。</div>

<div class="phase p1"><span class="pl">BEFORE / DURING RUN</span></div>
<div class="rt card">
  <span>Agent State</span><b class="arrow">→</b><span class="hl">Jev Runtime Decision</span><b class="arrow">→</b>
  <span><small>Route → Model / Tool</small><br><small>Gate → Allow / Block</small></span><b class="arrow">→</b><span>Agent Execution</span>
</div>
<div class="mid-arrow">↓　Trace + Outcome　↓</div>

<div class="phase p2"><span class="pl">AFTER RUN</span></div>
<div class="ev card">
  <span class="hl">Jev-as-a-Judge</span>
  <div class="outs">
    <div class="o">Pass / Fail</div><div class="o">Quality Score</div><div class="o">Failure Type</div>
  </div>
  <b class="arrow">→</b><span>Eval / Regression</span>
</div>

<div class="sum card"><b>Runtime：</b>下一步怎么做？　｜　<b>Evaluation：</b>刚才做得怎么样？</div>

<div class="foot"><span>Jev 学习笔记 · 图 5</span><span>第三种 Evaluator：Code-based · LLM-as-a-Judge · Jev-as-a-Judge</span></div>
""", """
.phase{margin:0 0 8px}
.pl{display:inline-block;font:700 11px Georgia,serif;letter-spacing:.14em;color:var(--muted);
border:1px solid var(--edge);background:#f4f1e8;border-radius:4px;padding:2.5px 10px}
.p2{margin-top:10px}
.rt,.ev{padding:13px 20px;display:flex;align-items:center;justify-content:center;gap:11px;flex-wrap:wrap;
font:600 14px/1.5 ui-monospace,Consolas,monospace;color:#3d4a44}
.rt span,.ev span{background:#f0ede4;border:1px solid var(--edge);border-radius:9px;padding:7.5px 12px;font-size:13px}
.rt .hl,.ev .hl{background:#f3e4de;border-color:#e0c4bb;color:#7e4438;font-weight:700;font-size:13.5px}
.rt small{font-size:11px;color:#6a716a;display:block;line-height:1.45}
.mid-arrow{text-align:center;color:var(--ochre);font-weight:700;font-size:13.5px;margin:6px 0 8px;line-height:1.3}
.outs{display:flex;gap:8px}
.o{background:#e3ebe6!important;border:1px solid #c3d4c8!important;color:#31544a!important;border-radius:9px!important;
padding:7.5px 12px!important;font-size:13px!important}
.sum{margin-top:11px;padding:9px 16px;text-align:center;font-size:14.5px;color:#3a4a42}
.sum b{color:var(--blush)}
""")

# ---------------------------------------------------------------- 图 6 · LangChain 实验
FIG6 = page("""
<div class="overline"><span class="no">图 6 / 实验</span>LANGCHAIN · JEV-AS-A-JUDGE</div>
<h1>Jev-as-a-Judge 实验：怎么读数字才不被误导</h1>
<div class="thesis"><b>读数原则：</b>评 Judge 要同时看 <b>alignment</b> 和 <b>variance</b> —— Low Variance ≠ High Accuracy；而且这只是 5 个任务、1 个 Agent 的窄实验。</div>

<div class="two">
  <div class="card half">
    <div class="h3">实验设计</div>
    <div class="dstep">5 个固定 Weather Tasks</div><div class="dn">↓</div>
    <div class="dstep">固定的 Agent Runs + Human Oracle</div><div class="dn">↓</div>
    <div class="judges">
      <span class="j jj">Jev</span><span class="j">GPT-5.6<br>Luna</span><span class="j">GPT-5.6<br>Terra</span><span class="j">Claude<br>Sonnet 4.6</span>
    </div>
    <div class="dn">↓</div>
    <div class="dstep">每例重复评价 100 次</div><div class="dn">↓</div>
    <div class="mets"><span>Accuracy</span><span>Agreement</span><span>Variance</span><span>Latency</span><span>Cost</span></div>
  </div>
  <div class="card half">
    <div class="h3">Jev 关键结果</div>
    <div class="nums">
      <div class="nc"><b>500 / 500</b><small>does_pass 与人工 oracle 一致</small></div>
      <div class="nc"><b>0.0000149</b><small>quality score 方差</small></div>
      <div class="nc"><b>≈ 0.44 s</b><small>平均延迟 / 次</small></div>
      <div class="nc"><b>≈ $0.00035</b><small>成本 / 次</small></div>
    </div>
    <div class="caution"><b>Low Variance ≠ High Accuracy</b><br>一个 Judge 可以每次都判断一样，但每次都判断错。<br>
    <small>实验边界：5 tasks · 1 agent · narrow dataset —— promising but early</small></div>
  </div>
</div>

<div class="foot"><span>Jev 学习笔记 · 图 6</span><span>Judge 本身也必须被 Evaluate</span></div>
""", """
.two{display:grid;grid-template-columns:1.05fr 1fr;gap:13px;align-items:stretch}
.half{padding:15px 17px}
.h3{font-size:13px;font-weight:700;color:var(--dai);letter-spacing:.06em;margin-bottom:10px}
.dstep{background:#f0ede4;border:1px solid var(--edge);border-radius:9px;text-align:center;padding:6.5px 9px;
font:600 13px/1.4 ui-monospace,Consolas,monospace;color:#4b534c}
.dn{text-align:center;color:var(--ochre);font-weight:700;font-size:11px;line-height:1.05}
.judges{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.j{background:var(--paper);border:1px solid var(--edge);border-radius:8px;text-align:center;padding:6.5px 4px;
font:700 12px/1.35 Georgia,serif;color:#4b534c}
.j.jj{background:#f3e4de;border-color:#e0c4bb;color:#7e4438}
.mets{display:flex;flex-wrap:wrap;gap:6px;justify-content:center}
.mets span{font:600 11.5px ui-monospace,Consolas,monospace;color:var(--qing);border:1px solid #c1d4c7;
background:var(--celadon);border-radius:20px;padding:2.5px 10px}
.nums{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.nc{background:#f4f1e8;border:1px solid var(--edge);border-radius:10px;text-align:center;padding:10px 8px 9px}
.nc b{display:block;font:750 20px Georgia,serif;color:#7e4438}
.nc small{display:block;font-size:11px;color:var(--muted);margin-top:3px;line-height:1.4}
.caution{margin-top:10px;background:#faf1e9;border:1px solid #ead8c6;border-radius:10px;padding:10px 13px;
font-size:13px;color:#6b5140;line-height:1.65}
.caution b{color:#8f5547;font-size:14px}
.caution small{color:#9a8977}
""")

# ---------------------------------------------------------------- 图 7 · 腾讯云 Trade-off + Threshold
FIG7 = page("""
<div class="overline"><span class="no">图 7 / 工程</span>TENCENT ADP · TRADE-OFF × THRESHOLD</div>
<h1>工程取舍与阈值：Jev 的价值不止于模型指标</h1>
<div class="thesis"><b>工程视角：</b>模型概率的价值，不在于输出 0.83，而在于<b>如何被业务 Policy 消费</b> —— 用可控的质量 trade-off 换成本、延迟与概率化决策。</div>

<div class="tc card">
  <div class="col jevc">
    <div class="chead">Jev</div>
    <div class="m"><span>Intent Accuracy</span><b>88.2%</b></div>
    <div class="m"><span>Emotion MAE</span><b>0.29</b></div>
    <div class="m"><span>Human Escalation</span><b>86.6%</b></div>
    <div class="m good"><span>Latency</span><b>0.38 s</b></div>
    <div class="m good"><span>500 条成本</span><b>$0.0103</b></div>
    <div class="m bad"><span>空响应</span><b>5.6%</b></div>
  </div>
  <div class="axis"><span>Quality</span><span class="bar"><i class="arrow">◄──────►</i></span><span>Efficiency</span></div>
  <div class="col llmc">
    <div class="chead">通用 LLM</div>
    <div class="m good"><span>Intent Accuracy</span><b>93.2%</b></div>
    <div class="m good"><span>Emotion MAE</span><b>0.16</b></div>
    <div class="m good"><span>Human Escalation</span><b>89.8%</b></div>
    <div class="m"><span>Latency</span><b>0.57 s</b></div>
    <div class="m"><span>500 条成本</span><b>≈ $2.45</b></div>
    <div class="m"><span>空响应</span><b>0%</b></div>
  </div>
</div>

<div class="sep"><span>THRESHOLD TRIAGE · 是否转人工</span></div>

<div class="scale card">
  <div class="track">
    <div class="seg auto"><b>AUTO PROCESS</b><small>&lt; 0.3</small><i>30.2%</i></div>
    <div class="seg review"><b>HUMAN REVIEW</b><small>0.3 ~ 0.7</small><i>31.4%</i></div>
    <div class="seg esc"><b>ESCALATE</b><small>≥ 0.7</small><i>38.4%</i></div>
  </div>
  <div class="ticks"><span>0</span><span>0.3</span><span>0.7</span><span>1.0</span></div>
  <div class="chain"><b>Probability</b><span class="arrow">→</span><b>Threshold</b><span class="arrow">→</span><b>Business Policy</b><span class="arrow">→</span><b>Action</b></div>
</div>

<div class="foot"><span>Jev 学习笔记 · 图 7</span><span>不是"谁赢谁输"，而是 Trade-off</span></div>
""", """
.tc{display:grid;grid-template-columns:1fr 150px 1fr;gap:8px;padding:13px 18px;align-items:center}
.chead{font:750 18px Georgia,serif;text-align:center;margin-bottom:7px}
.jevc .chead{color:var(--blush)} .llmc .chead{color:var(--qing)}
.m{display:flex;justify-content:space-between;align-items:baseline;padding:5px 11px;border-bottom:1px dashed var(--edge);font-size:13px}
.m:last-child{border-bottom:0}
.m span{color:#5a615a}
.m b{font:700 15px Georgia,serif;color:#4b534c}
.m.good b{color:#31544a} .m.bad b{color:#8f5547}
.axis{display:flex;flex-direction:column;align-items:center;gap:5px;font:700 11.5px Georgia,serif;color:var(--muted);letter-spacing:.08em}
.axis .bar{color:var(--ochre);font-size:13px;letter-spacing:.05em}
.sep{margin:13px 0 8px;text-align:center}
.sep span{font:700 11px Georgia,serif;letter-spacing:.16em;color:var(--muted);border:1px dashed #cbc9bc;border-radius:4px;padding:3px 12px;background:#f4f1e8}
.scale{padding:15px 20px 12px}
.track{display:grid;grid-template-columns:30.2fr 31.4fr 38.4fr;gap:6px}
.seg{text-align:center;border-radius:10px;padding:9px 6px 7px}
.seg b{display:block;font:700 12px Georgia,serif;letter-spacing:.05em}
.seg small{display:block;font:600 11px monospace;margin-top:1px;opacity:.75}
.seg i{display:block;font:750 16px Georgia,serif;font-style:normal;margin-top:4px}
.auto{background:#e3ebe6;border:1px solid #c3d4c8;color:#31544a}
.review{background:#f1eadf;border:1px solid #e0d3b8;color:#8a6a3d}
.esc{background:#f3e4de;border:1px solid #e0c4bb;color:#7e4438}
.ticks{display:flex;justify-content:space-between;font:600 12px Georgia,serif;color:var(--muted);
margin:5px 2px 0;padding:0 calc(38.4fr/2) 0 0}
.chain{margin-top:10px;text-align:center;font-size:13.5px;color:#3a4a42}
.chain b{font-family:Georgia,serif;color:var(--dark)}
.chain .arrow{margin:0 7px;font-weight:700}
""")


def render(figures: dict):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": WIDTH, "height": 400}, device_scale_factor=2)
        pg = ctx.new_page()
        for name, html in figures.items():
            pg.set_content(html, wait_until="networkidle")
            pg.wait_for_timeout(250)
            # 把 viewport 调到与内容等高，full_page 截图就不会垫空白
            h = pg.evaluate("document.documentElement.scrollHeight")
            pg.set_viewport_size({"width": WIDTH, "height": h})
            pg.wait_for_timeout(80)
            out = OUT_DIR / f"{name}.png"
            pg.screenshot(path=str(out), full_page=True)
            print(f"  generated {out.name}  (content height {h}px)")
        browser.close()


if __name__ == "__main__":
    figures = {
        "fig1_three_layers": FIG1,
        "fig2_llm_vs_jev": FIG2,
        "fig3_primitives": FIG3,
        "fig4_decision_layer": FIG4,
        "fig5_runtime_eval_loop": FIG5,
        "fig6_langchain_experiment": FIG6,
        "fig7_tradeoff_threshold": FIG7,
    }
    render(figures)
    print("all figures done")
