#!/usr/bin/env python3
"""为《agentic_uav_1002.md》笔记生成 7 张结构化配图（HTML -> Playwright 截图 PNG）。

用法: python build_figures.py
输出: 同目录下 fig1..fig7 七张 PNG（2x 高清，高度自适应内容）。
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
.mono{font-family:ui-monospace,Consolas,monospace}
"""


def page(body: str, extra_css: str = "") -> str:
    return f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<style>{BASE_CSS}{extra_css}</style></head><body>{body}</body></html>"""


# ---------------------------------------------------------------- 图 1 · 单向链 vs 持续闭环
FIG1 = page("""
<div class="overline"><span class="no">图 1 / 定义</span>AGENTIC UAV ≠ LLM + DRONE</div>
<h1>从单向管线到持续闭环</h1>
<div class="thesis"><b>核心区别：</b>传统系统里 LLM 只是一个生成 Mission Plan 的 Planner；Agentic UAV 是一个 <b>感知-决策-执行-反馈-反思</b> 持续闭环的 Agent，且 Action 会真实改变物理世界。</div>

<div class="pair">
  <div class="side s-old">
    <div class="shead">传统 LLM-UAV</div>
    <div class="chain">
      <div class="nd">Natural Language</div><span class="a">→</span>
      <div class="nd">LLM</div><span class="a">→</span>
      <div class="nd">Mission Plan</div><span class="a">→</span>
      <div class="nd stop">UAV Execution <b class="stopmark">⊣</b></div>
    </div>
    <div class="snote">单向、断头：LLM 本质上仍然只是一个 Planner</div>
  </div>

  <div class="side s-new">
    <div class="shead">Agentic UAV</div>
    <div class="loop">
      <div class="row">
        <div class="nd">Perception</div><span class="a">→</span>
        <div class="nd">World Model / State</div><span class="a">→</span>
        <div class="nd">Reasoning</div><span class="a">→</span>
        <div class="nd">Planning / Tool Use</div>
      </div>
      <div class="loopback">↩ &nbsp;Reflection / Replanning&nbsp; ←&nbsp; Observation / Feedback&nbsp; ←&nbsp; Environment&nbsp; ←&nbsp; Action&nbsp; ↺</div>
    </div>
    <div class="snote good">闭环运行：观察环境、反思执行、动态重规划</div>
  </div>
</div>

<div class="outer card">外围支撑：<b>Memory</b> · <b>Knowledge</b> · <b>Tools</b> · <b>Communication</b> · <b>Security</b> · <b>Evaluation</b> · <b>Multi-Agent Coordination</b></div>

