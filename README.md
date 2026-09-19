# Paper Reading Notes

这里记录我在阅读论文、技术文章和研究资料后的理解、整理与思考，内容主要关注 AI Agent、Harness Engineering、Coding Agent 及相关工程实践。

## 在线阅读

**[进入论文阅读笔记](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/)**

## 当前内容

### 2026-09-18

| 主题 | 在线阅读 |
| --- | --- |
| A Survey on Evaluation of LLM-based Agents｜ACL 2026 综述精读 | [阅读文章](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/9.18/agent_evaluation_survey_acl2026_reading.html) |
| LLM-as-a-Judge｜MT-Bench 与 Chatbot Arena · 论文精读 | [阅读文章](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/9.18/agent_eval_llm_as_judge_mt_bench_arena_reading.html) |
| Arena-Hard × BenchBuilder｜论文精读 | [阅读文章](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/9.18/agent_eval_arena_hard_benchbuilder_reading.html) |
| Agent-as-a-Judge｜论文精读 | [阅读文章](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/9.18/agent_eval_agent_as_a_judge_2025_reading.html) |
| Agent Arena｜真实世界 Agent 因果评测 · 官方技术文章精读 | [阅读文章](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/9.18/agent_eval_agent_arena_causal_methodology_reading.html) |
| Agent Evaluation 工业实践精读｜LangChain × 火山引擎 | [阅读文章](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/9.18/agent_eval_industry_practices_langchain_volcengine.html) |

### 2026-09-11

| 主题 | 在线阅读 |
| --- | --- |
| Agent Harness Engineering: A Survey｜论文精读与解读 | [阅读文章](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/9.11/agent_harness_survey_learning_v4.html) |
| Harness Engineering：11 个 Coding Agent 源码解剖 | [阅读文章](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/9.11/harness_engineering_coding_agents_source_study.html) |
| Agent Harness 工业实践三篇精读｜OpenAI × LangChain × Anthropic | [阅读文章](https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/9.11/agent_harness_industry_openai_langchain_anthropic.html) |

## 仓库结构

```text
paper-reading-notes/
├── index.html
├── README.md
├── .nojekyll
├── 9.11/
│   ├── agent_harness_survey_learning_v4.html
│   ├── harness_engineering_coding_agents_source_study.html
│   └── agent_harness_industry_openai_langchain_anthropic.html
└── 9.18/
    ├── agent_evaluation_survey_acl2026_reading.html
    ├── agent_eval_llm_as_judge_mt_bench_arena_reading.html
    ├── agent_eval_arena_hard_benchbuilder_reading.html
    ├── agent_eval_agent_as_a_judge_2025_reading.html
    ├── agent_eval_agent_arena_causal_methodology_reading.html
    └── agent_eval_industry_practices_langchain_volcengine.html
```

- 根目录保存网站首页、README 和发布配置。
- 每次更新的文章按照日期放入对应目录。
- 每篇笔记使用独立 HTML 页面，便于直接阅读和分享。

## 本地查看

```bash
git clone https://github.com/AAA-Pig-Feed-Wholesale/paper-reading-notes.git
cd paper-reading-notes
```

随后直接使用浏览器打开根目录的 `index.html`。

## 更新方式

1. 为当次更新建立日期目录，例如 `9.12/`。
2. 将新增 HTML 文件放进该目录。
3. 在 `index.html` 和 `README.md` 中添加文章入口。
4. 提交并推送到 `main` 分支，GitHub Pages 会自动重新发布。

## 关于内容

这些笔记用于个人学习和知识整理，并不替代原论文或原始资料。阅读时建议结合文章中引用的原始来源。

持续更新中。
