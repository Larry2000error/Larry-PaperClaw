# Daily Reports

最近三天日报（最新在前）：

# [20260915](./202609/20260915.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI领域聚焦多模态大模型的检索与生成能力优化。两项研究分别从区域级检索增强和跨模态对齐角度切入，探索视觉-语言模型的细粒度理解与高效表征，推动多模态系统在精准定位与灵活生成方面的技术边界。

## ✨ 今日亮点

- RegRet提出区域级检索框架，通过区域感知编码器增强大模型的细粒度定位能力
- FLAT创新将图像文本重采样为1D可变长度对齐令牌，统一检索与生成任务
- 两项研究均来自产业界与学术界合作，体现多模态技术向实用化迈进

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260915] RegRet: Enhancing Region-Level Retrieval in Large Multimodal Models | Liang Xun, Yang Honghui, Pan Weihang, Zhao Ruisi, Pan Boyuan, Hu Yao, Wang Wenxiao, Lin Binbin, Cai Deng | State Key Lab of CAD&CG, Zhejiang University；Xiaohongshu Inc.；School of Software Technology, Zhejiang University | RegRet通过区域感知编码器与对比学习，提升大模型在区域级视觉-语言检索中的细粒度定位能力。 | [#507](https://github.com/Larry2000error/Larry-PaperClaw/issues/507) |
| [20260915] FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation | Sun Guangyu, Shlok Kumar Mishra, Bao Wentao, Robert Zhenheng Yang, Wang Xiao, Wang Xiyuan, Ma Yujunrong, Yuan Chen, Max Xiangjun Fan, Xiao Jun, Cheng Jianpeng | Meta AI | FLAT将图像和文本重采样为1D灵活长度对齐令牌，实现跨模态检索与生成的统一高效框架。 | [#508](https://github.com/Larry2000error/Larry-PaperClaw/issues/508) |

## 🔎 观察

- 区域级检索成为多模态大模型的新焦点，反映应用层对空间细粒度理解的迫切需求
- 1D令牌化与长度灵活设计或成为跨模态架构的新范式，兼顾效率与任务统一性

---

Powered by OpenClaw🦞

---

# [20260914](./202609/20260914.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 4 篇。

今日研究聚焦多模态检索与智能体系统两大方向。多模态检索领域出现两项几何方法创新，分别探索球面质心聚合与超图正则化；视觉文档理解则向Agentic架构演进，强调显式证据选择与上下文整合。此外，低资源语言评测的有效性边界问题引发关注。

## ✨ 今日亮点

- Agentic视觉RAG通过显式证据选择与上下文整合，解决稀疏证据场景下的文档理解难题
- 两项独立研究从球面几何与超图正则化切入，为跨模态检索提供新的嵌入优化范式
- 土耳其语MMLU Pro研究揭示选项增强策略的有效性边界，警示基准评测的方法论风险

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260914] Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation | Shen Yucheng, Yan Lingyong, Wu Jiulong, Wang Shuaiqiang, WU Jianmin, Yin Dawei, Cao Min | School of Computer Science and Technology, Soochow University；Baidu Inc. | 提出Agentic视觉RAG框架，通过显式上下文选择与整合机制，提升稀疏证据场景下的文档推理能力。 | [#502](https://github.com/Larry2000error/Larry-PaperClaw/issues/502) |
| [20260914] Turkish MMLU Pro: Traceable Option Augmentation and Its Validity Limits in Turkish Multiple-Choice Evaluation | M. Ali Bayram | Yıldız Technical University | 构建土耳其语MMLU Pro基准，系统评估选项增强策略的可追溯性与有效性边界。 | [#503](https://github.com/Larry2000error/Larry-PaperClaw/issues/503) |
| [20260914] Query-Conditioned Spherical Centroid Aggregation for Multimodal Retrieval | Mehrish Ambuj, Nag Anindya, Vascon Sebastiano | Ca' Foscari University of Venice | 设计查询条件化的球面质心聚合方法，结合LoRA适配器实现自适应模态加权的多模态检索。 | [#504](https://github.com/Larry2000error/Larry-PaperClaw/issues/504) |
| [20260914] Hypergraph-Regularized Gramian Volumes for Multimodal Retrieval | Nag Anindya, Mehrish Ambuj, Vascon Sebastiano | Ca' Foscari University of Venice | 引入超图正则化的Gramian体积度量，通过高阶结构约束优化跨模态嵌入空间。 | [#505](https://github.com/Larry2000error/Larry-PaperClaw/issues/505) |

## 🔎 观察

- 多模态检索正从欧氏空间向非欧几何拓展，球面与超图方法的同期出现暗示该领域正寻求更契合语义结构的数学表征。
- Agentic系统与RAG的深度融合成为文档智能新趋势，显式证据管理或成缓解视觉语言模型幻觉的关键路径。

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
