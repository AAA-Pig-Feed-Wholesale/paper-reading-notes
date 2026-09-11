最近集中读了 2 篇 Agent Harness 相关论文，以及 OpenAI、LangChain、Anthropic 的 3 篇工业实践文章。几篇材料放在一起看，基本能形成一条完整链路：**从 Harness 的理论框架，到真实 Coding Agent 的源码结构，再到工业界如何设计 Agent-first 工程系统。**

最核心的变化是，Agent 工程的关注点正在从“模型能不能完成任务”，逐渐转向“系统能不能长期、稳定、可控地让模型完成任务”。

## 1. 为什么现在开始讲 Harness？

早期 Agent 讨论通常集中在几个层次：Prompt Engineering 解决“如何让模型回答得更好”；Context Engineering 解决“模型当前应该看到什么”；Agent Engineering 开始关注 Tool Calling、Planning、Workflow、Multi-Agent。

但一旦 Agent 真正进入生产环境，问题会迅速复杂起来：工具调用失败后如何恢复？长任务中断后如何继续？Context 持续膨胀怎么办？Agent 是否有权限执行某个动作？怎么判断任务真的完成，而不是模型自己宣布完成？如何记录执行轨迹、控制成本？模型升级之后，原来的 Workflow 是否还合理？

这些问题已经很难仅靠 Prompt 或单一编排框架解决。

更准确地说：

> **Harness 是把模型能力转化为可执行、可持续、可验证、可治理系统能力的工程层。**

模型决定“有没有能力”，Harness 决定“这种能力能不能稳定释放出来”。

## 2. 第一篇 Survey 给出了一张完整地图

《Agent Harness Engineering: A Survey》提出了 ETCLOVG 七层：

**E — Execution**：Shell、Browser、Filesystem、Sandbox。
**T — Tooling**：Tools、MCP、外部 API、协议。
**C — Context**：Memory、Retrieval、Compaction、上下文管理。
**L — Lifecycle & Orchestration**：Agent Loop、State、Workflow、Session。
**O — Observability**：Trace、Log、Metrics。
**V — Verification & Evaluation**：Tests、Verifier、Agent Eval。
**G — Governance & Security**：Permission、Policy、Audit、安全边界。

这个框架最有价值的地方，是把很多容易混淆的概念重新分层。

例如，**LangGraph 并不等于 Agent Harness**。LangGraph 更接近 Lifecycle & Orchestration，主要负责 Agent 生命周期、状态流转和 Workflow 编排；MCP 更接近 Tooling / Protocol，解决 Agent 如何标准化连接外部工具和数据源；Harness 则是更大的系统边界，还包括 Execution、Context、Observability、Verification、Governance 和 Security。

所以 LangGraph、MCP、Harness 并不是简单的平级关系。

## 3. 第二篇源码研究揭示了生产 Coding Agent 的真实结构

《Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents》直接分析了 Claude Code、Codex CLI、Gemini CLI、OpenHands、Aider、OpenClaw 等 11 个系统的源码。

相比理论综述，这篇更像一次“真实工程解剖”。

其中第一个值得注意的结论是：**这些生产级 Coding Agent 的核心 Runtime 几乎不依赖通用 Agent Framework。**

作者检查了 LangChain、LangGraph、AutoGen、CrewAI、Semantic Kernel 等框架，结果是它们几乎没有直接出现在核心 runtime path 中。生产系统更常见的做法是使用原生 async primitives，自行实现 agent loop、自定义 tool schema、自维护 state，并自己控制 permission 与 execution。

这并不意味着通用框架没有价值，更可能说明：

> **当 Agent 真正产品化以后，Harness 本身正在逐渐承担 Framework 的角色。**

真正的生产 Harness 往往已经包含 Runtime、Tool System、State Management、Extension System、Permission Model、Session System 和 Observability，本身就是一套完整的系统框架。

## 4. 代码检索几乎不用 Vector RAG

另一个很有意思的发现是，这些 Coding Agent 检索代码时，更常使用 ripgrep、glob、tree-sitter、LSP、文件路径、repo structure、AGENTS.md / README，而不是先把整个代码仓库做 embedding。

原因并不复杂。代码本身具有很强的确定性结构：文件路径、函数名、符号引用、AST、调用关系，这些信息很多时候比语义 embedding 更可靠。同时代码仓库变化频率高，预构建向量索引容易失效，还会引入额外维护成本。

这说明：

> **RAG 不是 Agent 系统的默认答案，Retrieval Mechanism 应该由任务结构决定。**

文档问答适合向量检索，并不意味着代码仓库同样适合。

## 5. Skills、MCP、ACP 正在推动 Harness 平台化

源码研究里还有一个明显趋势：越来越多 Harness 开始支持 SKILL.md、MCP、Hooks、Plugins、ACP、A2A、SDK、HTTP Server、Hosted Runtime。

这意味着 Harness 正从“单一工具”变成“平台”。

特别是 Skill。它表面上只是 Markdown + YAML metadata，但实际越来越像一个面向 LLM Runtime 的声明式程序，可以描述什么时候触发、完成什么任务、调用哪些工具、拥有哪些权限、使用哪些脚本，以及输入输出约束。

因此 Skill 的角色已经开始接近传统软件中的 package / plugin / capability bundle。

