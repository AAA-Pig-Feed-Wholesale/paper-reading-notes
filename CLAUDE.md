# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库性质

论文阅读笔记静态网站，通过 GitHub Pages 发布（https://aaa-pig-feed-wholesale.github.io/paper-reading-notes/）。没有构建系统、包管理器和测试——HTML 文件本身就是站点。内容主题：AI Agent、Harness Engineering、Agent Evaluation 等，全部为中文精读笔记。

## 结构

- `index.html`：站点首页，按日期分组的文章卡片列表，使用**相对链接**指向日期目录下的 HTML。
- `README.md`：仓库说明 + 与首页同步的文章目录，使用 **GitHub Pages 绝对 URL**。
- 日期目录（`9.11/`、`9.18/` …）：每篇笔记一个**自包含** HTML 文件——CSS 全部内联、原生 JS 实现交互（tabs / quiz / collapsible 等），无任何外部依赖或框架。
- 日期目录内可能保留 Markdown 草稿（如 `agent harness_911.md`、`agent eval_918.md`），是 HTML 成稿的素材/大纲，不发布。
- 根目录 PDF 是本地参考资料，已被 `.gitignore`（`/*.pdf`）排除，不会提交或发布。

## 发布流程（每批新笔记）

1. 新建日期目录（如 `9.19/`），HTML 文件放入其中；命名沿用同批模式（9.18 为 `agent_eval_*_reading.html`）。
2. 在 `index.html` **和** `README.md` 两处都登记新文章——这两个目录必须同步维护，缺一会导致首页或仓库页看不到新文章。
3. 提交并推送到 `main`，GitHub Pages 自动重新发布。无本地构建步骤；本地预览直接用浏览器打开 `index.html`。

## 写作约定

- 全部内容为中文（zh-CN），技术术语保留英文原名（如 Harness、Benchmark、Trajectory）。
- 新 HTML 应匹配同批次已有文章的视觉设计：整体版式沿用 `mast / nav / sec / card / quiz / callout` 等结构类名，配色按批次自定（9.11 与 9.18 是两套不同主题色）。
- 笔记定位是"精读"：明确区分"原文结论"与"个人解读"，页码引用（`<span class="ref">PDF pp.X</span>`）指向本地 PDF 的实际页码。
