#!/usr/bin/env python3
"""为《agent eval_918》笔记生成 5 张结构化配图（HTML -> Playwright 截图 PNG）。

用法: python build_figures.py
输出: 同目录下 fig1..fig5 五张 PNG（2x 高清）。
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# Windows 控制台默认 GBK，print 中文/符号可能报错，强制 UTF-8
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

OUT_DIR = Path(__file__).resolve().parent
WIDTH = 1240  # 逻辑像素，截图 2x 后 2480px

# 9.18 批次 HTML 笔记同款配色
BASE_CSS = """
:root{--bg:#f5f2eb;--paper:#fdfbf6;--ink:#292c2a;--dark:#233b3c;--text:#383c38;
--muted:#71766f;--edge:#dddcd0;--dai:#334f50;--qing:#567d72;--celadon:#e8f0e9;
--ochre:#a77e4b;--blush:#a6675e;--violet:#796e82}
*{box-sizing:border-box;margin:0}
body{background:var(--bg);font:15px/1.75 "Noto Sans CJK SC","Source Han Sans SC","Microsoft YaHei",system-ui,sans-serif;color:var(--text);
padding:46px 44px 40px;width:1240px}
.overline{letter-spacing:.22em;font:600 11px/1.2 Georgia,serif;color:var(--qing);text-transform:uppercase}
.overline .no{color:var(--blush);margin-right:10px}
h1{font-size:31px;font-weight:750;letter-spacing:-.03em;line-height:1.3;color:var(--dark);margin:14px 0 12px;max-width:1050px}
.thesis{margin:18px 0 26px;border-left:4px solid var(--blush);background:#eeeae2;padding:15px 20px;
font-size:15.5px;color:#3a4540;border-radius:0 8px 8px 0}
.thesis b{color:#874b44}
.foot{margin-top:26px;padding-top:14px;border-top:1px dashed #cbc9bc;color:#8a8d83;font-size:11.5px;display:flex;justify-content:space-between}
.card{background:var(--paper);border:1px solid var(--edge);border-radius:12px;box-shadow:0 4px 16px rgba(38,45,37,.045)}
"""


def page(body: str, extra_css: str = "") -> str:
    return f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<style>{BASE_CSS}{extra_css}</style></head><body>{body}</body></html>"""


# ---------------------------------------------------------------- 图 1 · 定义图
FIG1 = page("""
<div class="overline"><span class="no">图 1 / 定义</span>AGENT EVALUATION · WHAT TO EVALUATE</div>
<h1>Agent Evaluation 到底在评什么？</h1>
<div class="thesis"><b>核心原则：</b>不能只验证模型<b>声称</b>完成了什么，还要验证系统<b>实际执行</b>了什么，以及环境<b>最终发生了什么变化</b>。</div>

<div class="flow">
  <div class="fnode">Planning<br><small>规划</small></div><div class="arr">→</div>
  <div class="fnode">Tool Calling<br><small>工具调用</small></div><div class="arr">→</div>
  <div class="fnode">Environment Interaction<br><small>环境交互</small></div><div class="arr">→</div>
  <div class="fnode">State Update<br><small>状态更新</small></div><div class="arr">→</div>
  <div class="fnode fout">Final Answer<br><small>最终输出</small></div>
</div>
<div class="flowcap">一个典型 Agent 的执行流 —— 三个评测对象分别锚定在<b>过程</b>、<b>结果</b>、<b>环境落点</b>上</div>

<div class="cols">
  <div class="card ev ev-t">
    <div class="anchor">锚定 · Planning → Tool Calling 执行段</div>
    <div class="en">TRAJECTORY EVALUATION</div>
    <div class="cn">过程评测</div>
    <p class="q">执行轨迹中每一步是否合理？</p>
    <p class="w"><b>盲区：</b>最终回答正确 ≠ 没有重复检索、无效循环、错误的工具调用</p>
  </div>
  <div class="card ev ev-o">
    <div class="anchor">锚定 · Final Answer 最终输出</div>
    <div class="en">OUTCOME EVALUATION</div>
    <div class="cn">结果评测</div>
    <p class="q">任务目标最终是否达成？</p>
    <p class="w"><b>盲区：</b>Agent 回复"文件已修改完成" ≠ 文件真的发生了变化</p>
  </div>
  <div class="card ev ev-s">
    <div class="anchor">锚定 · State Update 环境状态</div>
    <div class="en">STATE EVALUATION</div>
    <div class="cn">状态评测</div>
    <p class="q">外部环境是否被正确改变？</p>
    <p class="w"><b>盲区：</b>目标文件修改正确 ≠ 没有越权访问其他文件 / 数据库</p>
  </div>
</div>
<div class="note">三者互不可替代：只看其中任何一个，都会漏掉另外两类失败。</div>

<div class="foot"><span>Agent Evaluation 阅读笔记 · 图 1</span><span>Trajectory / Outcome / State</span></div>
""", """
.flow{display:flex;align-items:stretch;gap:6px;margin-top:6px}
.fnode{flex:1;background:var(--dai);color:#f2f6f3;border-radius:10px;padding:16px 10px;text-align:center;
font-weight:700;font-size:15.5px;line-height:1.35}
.fnode small{display:block;font-weight:400;font-size:12px;color:#c9d8d2;margin-top:3px}
.fnode.fout{background:var(--ochre)}
.arr{align-self:center;color:var(--ochre);font-size:20px;font-weight:700}
.flowcap{text-align:center;color:var(--muted);font-size:13px;margin:12px 0 24px}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.ev{padding:20px 20px 18px;border-top:4px solid var(--qing);position:relative}
.ev-t{border-top-color:var(--qing)} .ev-o{border-top-color:var(--ochre)} .ev-s{border-top-color:var(--blush)}
.anchor{font-size:11px;letter-spacing:.04em;color:var(--muted);border:1px solid var(--edge);border-radius:20px;
display:inline-block;padding:2px 10px;margin-bottom:12px;background:#f4f1e8}
.en{font:700 14px/1.3 Georgia,serif;letter-spacing:.02em}
.ev-t .en{color:var(--qing)} .ev-o .en{color:var(--ochre)} .ev-s .en{color:var(--blush)}
.cn{font-size:12.5px;color:var(--muted);margin:2px 0 10px}
.q{font-size:15px;font-weight:600;color:var(--dark);margin-bottom:8px}
.w{font-size:13px;color:#5a615a;background:#f2efe6;border-radius:8px;padding:9px 11px}
.note{margin-top:18px;text-align:center;font-size:13.5px;color:#6a5f4e;background:#f1eadf;border:1px dashed #d8c9a8;
border-radius:9px;padding:10px 16px}
""")

# ---------------------------------------------------------------- 图 2 · 方法图
FIG2 = page("""
<div class="overline"><span class="no">图 2 / 方法</span>BENCHBUILDER PIPELINE · ARENA-HARD</div>
<h1>一条可信的 Benchmark 是怎么造出来的？</h1>
<div class="thesis"><b>核心结论：</b>可靠的 Benchmark 不仅要有正确的<b>评分方法</b>，还应有合理的<b>任务分布</b>、<b>区分能力</b>与<b>统计稳定性</b>。</div>

<div class="pipe">
  <div class="step"><div class="n">01</div><b>Crowdsourced<br>Prompts</b><small>收集众包真实问题</small></div><div class="parr">→</div>
  <div class="step"><div class="n">02</div><b>Topic<br>Clustering</b><small>按主题聚类</small></div><div class="parr">→</div>
  <div class="step"><div class="n">03</div><b>Quality<br>Scoring</b><small>七项标准打分</small></div><div class="parr">→</div>
  <div class="step"><div class="n">04</div><b>Cluster<br>Filtering</b><small>过滤低质量簇</small></div><div class="parr">→</div>
  <div class="step"><div class="n">05</div><b>Diverse<br>Sampling</b><small>多样性采样</small></div><div class="parr">→</div>
  <div class="step last"><div class="n">★</div><b>Benchmark</b><small>高质量测试集</small></div>
</div>

<div class="sub">
  <div class="card left">
    <div class="h3">问题质量 · 7 项评分标准</div>
    <div class="pills">
      <span class="pill">Specificity <i>具体性</i></span><span class="pill">Domain Knowledge <i>领域知识</i></span>
      <span class="pill">Complexity <i>复杂度</i></span><span class="pill">Problem-Solving <i>问题解决</i></span>
      <span class="pill">Creativity <i>创造性</i></span><span class="pill">Technical Accuracy <i>技术准确性</i></span>
      <span class="pill">Real-world Application <i>真实应用</i></span>
    </div>
  </div>
  <div class="card right">
    <div class="h3">Benchmark 健康度 · 3 个指标</div>
    <div class="mrow"><b>Separability</b><i>区分度</i><span>能否以足够的统计置信度区分不同模型？</span></div>
    <div class="mrow"><b>Agreement</b><i>一致性</i><span>对模型差异的判断，是否与人类偏好参考一致？</span></div>
    <div class="mrow"><b>Brier Score</b><i>概率校准</i><span>两两比较的概率预测是否准确、置信是否合理？</span></div>
  </div>
</div>

<div class="warn"><b>统计口径提醒：</b>85 分 vs 86 分的 1 分差距，可能只是样本方差带来的<b>统计噪声</b> —— 判断差异要看<b>置信区间是否重叠</b>（Bootstrap），而不是只看点值。</div>

<div class="foot"><span>Agent Evaluation 阅读笔记 · 图 2</span><span>Arena-Hard &amp; BenchBuilder Pipeline</span></div>
""", """
.pipe{display:flex;align-items:stretch;gap:5px}
.step{flex:1;background:var(--paper);border:1px solid var(--edge);border-radius:11px;padding:16px 12px 13px;text-align:center;
box-shadow:0 4px 14px rgba(38,45,37,.04)}
.step .n{font:700 11px Georgia,serif;color:var(--qing);letter-spacing:.1em;margin-bottom:7px}
.step b{display:block;font-size:15px;color:var(--dark);line-height:1.3}
.step small{display:block;font-size:12px;color:var(--muted);margin-top:5px}
.step.last{background:var(--dai);border-color:var(--dai)}
.step.last b,.step.last .n{color:#f2f6f3}.step.last small{color:#c9d8d2}
.parr{align-self:center;color:var(--ochre);font-size:19px;font-weight:700}
.sub{display:grid;grid-template-columns:1fr 1.25fr;gap:16px;margin-top:20px}
.left,.right{padding:18px 20px}
.h3{font-size:13px;font-weight:700;color:var(--dai);letter-spacing:.06em;margin-bottom:12px}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.pill{border:1px solid #c1d4c7;background:var(--celadon);color:#3c5f54;border-radius:20px;
padding:5px 12px;font-size:12.5px;font-weight:600}
.pill i{font-style:normal;color:#6d8379;font-weight:400;margin-left:4px}
.mrow{display:flex;align-items:baseline;gap:8px;padding:9px 0;border-bottom:1px dashed var(--edge);flex-wrap:wrap}
.mrow:last-child{border-bottom:0}
.mrow b{font:700 14px Georgia,serif;color:var(--qing);white-space:nowrap}
.mrow i{font-style:normal;font-size:12px;color:var(--ochre);font-weight:700;white-space:nowrap}
.mrow span{font-size:12.5px;color:#5a615a;flex-basis:100%;margin-top:-2px}
.warn{margin-top:20px;background:#faf1e9;border:1px solid #ead8c6;border-radius:10px;padding:13px 18px;
font-size:13.5px;color:#6b5140}
.warn b{color:#8f5547}
""")

# ---------------------------------------------------------------- 图 3 · 机制图
FIG3 = page("""
<div class="overline"><span class="no">图 3 / 机制</span>AGENT-AS-A-JUDGE · DEVAI</div>
<h1>从任务级 0/1，到需求级证据</h1>
<div class="thesis"><b>核心结论：</b>Judge 的核心不是让评判器更<b>复杂</b>，而是让它具备获取与验证<b>有效证据</b>的能力。</div>

<div class="two">
  <div class="card half">
    <div class="h3">Requirements DAG · 需求依赖图</div>
    <div class="dag">
      <div class="dnode"><b>数据加载</b><small>文件存在 · Schema 正确</small></div><div class="darr">↓</div>
      <div class="dnode"><b>数据预处理</b><small>清洗与转换完成</small></div><div class="darr">↓</div>
      <div class="dnode"><b>模型训练</b><small>产物与记录存在</small></div><div class="darr">↓</div>
      <div class="dnode"><b>指标计算</b><small>指标可复现</small></div><div class="darr">↓</div>
      <div class="dnode"><b>报告生成</b><small>内容与需求对应</small></div>
    </div>
    <div class="dmeta">DevAI：55 个真实开发任务 · 365 项层级需求 · 125 项偏好</div>
    <div class="concl"><b>Success 不再只是 0 / 1</b><br>而是能指出：哪些需求已满足 · 失败发生在哪个节点 · 依赖是否闭环</div>
  </div>

  <div class="card half">
    <div class="h3">Judge 组件消融 · OpenHands 实验</div>
    <div class="abl up">
      <div class="abar a1"></div><div class="abar a2"></div><div class="abar a3"></div><div class="abar a4"></div>
      <div class="alabel"><span class="tri">▲</span> Ask · Graph · Read · Locate</div>
      <div class="asub">有效组合 —— 取得较好评测结果</div>
    </div>
    <div class="abl down">
      <div class="abar b1"></div><div class="abar b2"></div><div class="abar b3"></div>
      <div class="alabel"><span class="tri">▼</span> + Retrieve · Planning · Memory</div>
      <div class="asub">加入后评测表现<b>反而下降</b>：信息噪声 · 工作空间规模 · 历史判断错误传播</div>
    </div>
    <div class="ascale"><span>简单</span>趋势示意（非论文精确数值）<span>更复杂</span></div>
    <div class="caution"><b>典型失败：</b>把"合成数据"误判为"真实数据"；把"设置了超参数"误判为"完成了调参"。适合作为自动化评估的一种实现，而非替代确定性检查与人工验收。</div>
  </div>
</div>

<div class="foot"><span>Agent Evaluation 阅读笔记 · 图 3</span><span>Requirements DAG × Component Ablation</span></div>
""", """
.two{display:grid;grid-template-columns:1fr 1.12fr;gap:16px;align-items:stretch}
.half{padding:20px 22px}
.h3{font-size:13px;font-weight:700;color:var(--dai);letter-spacing:.06em;margin-bottom:14px}
.dag{display:flex;flex-direction:column;align-items:center}
.dnode{width:78%;background:#eef2ec;border:1px solid #ccdcd1;border-radius:9px;text-align:center;padding:9px 10px}
.dnode b{font-size:14.5px;color:var(--dark);display:block}
.dnode small{font-size:11.5px;color:var(--muted)}
.darr{color:var(--qing);font-size:15px;line-height:1.35;font-weight:700}
.dmeta{margin:13px 0 0;text-align:center;font-size:11.5px;color:var(--muted);
border-top:1px dashed var(--edge);padding-top:11px}
.concl{margin-top:12px;background:#edf3ed;border:1px solid #ceded3;border-radius:9px;padding:12px 15px;
font-size:13px;color:#3a4a42;line-height:1.65}
.concl b{color:#2f5d50}
.abl{border:1px solid var(--edge);border-radius:10px;padding:14px 16px 12px;margin-bottom:13px;background:#fbfaf5}
.abl.up{border-left:4px solid var(--qing)}
.abl.down{border-left:4px solid var(--blush)}
.abars{display:flex;align-items:flex-end;gap:7px;height:64px;margin-bottom:10px}
.abar{width:34px;border-radius:4px 4px 0 0}
.up .abars .abar{background:linear-gradient(180deg,#6e9c8c,#486d63)}
/* 高度由内联样式控制：up 逐级升高，down 加入额外组件后回落 */
.alabel{font-size:14px;font-weight:700;color:var(--dark)}
.alabel .tri{font-size:12px;margin-right:4px}
.up .tri{color:#3f7a68} .down .tri{color:#a05548}
.asub{font-size:12.5px;color:var(--muted);margin-top:3px}
.ascale{display:flex;justify-content:space-between;font-size:10.5px;color:var(--muted);
border-top:1px dashed var(--edge);padding-top:7px;margin-top:2px}
.caution{background:#faf1e9;border:1px solid #ead8c6;border-radius:9px;padding:12px 15px;font-size:12.5px;color:#6b5140;line-height:1.7}
.caution b{color:#8f5547}
""")

# 图 3 的条形高度需要内联样式，这里补上
FIG3 = FIG3.replace('<div class="abar a1"></div><div class="abar a2"></div><div class="abar a3"></div><div class="abar a4"></div>',
                    '<div class="abars"><div class="abar" style="height:38px"></div><div class="abar" style="height:50px"></div>'
                    '<div class="abar" style="height:60px"></div><div class="abar" style="height:64px"></div></div>')
FIG3 = FIG3.replace('<div class="abar b1"></div><div class="abar b2"></div><div class="abar b3"></div>',
                    '<div class="abars"><div class="abar" style="height:56px;background:linear-gradient(180deg,#6e9c8c,#486d63)"></div>'
                    '<div class="abar" style="height:42px;background:linear-gradient(180deg,#c4a284,#a77e4b)"></div>'
                    '<div class="abar" style="height:28px;background:linear-gradient(180deg,#c4a284,#a77e4b)"></div></div>')
FIG3 = FIG3.replace('.abars{display:flex', '.abars{display:flex')  # no-op，保持结构

# ---------------------------------------------------------------- 图 4 · 工程图
FIG4 = page("""
<div class="overline"><span class="no">图 4 / 工程</span>LANGCHAIN · RUN / TRACE / THREAD</div>
<h1>Agent 评测的三个粒度</h1>
<div class="thesis"><b>核心结论：</b>粒度决定你能发现什么 —— <b>局部错误</b>、<b>路径问题</b>、<b>长期漂移</b>不在同一层，只测一层必然漏。</div>

<div class="pyr">
  <div class="tier t1 card">
    <div class="l1"><span class="en">RUN</span><span class="zh">单步</span></div>
    <div class="grid2">
      <p><b>评什么：</b>一次 LLM 决策或工具调用 —— 工具是否选对、参数是否正确</p>
      <p><b>适合发现：</b>局部错误，能精确定位到具体某一步</p>
    </div>
  </div>
  <div class="tier t2 card">
    <div class="l1"><span class="en">TRACE</span><span class="zh">完整单轮执行</span></div>
    <div class="grid2">
      <p><b>评什么：</b>最终输出 + 执行轨迹 + 外部状态变化</p>
      <p><b>适合发现：</b>路径问题、单次任务是否可靠完成</p>
    </div>
  </div>
  <div class="tier t3 card">
    <div class="l1"><span class="en">THREAD</span><span class="zh">多轮会话</span></div>
    <div class="grid2">
      <p><b>评什么：</b>跨轮意图理解、上下文一致性、记忆使用与任务完成</p>
      <p><b>适合发现：</b>意图漂移、长期状态问题等单轮测不出的缺陷</p>
    </div>
  </div>
</div>

<div class="card tradeoff">
  <div class="h3">轨迹评测的关键取舍：必要约束 vs 允许变化</div>
  <div class="vs">
    <div class="v hard"><b>必要约束（硬性）</b>
      <p>先获得授权，再执行敏感动作 —— 顺序本身就是安全要求，违反即失败</p></div>
    <div class="v soft"><b>允许变化（弹性）</b>
      <p>先查文件再搜索 / 先搜索再定位文件 —— 两条路径都合法且完成任务，不应因路径不同判错</p></div>
  </div>
</div>

<div class="foot"><span>Agent Evaluation 阅读笔记 · 图 4</span><span>不要预先规定唯一标准 Workflow 让所有 Agent 照抄</span></div>
""", """
.pyr{display:flex;flex-direction:column;align-items:center;gap:11px;margin-top:4px}
.tier{padding:15px 24px 13px}
.t1{width:62%}.t2{width:81%}.t3{width:100%}
.t1{border-top:4px solid var(--qing)} .t2{border-top:4px solid var(--ochre)} .t3{border-top:4px solid var(--blush)}
.l1{display:flex;align-items:baseline;gap:10px;margin-bottom:7px}
.l1 .en{font:750 17px Georgia,serif;letter-spacing:.04em;color:var(--dark)}
.t1 .en{color:var(--qing)}.t2 .en{color:var(--ochre)}.t3 .en{color:var(--blush)}
.l1 .zh{font-size:12.5px;color:var(--muted)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6px 18px}
.grid2 p{font-size:13px;color:#4b534c;line-height:1.65}
.grid2 b{color:var(--dark)}
.tradeoff{margin-top:20px;padding:18px 22px}
.h3{font-size:13px;font-weight:700;color:var(--dai);letter-spacing:.06em;margin-bottom:12px}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.v{border-radius:9px;padding:13px 16px;font-size:13px;line-height:1.7}
.v b{display:block;margin-bottom:4px;font-size:13.5px}
.v p{color:#4b534c}
.hard{background:#edf3ed;border:1px solid #ceded3}.hard b{color:#2f5d50}
.soft{background:#f1eadf;border:1px solid #e0d3b8}.soft b{color:#8a6a3d}
""")

# ---------------------------------------------------------------- 图 5 · 总结图
def _ring_positions():
    import math
    cx = cy = 390
    r = 295
    names = [("Harness Design", "组织模型 · 工具 · 上下文 · 控制"),
             ("Agent Execution", "执行真实任务"),
             ("Trace & Outcome", "轨迹 + 结果 + 状态变化"),
             ("Evaluation", "Outcome / Trajectory / State"),
             ("Failure Analysis", "Error Pattern · Cost · Safety · Recovery"),
             ("Harness Optimization", "改动是否真正有效？")]
    out = []
    for i, (t, s) in enumerate(names):
        deg = math.radians(-90 + 60 * i)
        x = cx + r * math.cos(deg)
        y = cy + r * math.sin(deg)
        out.append(f'<div class="rnode" style="left:{x:.0f}px;top:{y:.0f}px"><b>{t}</b><small>{s}</small></div>')
    return "".join(out)


FIG5 = page(f"""
<div class="overline"><span class="no">图 5 / 总结</span>HARNESS × EVALUATION · FEEDBACK LOOP</div>
<h1>Agent 工程的迭代闭环</h1>
<div class="thesis"><b>核心结论：</b>Harness 负责组织和释放能力，Evaluation 提供判断系统是否真正达到目标的<b>证据</b> —— 两者缺一，都只能靠经验和 Demo 驱动。</div>

<div class="ringwrap">
  <svg class="ring" width="780" height="780" viewBox="0 0 780 780">
    <circle cx="390" cy="390" r="295" fill="none" stroke="#b9c9be" stroke-width="2" stroke-dasharray="7 8"/>
    <polygon points="404,88 388,80 398,66" fill="#a77e4b"/>
  </svg>
  <div class="center">
    <div class="cl">只有当 Harness 与 Evaluation<br>构成<b>反馈闭环</b>，<br>Agent 工程才真正进入<br><b>可迭代的系统化阶段</b></div>
  </div>
  {_ring_positions()}
</div>

<div class="foot"><span>Agent Evaluation 阅读笔记 · 图 5</span><span>模型决定能力 · Harness 释放能力 · Evaluation 提供证据</span></div>
""", """
.ringwrap{position:relative;width:780px;height:780px;margin:6px auto 0}
.ring{position:absolute;left:0;top:0}
.center{position:absolute;left:390px;top:390px;transform:translate(-50%,-50%);width:330px;height:330px;
border-radius:50%;background:radial-gradient(circle at 32% 26%,#3d6055,#233b3c 72%);
display:flex;align-items:center;justify-content:center;box-shadow:0 14px 40px rgba(35,59,60,.28)}
.cl{color:#eef4f0;font-size:19.5px;line-height:1.85;text-align:center;font-weight:500;padding:0 30px}
.cl b{color:#a8cdbe;font-weight:750}
.rnode{position:absolute;transform:translate(-50%,-50%);background:var(--paper);border:1px solid var(--edge);
border-radius:11px;padding:11px 15px;text-align:center;width:206px;box-shadow:0 5px 18px rgba(38,45,37,.08)}
.rnode b{display:block;font:700 14.5px Georgia,serif;color:var(--dai);letter-spacing:.01em}
.rnode small{display:block;font-size:11px;color:var(--muted);margin-top:3px;line-height:1.5}
""")


def render(figures: dict):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": WIDTH, "height": 900}, device_scale_factor=2)
        pg = ctx.new_page()
        for name, html in figures.items():
            pg.set_content(html, wait_until="networkidle")
            pg.wait_for_timeout(250)
            out = OUT_DIR / f"{name}.png"
            pg.screenshot(path=str(out), full_page=True)
            print(f"  generated {out.name}")
        browser.close()


if __name__ == "__main__":
    figures = {
        "fig1_what_to_evaluate": FIG1,
        "fig2_benchbuilder_pipeline": FIG2,
        "fig3_requirements_dag_ablation": FIG3,
        "fig4_run_trace_thread": FIG4,
        "fig5_harness_eval_loop": FIG5,
    }
    render(figures)
    print("all figures done")