这也是为什么在越来越多 Agent 系统里，Skill、MCP、Plugin System 会一起出现。

## 6. LangChain 提供了一种很实用的 Harness 设计方法

《The Anatomy of an Agent Harness》给出了一个很清晰的思路：不要先问“Harness 应该有哪些模块”，而应该先问：

> **模型原生在哪些行为上存在能力缺口？**

然后再补对应能力。

模型无法长期保存状态 → Filesystem / Memory；模型不知道训练后的新知识 → Search / MCP；模型上下文越来越长 → Compaction；模型需要执行真实操作 → Bash / Tools；执行代码存在风险 → Sandbox；长任务容易偏离目标 → Planning；需要并行探索 → Sub-Agent；容易提前宣布任务完成 → Verification Loop。

这种设计方式本质上可以概括为：

> **Failure-driven Harness Design**

即由实际失败模式反推 Harness，而不是为了“架构完整”去堆功能。

## 7. OpenAI：环境是否对 Agent 可读，比单纯“会不会写代码”更重要

OpenAI 的 Harness Engineering 文章里，有一个很重要的概念：**Agent Legibility**。

一个系统如果主要由 Agent 参与开发，那么整个工程环境都必须对 Agent 可理解。如果关键知识只存在于 Slack、飞书、Google Docs 或某个工程师脑子里，那么对于运行中的 Agent 来说，这些信息几乎等于不存在。

因此越来越多知识需要重新变成 repo-local，例如 Architecture Docs、Execution Plans、Tests、Logs、Metrics、Traces、Rules、Lints。

软件工程里的“可读性”因此正在发生变化。

过去主要考虑：

**Human-readable**

现在还需要考虑：

**Agent-readable**

## 8. 好的约束不是限制 Agent，而是在扩大它的安全自治空间

OpenAI 的另一个实践也很值得关注：Agent 越自主，并不意味着约束越少。

dependency direction、schema、naming convention、structured logging、architecture boundary、file size、testing requirements，如果只写在文档里，Agent 很容易违反；但如果被编码成 lint、structural test、CI rule、policy，那么 Agent 就可以在清晰边界内高速行动。

因此 Guardrail 更准确的理解不是“限制 Agent”，而是：

> **定义 Agent 可以安全自治的空间。**

## 9. Anthropic：Harness 不是越复杂越好

Anthropic 在长任务 Agent 实验中曾使用很多 scaffold：Context Reset、Structured Handoff、Sprint Decomposition、Planner、Generator、Evaluator。

这些机制在早期模型上非常重要，但随着模型能力提升，其中一些组件会逐渐失去作用。例如，当模型已经能在更长上下文中维持 coherence，过去强制 context reset 的必要性就会下降。

因此一个很重要的 Harness Engineering 原则是：

> **模型升级之后，不只是考虑加什么，还要重新判断哪些 Harness 可以删掉。**

这和传统软件框架有明显区别。传统 Framework 通常强调接口长期稳定，而 Agent Harness 必须持续跟随模型能力边界变化。

## 10. Evaluator 也不是默认必需组件

Anthropic 还指出，Evaluator 是否有价值，取决于任务是否接近模型能力边界。

如果任务本身已经处于模型高可靠区间，Generator + Evaluator 可能只是额外增加 token、时间和成本；只有当任务接近模型能力极限时，Evaluator 才真正提供明显收益。

这说明 Agent 系统里的很多模块不能简单问“应不应该有”，而应该问：

> **在什么条件下值得存在？**

这可能是 Harness Engineering 很重要的一种架构思维。

## 11. 把五篇文章合起来，可以得到一张更完整的 Harness 图

一个生产级 Agent Harness，大致可以包含：

**Context**：Memory、Retrieval、Compaction、Skills
**Execution**：Filesystem、Shell、Browser、Sandbox
**Tooling**：Tools、MCP、API、Plugin
**Lifecycle**：Agent Loop、Workflow、State、Session
**Verification**：Tests、Evaluator、Self-review、Acceptance Criteria
**Observability**：Logs、Trace、Metrics
**Governance**：Permission、Policy、Audit、Cost Control

因此真正的 Agent System 更接近：

> **Model + Harness**

而不是：

> **Model + Prompt**

## 12. Agent 系统的竞争正在逐渐变成 Model × Harness

未来 Agent 系统之间的差距，很可能不只是模型参数和 Benchmark 的差距。

同一个模型，在不同的 Context Strategy、Tool Interface、Sandbox、Memory、Verification Loop、Permission System、Feedback Loop 下，最终表现可能完全不同。

反过来，模型能力升级之后，旧的 Harness 也可能迅速过时。

所以 Harness Engineering 不太像一个“模型还不够强时期的过渡方案”，更可能是一种长期存在的工程层。原因并不是模型不够智能，而是：

> **模型越强，人们越会把更复杂、更长期、更高风险的任务交给它。**

而这些任务最终都需要一个足够成熟的运行系统承载。

这 5 篇材料放在一起看，最大的价值不是多记几个 Agent 术语，而是把原本分散的：

**LangGraph / MCP / Skills / Memory / Sandbox / Runtime / Agent Eval / Observability / Governance**

重新放回同一张系统图里。

它们共同回答的是同一个问题：

> **怎样让模型从“会做”，真正走向“长期、稳定、可控地做”。**