<div class="foot"><span>Agentic UAV 学习笔记 · 图 1</span><span>Latency · Safety · Fallback · Verification 成为核心系统问题</span></div>
""", """
.pair{display:grid;grid-template-columns:1fr 1.35fr;gap:13px}
.side{background:var(--paper);border:1px solid var(--edge);border-radius:14px;padding:15px 17px 12px;
box-shadow:0 5px 18px rgba(38,45,37,.05)}
.s-old{border-top:5px solid var(--slate)} .s-new{border-top:5px solid var(--qing)}
.shead{font:750 16px Georgia,serif;margin-bottom:11px}
.s-old .shead{color:var(--slate)} .s-new .shead{color:var(--qing)}
.chain{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.nd{background:#f0ede4;border:1px solid var(--edge);border-radius:8px;padding:6px 9px;
font:600 12px/1.35 ui-monospace,Consolas,monospace;color:#4b534c;text-align:center}
.s-new .nd{background:#e3ebe6;border-color:#c3d4c8;color:#31544a}
.nd.stop{background:#eee9e4;border-color:#ddd0c2}
.stopmark{color:#8f5547;font-size:14px;margin-left:2px}
.a{color:var(--ochre);font-weight:700;font-size:13px}
.loop .row{display:flex;align-items:center;gap:6px;justify-content:space-between}
.loopback{margin-top:9px;background:#f4f1e8;border:1px dashed #c9c4b4;border-radius:8px;padding:6px 10px;
text-align:center;font:600 11.5px/1.5 ui-monospace,Consolas,monospace;color:#5d6a5f}
.snote{margin-top:10px;font-size:12px;color:var(--muted);text-align:center}
.snote.good{color:#41695e;font-weight:600}
.outer{margin-top:13px;padding:11px 20px;text-align:center;font-size:13.5px;color:#4b534c}
.outer b{font-family:Georgia,serif;color:#31544a}
""")

# ---------------------------------------------------------------- 图 2 · Slow / Fast Thinking
FIG2 = page("""
<div class="overline"><span class="no">图 2 / 分层</span>SLOW THINKING × FAST THINKING</div>
<h1>LLM 负责认知，不替代飞控</h1>
<div class="thesis"><b>分层原则：</b>Agentic UAV 不是用 LLM 替换 Robotics Stack，而是在原有系统上增加一层高层 Cognitive Layer——生成式 LLM 的延迟、随机性和可靠性不适合作为底层控制器。</div>

<div class="layer slow">
  <div class="lh"><span class="lt">Slow Thinking</span><span class="lw">LLM / VLM</span></div>
  <div class="tags"><span>Task Understanding</span><span>Mission Planning</span><span>Semantic Reasoning</span><span>Scene Understanding</span><span>High-level Decision</span></div>
</div>
<div class="fb">⇅　双向状态反馈　⇅</div>
<div class="layer fast">
  <div class="lh"><span class="lt">Fast Thinking</span><span class="lw">传统机器人系统</span></div>
  <div class="tags"><span>State Estimation</span><span>Mapping</span><span>Obstacle Avoidance</span><span>Motion Planning</span><span>Low-level Control</span></div>
</div>

<div class="duty card">
  <span><b class="q1">LLM</b><small>决定"应该做什么"</small></span>
  <span class="arrow">→</span>
  <span><b class="q2">Motion Planner / Controller</b><small>决定"怎样安全地做到"</small></span>
  <span class="arrow">→</span>
  <span><b class="q3">PX4</b><small>实时飞行执行</small></span>
</div>
<div class="notthat">✗ 而不是 <span class="mono">LLM → Motor Control</span></div>

<div class="foot"><span>Agentic UAV 学习笔记 · 图 2</span><span>高频 · 确定 · 低延迟的闭环响应留给专用控制算法</span></div>
""", """
.layer{border-radius:14px;padding:14px 20px 12px;box-shadow:0 5px 18px rgba(38,45,37,.05);border:1px solid var(--edge);background:var(--paper)}
.slow{border-top:5px solid var(--qing)} .fast{border-top:5px solid var(--slate)}
.lh{display:flex;align-items:baseline;gap:12px;margin-bottom:9px}
.lt{font:750 17px Georgia,serif}
.slow .lt{color:var(--qing)} .fast .lt{color:var(--slate)}
.lw{font-size:12.5px;color:var(--muted)}
.tags{display:flex;flex-wrap:wrap;gap:7px}
.tags span{font:600 12px ui-monospace,Consolas,monospace;border-radius:18px;padding:3.5px 11px}
.slow .tags span{color:#31544a;border:1px solid #c1d4c7;background:var(--celadon)}
.fast .tags span{color:#4c5450;border:1px solid #d3d7d2;background:#efeeea}
.fb{text-align:center;color:var(--ochre);font-weight:700;font-size:13px;margin:8px 0;letter-spacing:.08em}
.duty{margin-top:13px;padding:13px 22px;display:flex;justify-content:center;align-items:center;gap:14px;flex-wrap:wrap;text-align:center}
.duty b{font-family:Georgia,serif;font-size:15px}
.duty small{display:block;font-size:11.5px;color:var(--muted);margin-top:2px}
.q1{color:var(--qing)} .q2{color:var(--ochre)} .q3{color:var(--slate)}
.notthat{margin-top:9px;text-align:center;font-size:12.5px;color:#8f5547}
.notthat .mono{background:#f6ece8;border:1px solid #e8cfc7;border-radius:6px;padding:2px 8px}
""")

# ---------------------------------------------------------------- 图 3 · Agent Runtime 链路
FIG3 = page("""
<div class="overline"><span class="no">图 3 / 工程链路</span>NATURAL LANGUAGE → DRONE</div>
<h1>从自然语言到真实飞行：完整的 Agent Runtime</h1>
<div class="thesis"><b>链路设计：</b>系统没有让一个 LLM 包办所有能力——VLM 负责视觉语义理解，LLM 决定下一步动作，PX4 负责真实飞行执行，中间经过 ROS2 与受限动作空间。</div>

<div class="pipe card">
  <span class="pn">Natural Language</span><span class="pa">→</span>
  <span class="pn hl">LLM / VLM</span><span class="pa">→</span>
  <span class="pn">ROS2</span><span class="pa">→</span>
  <span class="pn">Agent Nodes</span><span class="pa">→</span>
  <span class="pn hl2">Restricted Actions</span><span class="pa">→</span>
  <span class="pn">PX4</span><span class="pa">→</span>
  <span class="pn end">Drone</span>
</div>
<div class="nodes">Agent Nodes = <b>Visual Q&amp;A Node</b> · <b>Path Planning Node</b> · <b>Map Encoder Node</b></div>

<div class="constrain card">
  <div class="ch">Action Space Constraining</div>
  <div class="cbody">
    <div class="cbox">
      <div class="cfn mono">Turn(θ)</div>
      <div class="cfn mono">Move(d)</div>
      <div class="crange">参数都有明确范围</div>
    </div>
    <div class="ctext">模型负责<b>选择动作</b>，但可以执行什么动作、参数范围多大，<b>由系统决定</b>。<br>
    <small>≈ Agent Harness 中的 Tool Schema · Permission · Parameter Validation</small></div>
  </div>
</div>

<div class="foot"><span>Agentic UAV 学习笔记 · 图 3</span><span>有限、可验证的 Action Primitive &gt; 自由生成控制命令</span></div>
""", """
.pipe{padding:13px 18px;display:flex;justify-content:center;align-items:center;gap:8px;flex-wrap:wrap}
.pn{background:#f0ede4;border:1px solid var(--edge);border-radius:9px;padding:7px 11px;
font:600 12.5px/1.35 ui-monospace,Consolas,monospace;color:#4b534c}
.pn.hl{background:#e3ebe6;border-color:#c3d4c8;color:#31544a;font-weight:700}
.pn.hl2{background:#f3e4de;border-color:#e0c4bb;color:#7e4438;font-weight:700}
.pn.end{background:var(--dai);border-color:var(--dai);color:#eef4f0}
.pa{color:var(--ochre);font-weight:700;font-size:13px}
.nodes{margin:9px 0 13px;text-align:center;font-size:13px;color:#4b534c}
.nodes b{font-family:Georgia,serif;color:#31544a}
.constrain{padding:14px 18px 12px}
.ch{font:700 13px Georgia,serif;color:#7e4438;margin-bottom:10px;letter-spacing:.04em}
.cbody{display:grid;grid-template-columns:290px 1fr;gap:16px;align-items:center}
.cbox{background:#f4f1e8;border:1px solid var(--edge);border-radius:10px;padding:11px;text-align:center;display:flex;gap:9px;justify-content:center;align-items:center;flex-wrap:wrap}
.cfn{background:var(--paper);border:1px solid #e0c4bb;color:#7e4438;border-radius:8px;padding:5px 12px;font-size:13.5px;font-weight:700}
.crange{flex-basis:100%;font-size:11px;color:var(--muted)}
.ctext{font-size:14px;color:#3a4a42;line-height:1.7}
.ctext small{color:var(--muted);font-size:12px}
""")

# ---------------------------------------------------------------- 图 4 · 五层架构
FIG4 = page("""
<div class="overline"><span class="no">图 4 / 架构</span>FIVE-LAYER AGENTIC UAV STACK</div>
<h1>Agentic UAV 的五层架构</h1>
<div class="thesis"><b>分层拆解：</b>Perception → Reasoning → Action → Integration → Learning（自下而上堆叠）；其中 Integration 层与 Agent Harness 的关系最直接。</div>

<div class="stack">
  <div class="ly l5"><div class="ltag">Learning</div><div class="ldesc"><b>跨任务持续改进</b>：RL · RLHF · RAG · Cross-Mission Memory · Knowledge Update</div></div>
  <div class="ly l4"><div class="ltag">Integration</div><div class="ldesc"><b>Agent Harness 落地层</b>：Tool Registry · Auth · Schema Validation · Retry / Timeout · Circuit Breaker · Telemetry · Security
    <div class="protos"><span><b>MCP</b><i>Agent-Tool</i></span><span><b>ACP</b><i>UAV-Cloud / Operator</i></span><span><b>A2A</b><i>Agent-Agent</i></span></div></div></div>
  <div class="ly l3"><div class="ltag">Action</div><div class="ldesc"><b>Reasoning 决定 What，Action 负责 Execute</b>：Physical（fly_to · land · hover · deploy_rescue_kit）＋ Digital（weather API · database · alert · log）</div></div>
  <div class="ly l2"><div class="ltag">Reasoning</div><div class="ldesc"><b>Cognitive Core</b>：LLM + Planning + ReAct + Tool Use + Reflection → 输出结构化 Plan / Policy</div></div>
  <div class="ly l1"><div class="ltag">Perception</div><div class="ldesc"><b>Context Engineering</b>：RGB · Thermal · LiDAR · IMU → 目标检测 · 语义理解 · Sensor Fusion → 结构化 World Model</div></div>
</div>

<div class="foot"><span>Agentic UAV 学习笔记 · 图 4</span><span>不是让模型看到所有原始信息，而是看到当前决策真正需要的状态</span></div>
""", """
.stack{display:flex;flex-direction:column;gap:9px}
.ly{display:grid;grid-template-columns:150px 1fr;gap:14px;align-items:center;background:var(--paper);
border:1px solid var(--edge);border-radius:11px;padding:11px 16px;box-shadow:0 3px 12px rgba(38,45,37,.04)}
.ltag{font:750 16px Georgia,serif}
.ldesc{font-size:13px;color:#4b534c;line-height:1.65}
.ldesc b{color:var(--dark)}
.l1{border-left:5px solid var(--qing)} .l1 .ltag{color:var(--qing)}
.l2{border-left:5px solid var(--ochre)} .l2 .ltag{color:var(--ochre)}
.l3{border-left:5px solid var(--blush)} .l3 .ltag{color:var(--blush)}
.l4{border-left:5px solid var(--violet)} .l4 .ltag{color:var(--violet)}
.l5{border-left:5px solid var(--dai)} .l5 .ltag{color:var(--dai)}
.protos{display:flex;gap:9px;margin-top:7px;flex-wrap:wrap}
.protos span{border:1px solid #d8cfdd;background:#f3f0f4;border-radius:18px;padding:2.5px 11px;
font:600 11.5px ui-monospace,Consolas,monospace;color:#5d5566;display:inline-flex;gap:6px;align-items:baseline}
.protos b{color:#6b5f78}.protos i{font-style:normal;color:#8d8496;font-size:10.5px}
""")

# ---------------------------------------------------------------- 图 5 · Eval 断崖
FIG5 = page("""
<div class="overline"><span class="no">图 5 / 警示</span>STEP CORRECT ≠ MISSION SUCCESS</div>
<h1>组件全对，任务为什么只成功 40%？</h1>
<div class="thesis"><b>实验结果：</b>指令格式 100% 正确、检测响应 97~100% 有效，最终任务成功率最高却只有 <b>40%</b> —— 不能拿某个 Component 的 Accuracy 替代 Agent 的 End-to-End Success。</div>

<div class="cliff">
  <div class="cl c1"><b>100%</b><small>Valid Flight Command<br>Gemma3 · Qwen2.5 · Llama-3.2</small></div>
  <div class="cl c1"><b>97~100%</b><small>Valid Detection Response<br>多个 VLM</small></div>
  <div class="fall">↘↘↘</div>
  <div class="cl c2"><b>40%</b><small>Mission Success Rate<br>最终 · 最高值</small></div>
</div>
<div class="neq card"><b>Command Syntax Correct</b> ≠ <b>Action Correct</b> ≠ <b>Trajectory Correct</b> ≠ <b>Mission Success</b></div>

<div class="three">
  <div class="t"><div class="th">Component / Step Level</div><p>Perception Accuracy · Tool Call Correctness · Command Validity · Parameter Validity</p></div>
  <div class="t"><div class="th">Trajectory Level</div><p>Repeated Action · Recovery · Path Efficiency · Collision · Replanning</p></div>
  <div class="t"><div class="th">Outcome Level</div><p>Mission Success · Time to Completion · Human Takeover Rate · Safety Violation</p></div>
</div>
<div class="attr card"><b>Failure Attribution</b>：Mission Failed → 失败来自 Perception · Reasoning · Planning · Tool · Action · Control · Communication 中的哪一环？</div>

<div class="foot"><span>Agentic UAV 学习笔记 · 图 5</span><span>Move(1.5) 格式全对，距离判断错就 Overshoot</span></div>
""", """
.cliff{display:flex;align-items:stretch;justify-content:center;gap:12px}
.cl{background:var(--paper);border:1px solid var(--edge);border-radius:12px;text-align:center;padding:14px 22px 11px;
box-shadow:0 4px 14px rgba(38,45,37,.05);min-width:220px}
.cl b{display:block;font:750 34px Georgia,serif}
.cl small{display:block;font-size:11.5px;color:var(--muted);margin-top:5px;line-height:1.5}
.c1{border-top:5px solid var(--qing)} .c1 b{color:#31544a}
.c2{border-top:5px solid var(--blush);background:#fbf4f0} .c2 b{color:#8a4a3e}
.fall{align-self:center;color:var(--blush);font-size:20px;font-weight:700}
.neq{margin-top:13px;padding:10px 16px;text-align:center;font-size:13.5px;color:#3a4a42}
.neq b{font-family:Georgia,serif}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:11px;margin-top:13px}
.t{background:var(--paper);border:1px solid var(--edge);border-radius:10px;padding:11px 13px}
.t:nth-child(1){border-top:4px solid var(--qing)}.t:nth-child(2){border-top:4px solid var(--ochre)}.t:nth-child(3){border-top:4px solid var(--blush)}
.th{font:700 12.5px Georgia,serif;margin-bottom:6px}
.t:nth-child(1) .th{color:var(--qing)}.t:nth-child(2) .th{color:var(--ochre)}.t:nth-child(3) .th{color:var(--blush)}
.t p{font-size:11.5px;color:#5a615a;line-height:1.65}
.attr{margin-top:12px;padding:11px 18px;font-size:13.5px;color:#3a4a42}
.attr b{color:#8a4a3e}
""")

# ---------------------------------------------------------------- 图 6 · Hybrid 延迟对比 + Tier
FIG6 = page("""
<div class="overline"><span class="no">图 6 / 权衡</span>HYBRID SYSTEM, NOT ALL-IN-LLM</div>
<h1>三个数量级的延迟差，决定了 Hybrid 架构</h1>
<div class="thesis"><b>工程结论：</b>Rule-based 极快但只能窄域检测，LLM 有语义能力但延迟明显——按<b>复杂度、风险、实时性、算力预算</b>路由到不同层级，而不是让最大模型处理所有请求。</div>

<div class="lat card">
  <div class="lrow"><span class="ln">Rule-based YOLO</span><div class="bar"><i class="b1"></i></div><b class="lv">29.5 μs</b><small>极快 · 仅窄域检测</small></div>
  <div class="lrow"><span class="ln">Local Gemma-3</span><div class="bar"><i class="b2"></i></div><b class="lv">1.48 s</b><small>语义理解 · 决策</small></div>
  <div class="lrow"><span class="ln">GPT-4 API</span><div class="bar"><i class="b3"></i></div><b class="lv">4.95 s</b><small>高复杂度推理 · 成本最高</small></div>
  <div class="lnote">条长为示意（μs → s 相差约 5 个数量级，无法按真实比例绘制）</div>
</div>

<div class="tiers">
  <div class="tier t1"><div class="tn">Tier 1</div><b>Rule / Traditional Model</b><p>高频 · 简单 · 确定性任务</p></div>
  <div class="tier t2"><div class="tn">Tier 2</div><b>Local LLM</b><p>需要语义理解和决策的任务</p></div>
  <div class="tier t3"><div class="tn">Tier 3</div><b>Cloud LLM</b><p>少量高复杂度推理</p></div>
</div>

<div class="foot"><span>Agentic UAV 学习笔记 · 图 6</span><span>≈ Agent 系统的 Model Routing 思路</span></div>
""", """
.lat{padding:14px 20px 10px}
.lrow{display:grid;grid-template-columns:170px 1fr 92px 200px;gap:12px;align-items:center;padding:6px 0;border-bottom:1px dashed var(--edge)}
.lrow:last-of-type{border-bottom:0}
.ln{font:600 13px ui-monospace,Consolas,monospace;color:#3d4a44}
.bar{height:13px;border-radius:8px;background:#eeeae0;overflow:hidden}
.bar i{display:block;height:100%;border-radius:8px}
.b1{width:4%;background:linear-gradient(90deg,#6e9c8c,#486d63)}
.b2{width:42%;background:linear-gradient(90deg,#c4a284,#a77e4b)}
.b3{width:88%;background:linear-gradient(90deg,#c4918a,#a6675e)}
.lv{font:750 15px Georgia,serif;text-align:right}
.lrow:nth-child(1) .lv{color:#31544a}.lrow:nth-child(2) .lv{color:#8a6a3d}.lrow:nth-child(3) .lv{color:#8a4a3e}
.lrow small{font-size:11.5px;color:var(--muted)}
.lnote{margin-top:7px;padding-top:6px;border-top:1px dashed var(--edge);font-size:10.5px;color:#9a9a90;text-align:right}
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:11px;margin-top:13px}
.tier{background:var(--paper);border:1px solid var(--edge);border-radius:11px;padding:12px 15px 10px;text-align:center}
.t1{border-top:4px solid var(--qing)}.t2{border-top:4px solid var(--ochre)}.t3{border-top:4px solid var(--blush)}
.tn{font:700 11px Georgia,serif;letter-spacing:.14em;margin-bottom:4px}
.t1 .tn{color:var(--qing)}.t2 .tn{color:var(--ochre)}.t3 .tn{color:var(--blush)}
.tier b{font:700 14.5px Georgia,serif;color:var(--dark);display:block}
.tier p{font-size:12px;color:#5a615a;margin-top:3px}
""")

# ---------------------------------------------------------------- 图 7 · 总架构
FIG7 = page("""
<div class="overline"><span class="no">图 7 / 总结</span>FULL AGENTIC UAV ARCHITECTURE</div>
<h1>一套完整的 Agentic UAV 架构</h1>
<div class="thesis"><b>系统本质：</b>把无人机重新设计成 <b>Perception → Reasoning → Action → Feedback → Reflection</b> 持续循环的 Agent System——数字与物理双世界操作，感知结果回流认知。</div>

<div class="arch card">
  <div class="main"><span class="an top">Human Goal</span><span class="ad">↓</span>
    <span class="an hi">Agent Harness</span><span class="ad">↓</span>
    <span class="an">Reasoning / Planning <small>Tool Use · Reflection</small></span></div>
  <div class="fork-arrows">↙　　　　　　　　　　↘</div>
  <div class="dual">
    <div class="d"><div class="dh dg">Digital Action</div><p class="mono">API · DB · RAG<br>Communication</p></div>
    <div class="d"><div class="dh dp">Physical Action</div><p class="mono">Motion Planner ↓<br>PX4</p></div>
  </div>
  <div class="fork-arrows">↘　　　　　　　　　　↙</div>
  <div class="main"><span class="an">Environment</span><span class="ad">↓</span>
    <span class="an sense">RGB · LiDAR · IMU · Thermal<small>Perception → World Model</small></span></div>
  <div class="loopback">World Model → Reasoning　↺ 持续闭环</div>
</div>

<div class="outer card">外围：<b>Memory</b> · <b>Observability</b> · <b>Evaluation</b> · <b>Security</b> · <b>Human-in-the-loop</b> · <b>Multi-Agent Coordination</b></div>

<div class="foot"><span>Agentic UAV 学习笔记 · 图 7</span><span>Generative AI × 确定性 Robotics 的组合</span></div>
""", """
.arch{padding:16px 22px 13px;text-align:center}
.main{display:flex;flex-direction:column;align-items:center;gap:2px}
.an{background:#f0ede4;border:1px solid var(--edge);border-radius:9px;padding:7px 18px;
font:600 13.5px/1.4 ui-monospace,Consolas,monospace;color:#3d4a44;min-width:300px;text-align:center}
.an small{display:block;font-size:10.5px;color:#6a716a;font-weight:400}
.an.hi{background:var(--dai);border-color:var(--dai);color:#eef4f0;font-weight:700}
.an.top{background:#e3ebe6;border-color:#c3d4c8;color:#31544a}
.an.sense{background:#e3ebe6;border-color:#c3d4c8;color:#31544a}
.ad{color:var(--ochre);font-weight:700;font-size:12px;line-height:1.15}
.fork-arrows{color:var(--ochre);font-weight:700;font-size:12.5px;line-height:1.3;letter-spacing:.2em;margin:2px 0}
.dual{display:grid;grid-template-columns:1fr 1fr;gap:13px;max-width:640px;margin:0 auto}
.d{background:#f8f5ec;border:1px solid var(--edge);border-radius:10px;padding:9px 12px}
.dh{font:700 13px Georgia,serif;margin-bottom:5px}
.dg{color:#31544a}.dp{color:#7e4438}
.d p{font-size:12px;color:#5a615a;line-height:1.6;margin:0}
.loopback{margin-top:10px;display:inline-block;background:#f4f1e8;border:1px dashed #c9c4b4;border-radius:20px;
padding:5px 16px;font:600 12px ui-monospace,Consolas,monospace;color:#41695e}
.outer{margin-top:12px;padding:10px 18px;text-align:center;font-size:13px;color:#4b534c}
.outer b{font-family:Georgia,serif;color:#31544a}
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
        "fig1_oneway_vs_loop": FIG1,
        "fig2_slow_fast_thinking": FIG2,
        "fig3_agent_runtime": FIG3,
        "fig4_five_layers": FIG4,
        "fig5_eval_cliff": FIG5,
        "fig6_hybrid_tiers": FIG6,
        "fig7_full_architecture": FIG7,
    }
    render(figures)
    print("all figures done")
