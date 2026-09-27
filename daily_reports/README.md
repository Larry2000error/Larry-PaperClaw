# Daily Reports

最近三天日报（最新在前）：

# [20260915](./202609/20260915.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 2 篇。

今日研究聚焦于多模态大模型的表征学习与跨模态对齐。两项工作分别从区域级检索增强和灵活长度token对齐两个角度，探索提升视觉-语言模型细粒度理解与生成能力的新路径，体现向更高效、更精准多模态交互发展的趋势。

## ✨ 今日亮点

- RegRet提出区域感知编码器，增强大模型区域级检索能力
- FLAT将图文重采样为1D灵活长度对齐token，统一检索与生成
- 两项工作均来自产业界与学术界合作，凸显产学研融合态势

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260915] RegRet: Enhancing Region-Level Retrieval in Large Multimodal Models | Liang Xun, Yang Honghui, Pan Weihang, Zhao Ruisi, Pan Boyuan, Hu Yao, Wang Wenxiao, Lin Binbin, Cai Deng | State Key Lab of CAD&CG, Zhejiang University；Xiaohongshu Inc.；School of Software Technology, Zhejiang University | RegRet通过区域感知编码器与对比学习，提升大模型对图像局部区域的细粒度检索能力。 | [#507](https://github.com/Larry2000error/Larry-PaperClaw/issues/507) |
| [20260915] FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation | Sun Guangyu, Shlok Kumar Mishra, Bao Wentao, Robert Zhenheng Yang, Wang Xiao, Wang Xiyuan, Ma Yujunrong, Yuan Chen, Max Xiangjun Fan, Xiao Jun, Cheng Jianpeng | Meta AI | FLAT将图像和文本重采样为统一1D灵活长度token序列，实现跨模态检索与生成的端到端优化。 | [#508](https://github.com/Larry2000error/Larry-PaperClaw/issues/508) |

## 🔎 观察

- 区域级理解正成为多模态大模型差异化竞争的关键技术方向。
- 一维token化方案有望降低跨模态对齐复杂度，但计算效率仍需验证。

---

Powered by OpenClaw🦞

---

# [20260914](./202609/20260914.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 4 篇。

今日研究聚焦多模态检索与智能体系统两大方向。多模态检索领域出现两项球面几何与超图正则化新方法，强调查询条件聚合与嵌入空间优化。文档理解方向探索视觉RAG的显式证据选择机制。此外，土耳其语大模型评测的选项增强有效性研究为低资源语言评估提供新视角。

## ✨ 今日亮点

- 球面质心聚合：通过查询条件动态加权实现多模态检索的模态自适应融合
- 超图正则化：利用格拉姆体积约束优化跨模态嵌入空间的结构化关系
- 显式证据选择：智能体视觉RAG通过上下文整合解决稀疏证据导航难题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260914] Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation | Shen Yucheng, Yan Lingyong, Wu Jiulong, Wang Shuaiqiang, WU Jianmin, Yin Dawei, Cao Min | School of Computer Science and Technology, Soochow University；Baidu Inc. | 提出显式上下文选择与整合机制，使智能体视觉RAG系统能够主动导航稀疏证据场景。 | [#502](https://github.com/Larry2000error/Larry-PaperClaw/issues/502) |
| [20260914] Turkish MMLU Pro: Traceable Option Augmentation and Its Validity Limits in Turkish Multiple-Choice Evaluation | M. Ali Bayram | Yıldız Technical University | 构建土耳其语MMLU Pro基准，系统追踪选项增强方法的有效性及适用边界。 | [#503](https://github.com/Larry2000error/Larry-PaperClaw/issues/503) |
| [20260914] Query-Conditioned Spherical Centroid Aggregation for Multimodal Retrieval | Mehrish Ambuj, Nag Anindya, Vascon Sebastiano | Ca' Foscari University of Venice | 设计查询条件球面质心聚合方法，通过LoRA适配器实现多模态检索的动态模态加权。 | [#504](https://github.com/Larry2000error/Larry-PaperClaw/issues/504) |
| [20260914] Hypergraph-Regularized Gramian Volumes for Multimodal Retrieval | Nag Anindya, Mehrish Ambuj, Vascon Sebastiano | Ca' Foscari University of Venice | 引入超图正则化格拉姆体积约束，优化多模态检索中的跨模态嵌入空间结构。 | [#505](https://github.com/Larry2000error/Larry-PaperClaw/issues/505) |

## 🔎 观察

- 多模态检索正从简单对齐转向几何结构约束与查询自适应的精细化建模，数学工具深度介入。
- RAG系统研究重心后移，从检索增强本身转向智能体的主动证据选择与上下文整合策略。

---

Powered by OpenClaw🦞

---

# [20260913](./202609/20260913.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦多模态安全与高效推理两大方向。ViTeGate揭示视觉-语言检索增强生成中的知识投毒攻击风险，而多相机行人重识别框架则探索生成式AI与早退级联结合的低延迟方案。两者分别关注VLM的安全漏洞与实时性能优化，体现该领域攻防并进的发展态势。

## ✨ 今日亮点

- ViTeGate首次针对VLM检索增强生成场景设计视觉-文本触发式知识投毒攻击
- 多相机行人重识别框架整合生成式AI与早退级联机制实现低延迟推理
- 两篇论文均涉及视觉-语言模型，分别聚焦安全性与效率优化两个维度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260913] ViTeGate: Visual-Textual Triggered Knowledge Poisoning for Vision-Language Retrieval-Augmented Generation | Tan Xue, Zeng Xuandi, Shao Yu, Fang Zhongli, Luo Mingyu, Sun Xiaoyan, Chen Ping, Dai Jun | Fudan University；Guangdong University of Technology；Worcester Polytechnic Institute | ViTeGate提出视觉-文本触发知识投毒方法，揭示VLM检索增强生成系统在多模态对抗攻击下的安全漏洞。 | [#499](https://github.com/Larry2000error/Larry-PaperClaw/issues/499) |
| [20260913] A Generative AI Integrated Multimodal Framework for Low-Latency Multi-Camera Person Re-Identification | Fernando Leon, Dombawala C, Hettigoda P., Vanodhya G. Warnasooriya, Neranjana Ishara, Nawaratne Rashmika | University of Moratuwa；Zone24x7 (Pvt) Ltd；Chulalongkorn University；University of Colombo；La Trobe University | 该框架融合生成式AI与早退级联架构，构建面向多相机场景的低开销行人重识别系统。 | [#500](https://github.com/Larry2000error/Larry-PaperClaw/issues/500) |

## 🔎 观察

- VLM安全研究从传统对抗样本向检索增强生成等复杂场景延伸，知识投毒成为新兴威胁向量。
- 生成式AI与早退机制的跨架构整合，反映边缘实时应用对效率与精度的双重诉求。

---

Powered by OpenClaw🦞

---
